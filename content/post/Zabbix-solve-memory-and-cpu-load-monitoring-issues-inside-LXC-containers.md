---
title: 'Zabbix: solve memory and cpu load monitoring issues inside LXC containers'
date: 2017-11-29 12:53:18
link: https://medium.com/@kvapss/zabbix-solve-memory-monitoring-issue-inside-lxc-containers-98ddf191051c
---

Zabbix have some problems with memory collecting from cgroups limited containers.
If you using Promxox, you know what I mean: The available memory collected worng without calculating buffers and cache memory.
Zabbix have [bug report](https://medium.com/r/?url=https%3A%2F%2Fsupport.zabbix.com%2Fbrowse%2FZBX-12164), but it seems that no one don’t want to fix it soon.
So let’s fix it together byself.
<!-- more -->
