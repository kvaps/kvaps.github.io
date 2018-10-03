---
title: Building a Network Bootable Server Farm for Kubernetes with LTSP
date: 2018-10-02 21:35:07
tags: en
link: https://kubernetes.io/blog/2018/10/02/building-a-network-bootable-server-farm-for-kubernetes-with-ltsp/
---

![](https://kubernetes.io/images/blog/2018-10-01-network-bootable-farm-with-ltsp/k8s+ltsp.svg)

In this post, I’m going to introduce you to a cool technology for Kubernetes, LTSP. It is useful for large baremetal Kubernetes deployments.

You don’t need to think about installing an OS and binaries on each node anymore. Why? You can do that automatically through Dockerfile!

You can buy and put 100 new servers into a production environment and get them working immediately - it’s really amazing!

Intrigued? Let me walk you through how it works.

<!--more-->
