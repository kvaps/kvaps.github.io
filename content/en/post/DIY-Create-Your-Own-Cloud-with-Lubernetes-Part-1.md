---
title: "DIY: Create Your Own Cloud with Kubernetes (Part 1)"
slug: diy-create-your-own-cloud-with-kubernetes-part-1
date: 2024-04-05T07:30:00+00:00
link: https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-1/
---

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/0*29CNNfqCIVq4Uqfa.jpg)

At Ænix, we have a deep affection for Kubernetes and dream that all modern technologies will soon
start utilizing its remarkable patterns.

Have you ever thought about building your own cloud? I bet you have. But is it possible to do this
using only modern technologies and approaches, without leaving the cozy Kubernetes ecosystem?
Our experience in developing Cozystack required us to delve deeply into it.

You might argue that Kubernetes is not intended for this purpose and why not simply use OpenStack
for bare metal servers and run Kubernetes inside it as intended. But by doing so, you would simply
  shift the responsibility from your hands to the hands of OpenStack administrators.
  This would add at least one more huge and complex system to your ecosystem.

Why complicate things? - after all, Kubernetes already has everything needed to run tenant
Kubernetes clusters at this point.

<!--more-->
