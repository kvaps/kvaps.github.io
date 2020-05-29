---
title: "Configuring routing for MetalLB in L2 mode"
date: 2020-05-14 22:05:09
link: https://itnext.io/configuring-routing-for-metallb-in-l2-mode-7ea26e19219e
---

![](https://miro.medium.com/max/1400/0*wI1GLh4MrCzuwiwB.png)

Not so far ago, I was faced with a quite unusual task of configuring routing for MetalLB. All would be nothing, since MetalLB usually does not require any additional configuration from user side, but in our case there is a fairly large cluster with a quite simple network configuration.

In this article I will show you how to configure source-based and policy-based routing for the external network on your cluster.

I will not dwell on installing and configuring MetalLB in detail, as I assume you already have some experience. Let’s understand the essence and configure the routing. So we have four cases:

<!--more-->
