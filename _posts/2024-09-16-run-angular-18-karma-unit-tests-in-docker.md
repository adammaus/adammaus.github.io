---
layout: post
permalink: "2024/09/run-angular-18-karma-unit-tests-in-docker/"
title: "Run Angular 18 Karma Unit Tests in Docker"
date: 2024-09-16T10:49:09-05:00
excerpt: Set up Karm Unit Tests for Angular v18 in a Docker container.
tags:
  - Angular
  - CI/CD
  - Docker
  - GitHub
  - Gitlab
  - Karma
---

I have been working on a frontend library using Ionic 8 and Angular v18 and wanted to set up Karma Unit Tests. One issue I ran into was getting the tests to run locally and, later, in a Docker container in a CI/CD pipeline so I put together a [GitHub Repository](https://github.com/adammaus/run-angular18-karma-in-docker) as an example. This details the updates I made from a base Angular app.

__Angular App Configuration__

If you have an existing Angular app or just ran `$ ng new <project>`, you can run `$ ng generate config karma` to generate a _karma.conf.js_ file and an updated _angular.json_.

You will need to add the following block to enable a ChromeHeadless browser to run the Karma Unit Tests packaged with the app. ChromeHeadless is necessary for a CI/CD but optional if you want to run the unit tests outside of a Docker container.

In _karma.conf.js_, add:

{% highlight bash %}
browsers: ['ChromeHeadlessNoSandbox'],
customLaunchers: {
  ChromeHeadlessNoSandbox: {
    base: 'ChromeHeadless',
    flags: ['--no-sandbox']
  }
}
{% endhighlight %}

I personally ran into issues using ChromeHeadless without the "–no-sandbox" flag which is why I had to add the karma.conf.js file and the Custom Launcher in the first place.

In _angular.json_, add the following under "tests" > "options" to give you a barebones output for CI/CD. In my case, I still wanted Code Coverage when I run this locally but codeCoverage could be considered optional.

{% highlight bash %}
"progress": false,
"watch": false,
"codeCoverage": true
{% endhighlight %}

A summary of these changes can be found in this [pull request](https://github.com/adammaus/run-angular18-karma-in-docker/pull/1/files).

From here, you should be able to run these tests locally using `$ ng test`.

__Fixing ChromesHeadless error__

If you're like me, you ran into a "Cannot start ChromeHeadless" error during testing. This happens if you don't have Chrome installed such as in a Docker container. This requires you to download and install it:

{% highlight bash %}
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb
{% endhighlight %}

Note: This is for installation in Linux inside of a Docker Container. You could also just download Chrome from their website.

Now, you should be able to run these tests locally using `$ ng test` without any problems.

__Setting up a Docker container for CI/CD__

After getting the tests to run locally and inside of a Docker container, I wanted to setup a Docker container to run these tests automatically on GitHub and Gitlab. You can use the dockerfile from the GitHub Repository to build the container and run the tests with `$ docker build -t angular-docker .; docker container run angular-docker ng test`

Just a note, from my really quick research, it looks like you do need to build or rebuild the container each time you make a change to the app or unit test code. You could also try setting up a continuously running container to make the tests run a bit faster.

In the [GitHub Repository](https://github.com/adammaus/run-angular18-karma-in-docker), I've also included basic scripts for a Github Actions Workflow and Gitlab CI Pipeline that should run those tests during each pull/merge request.

As part of your own CI/CD, you are welcome to use the [adammaus/run-angular18-karma-in-docker](https://hub.docker.com/repository/docker/adammaus/run-angular18-karma-in-docker/general) Docker container but the repo's dockerfile contains all the instructions used for that container.

That Docker container happens to contain a copy of the app and one of the coolest things I learned, and perhaps I'm a Docker noob, but you can run the following command to run those unit tests for the app straight from DockerHub! Kinda cool! `$ docker container run adammaus/run-angular18-karma-in-docker ng test`

I hope this helps get you off to a running start with unit testing a Angular app in a Docker container!
