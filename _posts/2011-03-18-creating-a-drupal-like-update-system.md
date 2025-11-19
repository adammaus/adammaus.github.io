---
layout: post
title: Creating a Drupal-like update system
date: 2011-03-18T13:56:58-05:00
excerpt: During a recent project I was working on, I came across a problem which involves easily updating a web application and its database from a customer standpoint. I have rarely worked on a system that is used by others and requires an update path so this presented a unique opportunity to learn how one could develop a system that is relatively simple to update.
permalink: 2011/03/creating-a-drupal-like-update-system/
tags:
  - Software Development
---
During a recent project I was working on, I came across a problem which involves easily updating a web application and its database from a customer standpoint. I have rarely worked on a system that is used by others and requires an update path so this presented a unique opportunity to learn how one could develop a system that is relatively simple to update.

I believe this is basically what Drupal does when they push updates and I can't imagine this is novel in any way.

So hypothetically, lets say you just released version 1.1 of your application. You are now potentially catering to two different customers, someone who just bought your application or someone that is updating from version 1.0.

Let's tackle the first time user so you can get a gist what I am proposing.

In the base of your application, much like Drupal, you can include a file named "Install.xyz", this is the first file that your first-time customer would go to in order to set up the application on their web server.

Install.xyz would do three things:

1. Create the database tables required in your application
2. Write a settings.xyz file that stores database configuration information such as the location, username, and password. This requires that this file is only write-able during the initial setup.
3. Reports errors and tries to correct them

Now with this set up, we do not want the customer to have to go into the database very often so when looking into how to update your web application, we must keep database integrity in mind. Let's look at how to create a way to update the application by creating Update.xyz.

Update.xyz does two things:

1. Executes queries to upgrade from each previous version of the application (optimization will be key if certain table columns are added and then removed between versions)
2. Reports any errors in upgrading and tries to correct them

We assume that when a customer is updating their application that they will download the new version of files and replace all files within the application. They should then run Update.xyz before attempting to run the application files. We could get tricky by putting in some sort of database version checking between the database and the web application files to force the customer into updating the database but for now, assume that the customer will manually run Update.xyz.

Since it was so easy to update the application, we now look at how to inform the user that a new version is available.

Assuming there is some sort of administration section for the application, we can put in a special script that checks your website for the latest version of the application. If the customer does not have the latest version, a nice little notification shows up asking the customer to download the new version and run Update.xyz

When all is said and done, we have created a system that is easy to maintain on the user's end and also helps reduce the amount of time we spend informing customers that a new version is available.