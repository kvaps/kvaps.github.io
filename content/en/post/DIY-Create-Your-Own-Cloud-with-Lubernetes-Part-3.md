---
title: "DIY: Create Your Own Cloud with Kubernetes (Part 3)"
slug: diy-create-your-own-cloud-with-kubernetes-part-3
date: 2024-04-05T07:40:00+00:00
link: https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-3/
---

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/0*0Iy0cbjm5zwVxNGW.jpg)

Approaching the most interesting phase, this article delves into running Kubernetes within
Kubernetes. Technologies such as Kamaji and Cluster API are highlighted, along with their
integration with KubeVirt.

Previous discussions have covered
[preparing Kubernetes on bare metal](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-1/)
and
[how to turn Kubernetes into virtual machines management system](https://kubernetes.io/blog/2024/04/05/diy-create-your-own-cloud-with-kubernetes-part-2/).
This article concludes the series by explaining how, using all of the above, you can build a
full-fledged managed Kubernetes and run virtual Kubernetes clusters with just a click.

First up, let's dive into the Cluster API.

<!--more-->
