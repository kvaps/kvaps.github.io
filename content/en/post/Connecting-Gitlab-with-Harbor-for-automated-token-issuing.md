---
title: Connecting Gitlab with Harbor for automated token issuing
date: 2020-04-24 23:00:00
link: https://medium.com/@kvaps/connecting-gitlab-with-harbor-for-automated-token-issuing-6446f58269a7
---

![](https://miro.medium.com/max/1400/1*rp7sSltmrBJ0lyHCenfmrw.png)

Gitlab CI have a nice feature to generate docker-registry tokens per each job, but this feature is working only for it’s own docker registry and does not working with an external ones, eg. Harbor, Nexus, Quay and etc.

There is an opportunity to set-up external docker registry for Gitlab, it is well described in the documentation [Use an external container registry with GitLab as an auth endpoint](https://docs.gitlab.com/ee/administration/packages/container_registry.html#use-an-external-container-registry-with-gitlab-as-an-auth-endpoint).

Proposed to configure brand new docker-registry with token based authentication. Harbor also uses docker-registry in backend, so that we could configure it, but problem is that both Gitlab and Harbor require to set their own parameters which are actually conflicts.

<!--more-->
