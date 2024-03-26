---
title: 'DIY: Ваше собственное облако на базе Kubernetes (часть 3)'
date: 2024-03-11
link: https://habr.com/ru/companies/aenix/articles/798567/
---

![](https://habrastorage.org/r/w780/getpro/habr/upload_files/fb7/364/f79/fb7364f79d054dee643232f5cec7f26f.jpg)

Вот мы и подобрались к самому интересному: запуску Kubernetes в Kubernetes. В этой статье мы поговорим о таких технологиях, как Kamaji и Cluster API, а также о том, как интегрировать их с KubeVirt.

В прошлых статьях мы уже рассказывали, [как мы готовим Kubernetes на bare metal](https://habr.com/ru/companies/aenix/articles/795791/), и о том, [как превратить Kubernetes в средство запуска виртуальных машин](https://habr.com/ru/companies/aenix/articles/797323/). Эта статья завершает серию, объясняя, как, используя всё вышеперечисленное, можно построить полноценный managed Kubernetes service и запускать виртуальные Kubernetes-кластеры по клику.

И начнём мы, пожалуй с Cluster API.

<!--more-->
