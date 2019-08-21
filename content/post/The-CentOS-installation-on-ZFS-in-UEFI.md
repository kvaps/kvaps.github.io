---
title: The CentOS installation on ZFS in UEFI [Translation]
date: 2015-10-13 15:37:00
link: http://developers-club.com/posts/268711/
index: false
---

![](https://habrastorage.org/files/fcc/619/ae4/fcc619ae4bb7418980f542ed02978583.png)

Has decided to try here the other day ZFS, and detailed and simple manual as to carry out it on CentOS has not found, has decided to correct situation. Besides there was a wish to set all this in the EFI mode. — not to stand still? And at the same time to understand for itself as DKMS, and also aspects of the manual RPM-based installation of distribution kits works.

ZFS has been selected too not accidentally as by this machine it was going to unroll hypervisor and to use zvol for storage of images of virtual computers. I wanted something bigger than program raid + lvm or simple file storage of images, something on similarity of ceph, but for one host it is too bold. Running forward I will tell that I was very pleased with this file system, its productivity and all its [counters](http://xgu.ru/wiki/ZFS#.D0.A2.D0.B5.D1.85.D0.BD.D0.B8.D1.87.D0.B5.D1.81.D0.BA.D0.B8.D0.B5_.D0.B2.D0.BE.D0.B7.D0.BC.D0.BE.D0.B6.D0.BD.D0.BE.D1.81.D1.82.D0.B8_ZFS).
<!-- more -->
