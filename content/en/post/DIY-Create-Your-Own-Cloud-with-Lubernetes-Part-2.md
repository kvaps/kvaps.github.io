---
title: "DIY: Create Your Own Cloud with Kubernetes (Part 2)"
slug: diy-create-your-own-cloud-with-kubernetes-part-2
date: 2024-04-05T07:35:00+00:00
link: https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-2/
---

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/0*sIWfm_FgDavwJgK8.jpg)

Continuing our series of posts on how to build your own cloud using just the Kubernetes ecosystem.
In the [previous article](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-1/), we
explained how we prepare a basic Kubernetes distribution based on Talos Linux and Flux CD.
In this article, we'll show you a few various virtualization technologies in Kubernetes and prepare
everything need to run virtual machines in Kubernetes, primarily storage and networking.

We will talk about technologies such as KubeVirt, LINSTOR, and Kube-OVN.

But first, let's explain what virtual machines are needed for, and why can't you just use docker
containers for building cloud?
The reason is that containers do not provide a sufficient level of isolation.
Although the situation improves year by year, we often encounter vulnerabilities that allow
escaping the container sandbox and elevating privileges in the system.

<!--more-->
