---
title: "Comparing Ceph, LINSTOR, Mayastor, and Vitastor storage performance in Kubernetes"
date: 2022-06-03
link: https://blog.palark.com/kubernetes-storage-performance-linstor-ceph-mayastor-vitastor/
---

![](https://blog.palark.com/wp-content/uploads/2022/06/performance_study_of_linstor_ceph_mayastor_and_vitastor_free_storage_preview.png)

There seems to be a new trend: every time I get a new job, the first activity I engage in is benchmarking different SDS solutions. My career at Flant is no exception. I joined the development team for the [Deckhouse Kubernetes platform](https://deckhouse.io/) when it decided to focus on running virtual machines in Kubernetes. But first, we had to find an easy-to-use, reliable block-type storage that we could offer to the platform’s customers.

Hence I decided to benchmark several Open Source solutions to see how they behave under various conditions. The focal point was the [DRBD](https://en.wikipedia.org/wiki/Distributed_Replicated_Block_Device) performance in different configurations and how they compared to [Ceph](https://ceph.io/en/).

However, the market for software-defined storage is constantly growing and evolving. Ambitious new projects are emerging, including the recently released [Mayastor](https://github.com/openebs/mayastor) and my fellow collaborator’s pet project [Vitastor](https://vitastor.io/). The results were pretty exciting and surprising.

<!--more-->
