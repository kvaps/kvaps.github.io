---
title: "Treating Kubernetes as a Linux Distro APT Style Packaging with FluxCD   Andrei Kvapil"
date: 2026-06-05T17:09:12+00:00
link: https://www.youtube.com/watch?v=E3H9GZAJKMI
source: youtube-en
---

{{< youtube E3H9GZAJKMI >}}

Kubernetes platforms face the same challenge Linux solved decades ago: how to let users install only what they need and build community-driven package ecosystems.

In Cozystack, we built an APT-like package system on FluxCD and OCI artifacts. The operator introduces Package and PackageSource CRDs - analogous to dpkg and sources.list - with pluggable repositories, dependency resolution, and content-based versioning.

We'll cover how we solved the chicken-and-egg problem (deploying CNI via Flux when Flux needs networking), evolving from HTTP hacks to a clean solution with flux-aio and FluxCD's source-watcher pattern using OCI artifacts directly.

Takeaways:
- Designing Kubernetes-native package management inspired by APT
- Using FluxCD source-watcher and OCI artifacts in practice
- Enabling pluggable repositories for Kubernetes platforms
- Building extensible platforms where users can fork and contribute packages
