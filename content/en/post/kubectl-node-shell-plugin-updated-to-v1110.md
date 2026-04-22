---
title: "kubectl-node-shell plugin updated to v1.11.0"
date: 2024-12-02T10:35:35+00:00
link: https://blog.aenix.io/kubectl-node-shell-plugin-updated-to-v1-11-0-3c3bb0a77f25?source=rss-d8a829bb74d8------2
source: medium
---

We have updated the kubectl-node-shell plugin to [v1.11.0](https://github.com/kvaps/kubectl-node-shell/releases/tag/v1.11.0).

- Added options: no-mount, -- no-net, -- no-ipc,--no-uts to disable automatic entry into the specified Linux namespaces.
- Added variable: KUBECTL_NODE_SHELL_IMAGE_PULL_SECRET_NAME to specify a pullSecret for pulling the image.
- Added ability to attach volumes using the -m option; attached volumes can be found in the /opt-pvc directory.

[Read on Medium →](https://blog.aenix.io/kubectl-node-shell-plugin-updated-to-v1-11-0-3c3bb0a77f25?source=rss-d8a829bb74d8------2)
