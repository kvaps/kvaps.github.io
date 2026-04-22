---
title: "Cozypkg: как мы упростили локальную разработку с Helm + Flux"
date: 2025-06-18T17:41:10+00:00
link: https://habr.com/ru/companies/aenix/articles/918990/?utm_campaign=918990&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/1b2/6bd/2a8/1b26bd2a8ec9befd63bcf4f8eccaa42b.png)

Привет! Я Андрей Квапил (или kvaps) и в этой статье я опишу наш путь организации доставки приложений в Kubernetes, объясню недостатки классического GitOps в локальной разработке и покажу, как новая утилита [cozypkg](https://github.com/cozystack/cozypkg) решает эти проблемы. Материал рассчитан на разработчиков, знакомых с Helm и Flux.

У нас есть общий репозиторий — в нем мы описываем общую конфигурацию всех компонентов, а также темплейты для их деплоя. Для того чтобы максимально упростить процесс поддержки каждого из компонентов, мы следуем определенному процессу.В основе этого процесса лежит идея о том, что каждый компонент — это Helm-чарт**. **

 [Читать далее](https://habr.com/ru/articles/918990/?utm_campaign=918990&utm_source=habrahabr&utm_medium=rss#habracut)

<!--more-->
