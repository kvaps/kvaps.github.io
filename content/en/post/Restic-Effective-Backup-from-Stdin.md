---
title: 'Restic: Effective Backup from Stdin'
date: 2023-12-25
link: https://itnext.io/restic-effective-backup-from-stdin-4bc1e8f083c1
---

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*uJ7As9uTvB-gvQLe.png)

I’ve previously discussed Restic in the article “[Backup storage for thousands of virtual machines using free tools](https://itnext.io/backup-storage-for-thousands-of-virtual-machines-using-free-tools-b3909004bef2),” and it remains my favorite backup tool since then.

Today, I will describe a ready-made recipe for setting up effective backup from Stdin, with deduplication and automatic cleaning of the repository from old copies.

Despite Restic being great for saving entire data directories, this article emphasizes on-the-fly backup from Stdin, typically for virtual machine backups, databases, and other large-file data that can be sequentially read and immediately sent to the backup system.

<!--more-->
