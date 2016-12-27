---
title: We build an own fault-tolerant cloud based on OpenNebula with Ceph, MariaDB Galera Cluster and OpenvSwitch [Translation]
date: 2015-11-16 16:45:00
tags: 
    - en
    - translation
link: http://developers-club.com/posts/270187/
index: false
---

![](https://habrastorage.org/files/1b8/185/6c4/1b81856c42da42ba903e85e1653969e4.png)
This time I would like to tell how to configure this subject, in a particular each separate component as a result to receive the own, expanded, otkazoustoycheavy cloud based on OpenNebula. In this article I will consider the next moments:

*    **[The Ceph installation, the distributed storage](http://habrahabr.ru/post/270187/#ceph)**. _(I will describe installation of two-level storage with the caching pool from SSD disks)_
*    **[The installation MySQL, Galera of a cluster with the master master replication](http://habrahabr.ru/post/270187/#galera)**
*    **[Installation software switch of OpenvSwitch](http://habrahabr.ru/post/270187/#openvswitch)**
*    **[Installation directly OpenNebula](http://habrahabr.ru/post/270187/#opennebula)**
*    **[Setup of failover cluster](http://habrahabr.ru/post/270187/#pacemaker)**
*    **[Initial configuration](http://habrahabr.ru/post/270187/#configuration)**


Subjects in itself very interesting so even if you are not interested in an ultimate goal, but setup of some separate component interests. I ask favor under cut.
<!-- more -->
