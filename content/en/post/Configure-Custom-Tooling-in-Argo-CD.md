---
title: "Configure Custom Tooling in Argo CD"
date: 2020-09-06T01:04:00+03:00
link: https://itnext.io/configure-custom-tooling-in-argo-cd-a4948d95626e
---

![](https://miro.medium.com/max/700/0*tcU-h452sfjDT96C.png)


Some time after writing the [first article](https://itnext.io/trying-new-tools-for-building-and-automate-the-deployment-in-kubernetes-f96f9684e580), where I cleverly use jsonnet and gitlab, I realized that pipelines are certainly good, but unnecessarily difficult and inconvenient.

In most cases, a typical task is need: “to generate YAML and put it in Kubernetes”. Actually, this is what the Argo CD does really well.

Argo CD allows you to connect a Git repository and sync its state to Kubernetes. By default several types of applications are supported: Kustomize, Helm charts, Ksonnet, raw Jsonnet or simple directories with YAML/JSON manifests.

Most users will be happy for having just this tool set, but not everyone. In order to satisfy the needs of anyone, Argo CD has the ability to use custom tooling.

First of all, I was interested in the opportunity to add support for [qbec](https://itnext.io/trying-new-tools-for-building-and-automate-the-deployment-in-kubernetes-f96f9684e580#4c4b) and [git-crypt](https://itnext.io/trying-new-tools-for-building-and-automate-the-deployment-in-kubernetes-f96f9684e580#29ed), which were fully discussed in the previous article.

<!--more-->
