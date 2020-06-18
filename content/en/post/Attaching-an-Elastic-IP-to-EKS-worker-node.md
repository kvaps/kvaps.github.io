---
title: "Attaching an Elastic IP to EKS worker node"
date: 2020-06-04 16:12:27
link: https://itnext.io/attaching-an-elastic-ip-to-eks-worker-node-f69b9d8fa521
---

![](https://miro.medium.com/max/1020/1*ip6KYgXR1Z_lM07mb6cOGg.png)

Hi, I also faced with an interesting task to run STUN server in Kubernetes.

STUN Server requires passtrough whole 1024-65535 udp port range, however Kubernetes [has no support for specifying port ranges in services](https://github.com/kubernetes/kubernetes/issues/23864). The solution would seem simple to run pod with hostNetwork: true and assign it to separate EC2 instance with Elastic IP.

The problem is that EKS does not allow you to create separate instances, but instead directs you to use Auto Scaling Groups. Thus you have no opportunity to assign Elastic IP to specific EKS worker statically, but you can do that dynamically

<!--more-->
