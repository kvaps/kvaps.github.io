---
title: "kubectl-node-shell plugin updated to v1.11.0"
date: 2024-12-02T10:35:35+00:00
link: https://blog.aenix.io/kubectl-node-shell-plugin-updated-to-v1-11-0-3c3bb0a77f25?source=rss-d8a829bb74d8------2
source: medium
---

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=3c3bb0a77f25)

We have updated the kubectl-node-shell plugin to [v1.11.0](https://github.com/kvaps/kubectl-node-shell/releases/tag/v1.11.0).

The kubectl-node-shell plugin allows you to log into a node in a cluster without SSH, using only the Kubernetes API. This is convenient for debugging any managed Kubernetes cluster. For example, AWS does not provide SSH access to nodes when using managed K8s.

- Added options: no-mount, -- no-net, -- no-ipc,--no-uts to disable automatic entry into the specified Linux namespaces.
- Added variable: KUBECTL_NODE_SHELL_IMAGE_PULL_SECRET_NAME to specify a pullSecret for pulling the image.
- Added ability to attach volumes using the -m option; attached volumes can be found in the /opt-pvc directory.

*Many thanks to *[jmcshane](https://github.com/jmcshane)*, *[huandu](https://github.com/huandu)*, and bernardgut who added these wonderful features to the new version of the plugin.*

[kubectl-node-shell plugin updated to v1.11.0](https://blog.aenix.io/kubectl-node-shell-plugin-updated-to-v1-11-0-3c3bb0a77f25) was originally published in [Ænix](https://blog.aenix.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

<!--more-->
