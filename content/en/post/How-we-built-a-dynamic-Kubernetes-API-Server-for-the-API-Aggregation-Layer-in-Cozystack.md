---
title: "How we built a dynamic Kubernetes API Server for the API Aggregation Layer in Cozystack"
date: 2024-12-12T12:42:37+00:00
link: https://blog.aenix.io/how-we-built-a-dynamic-kubernetes-api-server-for-the-api-aggregation-layer-in-cozystack-15709a183c86?source=rss-d8a829bb74d8------2
source: medium
---

![](https://cdn-images-1.medium.com/max/1024/1*UnLXn4UMrp8BzIliKvmIPA.png)

Hi there! I’m Andrei Kvapil, but you might know me as [@kvaps](https://github.com/kvaps) in communities dedicated to Kubernetes and cloud-native tools. In this article, I want to share how we implemented our own extension api-server in the open-source PaaS platform, Cozystack.

Kubernetes truly amazes me with its powerful extensibility features. You’re probably already familiar with the [controller](https://kubernetes.io/docs/concepts/architecture/controller/) concept and frameworks like [kubebuilder](https://book.kubebuilder.io/) and [operator-sdk](https://sdk.operatorframework.io/) that help you implement it. In a nutshell, they allow you to extend your Kubernetes cluster by defining custom resources (CRDs) and writing additional controllers that handle your business logic for reconciling and managing these kinds of resources. This approach is well-documented, with a wealth of information available online on how to develop your own operators.
