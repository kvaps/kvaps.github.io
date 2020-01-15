---
title: Trying new tools for building and automating the deployment in Kubernetes
date: 2020-01-15
link: https://medium.com/@kvaps/trying-new-tools-for-building-and-automate-the-deployment-in-kubernetes-f96f9684e58 
---

![](https://miro.medium.com/max/3882/0*HJu_pzhe660WFJZ2)

Hi!  
Recently, many cool automation tools have been released both for building Docker images and for deploying to Kubernetes. In this regard, I decided to play with the Gitlab a little, study its capabilities and, of course, configure the pipeline.

The source of inspiration for this work was the site [kubernetes.io](https://kubernetes.io/), which is automatically generated from [source code](github.com/kubernetes/website).  
For each new pullrequest the bot generates a preview version with your changes automatically and provides a link for review.

I tried to build a similar process from scratch, but entirely built on Gitlab CI and free tools that I used to use to deploy applications in Kubernetes. Today, I finally will tell you more about them.

The article will consider such tools as: **Hugo**, **qbec**, **kaniko**, **git-crypt** and **GitLab CI** with dynamic environments feature.

<!--more-->
