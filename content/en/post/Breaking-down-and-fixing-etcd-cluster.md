---
title: "Breaking down and fixing etcd cluster"
date: 2021-03-05T14:05:00+01:00
link: https://itnext.io/breaking-down-and-fixing-etcd-cluster-d81e35b9260d
---

![](https://miro.medium.com/max/2400/0*zp50MnKH708J9vYm.png)

**etcd** is a fast, reliable and fault-tolerant key-value database. It is at the heart of Kubernetes and is an integral part of its control-plane. It is quite important to have the experience to back up and restore the operability of both individual nodes and the whole entire etcd cluster.

In the [previous article](https://itnext.io/breaking-down-and-fixing-kubernetes-4df2f22f87c3), we looked in detail at regenerating SSL-certificates and static-manifests for Kubernetes, as well as issues related to restoring the operability of its control-plane. This article will be fully devoted to restoring an etcd-cluster.

<!--more-->
