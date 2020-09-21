---
title: "Tuning CNI plugins for having better performance and advanced features"
date: 2020-09-12
link: https://medium.com/@kvaps/tuning-cni-plugins-for-having-better-performance-and-advanced-features-a6c796d9fbf1
---

![](https://miro.medium.com/max/700/1*542zIrU1saV6nxdyQFnStA.png)

Thanks for the [benchmarks](https://itnext.io/benchmark-results-of-kubernetes-network-plugins-cni-over-10gbit-s-network-updated-august-2020-6e1b757b9e49) Alexis!

Most plugins have non-optimized defaults that work in most common situations, regardless of network topology, OS and kernel version.

I have an experience of tuning some of them, and I would like to share it with you, just briefly:

<!--more-->
