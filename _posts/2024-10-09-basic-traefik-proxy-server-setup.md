---
layout: post
permalink: "2024/10/basic-traefik-proxy-server-setup/"
title: "Basic Traefik proxy server setup"
date: 2024-10-09T08:22:24-05:00
excerpt: Recently, I came across a tool called Traefik. Traefik is a tool that takes care of routing HTTP requests to different Docker containers running on a server. This let's you focus more on your containers and projects and less on server maintenance.
tags:
  - CI/CD
  - Docker
  - LetsEncrypt
  - Traefik
---
Recently, I came across a tool called [Traefik](https://traefik.io/traefik/). Traefik is a tool that takes care of routing HTTP requests to different Docker containers running on a server. This let's you focus more on your containers and projects and less on server maintenance.

The basic setup I had in mind was to have two domains living on a single server powered by Docker containers running my code. A real world example might be running a Single Page Application website as well as the backend API. I also wanted to make sure that LetsEncrypt certificates were enabled out of the box.

I won't waste your time by going over the entire setup process since it is described in this [Github repo](https://github.com/adammaus/basic-traefik-setup) but the repo will provide the scripts and instructions for a very basic server setup with two domains running in two different Docker containers.

After going through the server provisioning and setup process, you should see something like this:

__Domain 1: Codenamed Alice__

![Image of Alice's Website](/assets/posts/2024-10-09-basic-traefik-proxy-server-setup/image-1.png)

__Domain 2: Codenamed Bob__

![Image of Bob's Website](/assets/posts/2024-10-09-basic-traefik-proxy-server-setup/image-2.png)

I will say that I was pleasantly surprised by how easy it was to set up. The server running Traefik and Docker is extremely light, as you can see in [provision-script.sh](https://github.com/adammaus/basic-traefik-setup/blob/main/provision-script.sh). This means server updates should be minimal and we could easily tear down and spin up a new server as needed. I hope you find the [instructions](https://github.com/adammaus/basic-traefik-setup) helpful!