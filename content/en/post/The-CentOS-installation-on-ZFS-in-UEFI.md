---
title: Installing CentOS on ZFS in UEFI [machine translation]
date: 2015-10-13 15:37:00
link: https://weekly-geekly.github.io/articles/268711/index.html
---

![](https://habrastorage.org/files/fcc/619/ae4/fcc619ae4bb7418980f542ed02978583.png)


I decided to try ZFS here the other day, but I did not find a detailed and simple manual on how to implement it on CentOS, I decided to correct the situation. In addition, I wanted to install all this in EFI mode. - not to stand still? And at the same time understand for yourself how [DKMS](https://ru.wikipedia.org/wiki/Dynamic_Kernel_Module_Support) works, as well as aspects of manual installation of RPM-based distributions.
ZFS was not chosen by chance either, since it was planned to deploy a hypervisor on this machine and use zvol to store images of virtual machines. I wanted something more than a software raid + lvm or simple file storage of images, something like [ceph](https://ru.wikipedia.org/wiki/Ceph_File_System), but for one host this is too bold. Looking ahead to say that I was very pleased with this file system, its performance and all its [chips](http://xgu.ru/wiki/ZFS).

<!--more-->
