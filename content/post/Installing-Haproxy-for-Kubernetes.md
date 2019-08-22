---
title: "Installing Haproxy for Kubernetes"
date: 2019-04-30
link: https://medium.com/@kvaps/for-make-this-scheme-more-safe-you-can-add-haproxy-layer-between-keepalived-and-kube-apiservers-62c344283076
---

![](https://miro.medium.com/max/619/1*HPqRvvMlCyxydro6ezCpow.jpeg)

If you want to make this scheme more safe you can add haproxy layer between keepalived and kube-apiserver.

Just install haproxy package into your system, and add the next configuration into `/etc/haproxy/haproxy.cfg` file

<!--more-->
