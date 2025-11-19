---
layout: post
title: Caching the results of a PDO Query in Memcache
date: 2014-07-15T16:06:09-05:00
excerpt: A quick example of code that will prepare a PDO statement and cache the results in Memcache in a LAMP environment.
permalink: 2014/07/caching-pdo-query-results-memcache/
tags:
  - Memcache
  - MySQL
  - PDO
  - PHP
---
This is a quick example of code that will prepare a [PDO statement](http://php.net/manual/en/book.pdo.php) and cache the results in [Memcache](http://memcached.org/).

It is easiest to use the two following sets of instructions to set up a LAMP environment that will handle the PHP, PDO, and Memcache packages that the code uses:

  1. [How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu)
  2. [How To Install and Use Memcache on Ubuntu 12.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-memcache-on-ubuntu-12-04)

Code

{% highlight php %}
<?php
function db_connect() {
	global $memcache, $db;

	// Connect to the Memcache server
	$memcache = new Memcache();
	$memcache->pconnect('localhost', 11211);

	// Connect to the Database using PDO
	$host = "localhost";
	$dbname = "test";
	$user = "test";
	$pass = "test";

	try {
		$db = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
	} catch (PDOException $e) {
		die($e->getMessage());
	}
}

function db_fetch_all($sql, $params = array(), $use_cache = true) {
	global $memcache, $db, $cache_expiration;

	$result = false;
	if ($use_cache) {
		// Generate a key for the cache
		$cache_key = md5($sql . serialize($params));
		$result = $memcache->get($cache_key);
	}

	if (!$result) {
		// Cache Miss: Prepare the sql and recache it
		$sth = $db->prepare($sql);

		// This handles ? within a sql query
		// i.e. "SELECT id FROM example WHERE name = ?";
		$i = 0;
		foreach ($params as $param) {
		    $sth->bindParam(++$i, $param);
		}

		// This handles :params within queries
		// "SELECT id FROM example WHERE name = :name";
		foreach ($params as $key => $value) {
		    // keys must be in the form :key within the query
		    $sth->bindParam($key, $value);
		}

		$sth->execute();
		$result = $sth->fetch(); // Fetch the entire result into an array

		// Cache expires in 10 seconds
                $cache_key = md5($sql . serialize($params));
		$cache_expiration = 10;
		$memcache->set($cache_key, serialize($result), MEMCACHE_COMPRESSED, $cache_expiration);

		echo "used mysql";
	} else {
		// Cache Hit
		echo "used memcache";
	}

	return $result;
}

echo "Time: " . time() . "<br />";
if (class_exists("Memcache")) {
	db_connect();

	// The query only works with ? as variables in the prepared statement
	$query = "SELECT id FROM example WHERE name = ?";
	$result = db_fetch_all($query, array("new_data"));

} else {
	echo "Memcache not installed :(";
}
?>
{% endhighlight %}