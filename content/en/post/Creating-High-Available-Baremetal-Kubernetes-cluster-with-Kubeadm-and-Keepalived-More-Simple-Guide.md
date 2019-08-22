---
title: "Creating High Available Baremetal Kubernetes cluster with Kubeadm and Keepalived (More Simple Guide)"
date: 2018-12-09
link: https://medium.com/@kvaps/creating-high-available-baremetal-kubernetes-cluster-with-kubeadm-and-keepalived-simplest-guide-71766d5e25ae
---

This guide is updated version of my previous article [Creating High Available Baremetal Kubernetes cluster with Kubeadm and Keepalived (Simple Guide)](https://medium.com/@kvapss/creating-baremethal-kubernetes-ha-cluster-with-kubeadm-and-keepalived-simple-guide-c70ec4adf8ca)
Since **v1.13** deployment has become much easier and more logical. Note that this article is my personal interpretation of official Creating Highly [Available Clusters with kubeadm](https://kubernetes.io/docs/setup/independent/high-availability/) for [Stacked control plane nodes](https://kubernetes.io/docs/setup/independent/high-availability/#stacked-control-plane-nodes) plus few more steps for Keepalived.

If you have any questions, or something is not clear, please refer to the official documentation or ask the [Google](https://www.google.com/). All steps described here in the short and simple form

<!--more-->
