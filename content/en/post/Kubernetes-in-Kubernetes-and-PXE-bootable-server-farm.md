---
title: "Kubernetes-in-Kubernetes and the WEDOS PXE bootable server farm"
date: 2021-12-22
link: https://kubernetes.io/blog/2021/12/22/kubernetes-in-kubernetes-and-pxe-bootable-server-farm/
---

[![Kubernetes-in-Kubernetes - We need to go deeper](https://pbs.twimg.com/media/FHMnruzWYAAT_xv?format=png)](https://kubernetes.io/blog/2021/12/22/kubernetes-in-kubernetes-and-pxe-bootable-server-farm/)

When you own two data centers, thousands of physical servers, virtual machines and hosting for hundreds of thousands sites, Kubernetes can actually simplify the management of all these things. As practice has shown, by using Kubernetes, you can declaratively describe and manage not only applications, but also the infrastructure itself. I work for the largest Czech hosting provider **WEDOS Internet a.s** and today I'll show you two of my projects — [Kubernetes-in-Kubernetes](https://github.com/kvaps/kubernetes-in-kubernetes) and [Kubefarm](https://github.com/kvaps/kubefarm).

With their help you can deploy a fully working Kubernetes cluster inside another Kubernetes using Helm in just a couple of commands. How and why?

<!--more-->
