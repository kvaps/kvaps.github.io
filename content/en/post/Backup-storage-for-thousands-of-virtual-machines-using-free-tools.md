---
title: "Backup storage for thousands of virtual machines using free tools"
date: 2020-05-29 20:06:10
link: https://itnext.io/backup-storage-for-thousands-of-virtual-machines-using-free-tools-b3909004bef2
---

![](https://miro.medium.com/max/1400/0*A6SRoMPAkAf-RnRB.png)

Hi, recently I faced across an interesting task to setup a storage server for backup of a large number of block devices.

Every week we back up all virtual machines in our cloud, so there is a need to be able handle thousands of backups and do it as fast and efficiently as possible.

Unfortunately, the standard RAID5, RAID6 levels are not suitable due the fact that recovery process on such large disks as ours will be painfully long and most likely never finished successfully.

Let’s consider what alternatives are:

**[Erasure Coding](https://docs.min.io/docs/minio-erasure-code-quickstart-guide.html)** — An analogue to RAID5, RAID6, but with a configurable parity level. Also the fault tolerance is performed not for whole block devices, but for each object separately. The easiest way to try Erasure Coding is to deploy [minio](https://min.io/).

**[DRAID](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/dRAID%20Howto.html)** — is currently alpha feature of ZFS. Unlike RAIDZ, DRAID has a distributed parity block and uses all the disks in the array during recovery, this makes it better surviving for disk failures and provides faster recovery than standard RAID levels.

<!--more-->
