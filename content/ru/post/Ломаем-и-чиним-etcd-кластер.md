---
title: "Ломаем и чиним etcd-кластер"
date: 2021-03-01T17:05:49+00:00
link: https://habr.com/ru/companies/aenix/articles/544390/?utm_campaign=544390&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/d45/e1a/ef8/d45e1aef8efcc248023c53caaaba9a34.jpg)

**etcd** — это быстрая, надёжная и устойчивая к сбоям key-value база данных. Она лежит в основе Kubernetes и является неотъемлемой частью control-plane, именно поэтому критически важно уметь бэкапить и восстанавливать работоспособность как отдельных нод, так и всего etcd-кластера.

В [предыдущей статье](https://habr.com/ru/post/541118/) мы подробно рассмотрели перегенерацию SSL-сертификатов и static-манифестов для Kubernetes, а также вопросы связанные c восстановлением работоспособности Kubernetes-кластера. Эта статья будет посвящена целиком и полностью восстановлению etcd.

 [Поехали!   ┬─┬ ノ( ゜-゜ノ)](https://habr.com/ru/articles/544390/?utm_campaign=544390&utm_source=habrahabr&utm_medium=rss#habracut)

<!--more-->
