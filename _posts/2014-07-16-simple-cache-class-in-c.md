---
layout: post
title: 'Simple Cache Class in C#'
date: 2014-07-16T11:18:02-05:00
excerpt: 'A simple class that gets and sets Hashtables within a Session object in C#.'
permalink: 2014/07/simple-cache-class-in-c/
tags:
  - .NET
  - C
  - Caching
---
A simple class that caches Hashtables within a Session object in C#.

{% highlight c# %}
using System;
using System.Web;
using System.Web.SessionState;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;

public class Cache
{
	/**
	 * Delete the cache item from the cache by key
	 *
	 * @param string CacheKey: The data to delete
	 * @return bool: Indicates the cache key was deleted
	 **/
	public static bool Delete(string CacheKey)
	{
		HttpContext.Current.Session[CacheKey] = null;
		return true;
	}

	/**
	 * Get the cache item by key
	 *
	 * @param string CacheKey: The data to retrieve
	 * @return Hashtable: The data retrieved
	 **/
	public static Hashtable Get(string CacheKey)
	{
		if (HttpContext.Current.Session[CacheKey] != null)
		{
			Cache.Item item = (Cache.Item)HttpContext.Current.Session[CacheKey];
			if (item.Expiration >= DateTime.Now)
			{
				return item.Data;
			}
		}

		return null;
	}

	/**
	 * Set a cache item
	 *
	 * @param string CacheKey: The key to set for the item
	 * @param Hashtable Data: The data to set
	 * @param int NumSecondsAlive: The number of seconds to set the cache for (defaults to 5 seconds)
	 * @return Hashtable: The data retrieved
	 **/
	public static bool Set(string CacheKey, Hashtable Data = null, int NumSecondsAlive = 5)
	{
		Cache.Delete(CacheKey);
		HttpContext.Current.Session[CacheKey] = new Cache.Item(Data, NumSecondsAlive);

		return true;
	}

	/**
	 *
	 * Start Item Class
	 *
	 **/
	private class Item
	{
		public Hashtable Data = null;
		public DateTime Expiration = new DateTime();

		public Item(Hashtable Data, int NumSecondsAlive)
		{
			this.Data = Data;
			this.Expiration = DateTime.Now.AddSeconds(NumSecondsAlive);
		}
	} // End Item Class
} // End Cache Class
{% endhighlight %}

You may want to consider performance and efficiency when implementing this on an actual site.