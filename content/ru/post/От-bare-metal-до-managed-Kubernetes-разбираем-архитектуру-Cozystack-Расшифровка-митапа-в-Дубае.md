---
title: "От bare metal до managed Kubernetes: разбираем архитектуру Cozystack. Расшифровка митапа в Дубае"
date: 2026-10-04T01:01:27+00:00
link: https://habr.com/ru/companies/aenix/articles/1090064/?utm_campaign=1090064&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/d70/e87/e9d/d70e87e9d3f5f5b448f9b4e6164101e2.jpg)

Как устроен Cozystack и managed Kubernetes на собственном железе

Во время поездки в ОАЭ я случайно попал в [дубайское IT-комьюнити в Telegram](https://t.me/RussianDubaiIT). Там мы внезапно скоординировались и собрали незапланированный митап. 3 октября встретились в небольшой переговорке в Дубае — получилось душевно, и мы успели обсудить много интересных тем: от Talos и хранилища до сетей и устройства managed Kubernetes.

На митапе я рассказывал о Cozystack — открытой платформе для предоставления managed-сервисов на собственном железе. Начали с обзорной презентации, но довольно быстро перешли к вопросам: почему выбрали именно такой storage, зачем нам одновременно Kube-OVN и Cilium, как устроен Kubernetes внутри Kubernetes и где проходит граница между облачной платформой и обычной виртуализацией.

Ниже — отредактированная техническая расшифровка доклада и обсуждения. Я разберу, как связаны Talos, Flux, LINSTOR, Kube-OVN, Cilium, KubeVirt, Kamaji и Cluster API; как пользовательский ресурс превращается в работающий сервис; и почему для managed Kubernetes важно отдельно обслуживать control plane, вычислительные узлы и хранилище.
