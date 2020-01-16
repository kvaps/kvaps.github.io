---
title: How to describe 100 Gitlab jobs in 100 lines using Jsonnet
date: 2020-01-16
link: https://medium.com/@kvaps/how-to-describe-100-gitlab-jobs-in-100-lines-using-jsonnet-4e19a4d5bca
---

In addition to the [previous article](https://medium.com/@kvaps/trying-new-tools-for-building-and-automate-the-deployment-in-kubernetes-f96f9684e58) about deployment tools in Kubernetes, I want to tell you about how you can use Jsonnet to simplify the description of the jobs in your **.gitlab-ci.yml**

![](https://miro.medium.com/max/350/1*fVzTtRqdqlthR-kEGqbxLw.png)

## Given

There is a monorepo in which:

- 10 dockerfiles
- 30 described deployments
- 3 environments: devel, stage and prod

## Task

Configure a pipeline:

- Building Docker images should be done by adding a git tag with a version number.
- Each deployment operation should be performed when pushing to the environment branch and only if files changed in a specific directory
- Each environment has its own gitlab-runner with a different tag that performs deployment only in this environment.
- Not any application should be deployed in each of the environments. We should describe the pipeline in order to be able to make exceptions.
- Some deployments use git submodule and should be run with the `GIT_SUBMODULE_STRATEGY=normal` environment variable set.

Describing all this may seem like a real hell, but do not despair, armed with Jsonnet, we can easily do it.

<!--more-->
