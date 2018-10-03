---
title: Deploying LINSTOR storage for Proxmox
date: 2018-09-12 21:36:59
tags: en
link: https://medium.com/@kvapss/deploying-linstor-with-proxmox-91c746b4035d
---

![](https://cdn-images-1.medium.com/max/800/1*cnj3wxTbCBWX6N_GGbgroA.png)

Few time ago LINBIT released their new solution LINSTOR which is providing orchestration tool for manage multiple DRBD-arrays.

For example you can have few nodes, each one will have own LVM or ZFS pool, LINSTOR will automatically create new volumes there and replicate or distribute them using DRBD protocol.

LINSTOR supports thin-provisioning, snapshots and many other interesting things.

This solution is good suitable for virtual machines and containers.

<!--more-->
