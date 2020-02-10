---
title: Build your own failover cloud based on OpenNebula with Ceph, MariaDB Galera Cluster and OpenvSwitch [machine translation]
date: 2015-11-16 16:45:00
link: https://weekly-geekly.github.io/articles/270187/index.html
---

![](https://habrastorage.org/files/1b8/185/6c4/1b81856c42da42ba903e85e1653969e4.png)
This time I would like to tell how to configure this subject, in a particular each separate component as a result to receive the own, expanded, otkazoustoycheavy cloud based on OpenNebula. In this article I will consider the next moments:

*    **[Install Ceph, distributed storage](https://weekly-geekly.github.io/articles/270187/index.html#ceph)**. _(I will describe the installation of a two-tier storage with a caching pool of SSDs)_
*    **[Install MySQL, Galera Cluster with master replication](https://weekly-geekly.github.io/articles/270187/index.html#galera)**
*    **[Installing OpenvSwitch soft switch](https://weekly-geekly.github.io/articles/270187/index.html#openvswitch)**
*    **[Installing directly OpenNebula itself](https://weekly-geekly.github.io/articles/270187/index.html#opennebula)**
*    **[Configuring Failover Cluster](https://weekly-geekly.github.io/articles/270187/index.html#pacemaker)**
*    **[Initial configuration](https://weekly-geekly.github.io/articles/270187/index.html#configuration)**

The topics themselves are very interesting, so even if you are not interested in the final goal, but you are interested in setting up a separate component. You are welcome under the cut. 
<!--more-->
