---
title: "Жизненный цикл объекта в Kubernetes: путь от kubectl apply до полного удаления"
date: 2026-05-29T05:48:51+00:00
link: https://habr.com/ru/companies/aenix/articles/1040618/?utm_campaign=1040618&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/14a/4c9/fd2/14a4c9fd27a3d2561621184757911065.png)

Привет. В предыдущих статьях этого цикла мы разбирали, как Kubernetes-объекты **читаются** ([первая](https://habr.com/ru/companies/aenix/articles/1031818/) — informer и кэш в `controller-runtime`) и **записываются** ([вторая](https://habr.com/ru/companies/aenix/articles/1039282/) — Server-Side Apply, patch’и, `managedFields`). Сегодня — про их жизненный цикл.

Между `kubectl apply` и появлением объекта в etcd проходит целая цепочка: admission chain, мутирующие и валидирующие вебхуки, schema-валидация, встроенные плагины. Между `kubectl delete` и реальным исчезновением объекта может пройти от миллисекунд до часов — в зависимости от того, какие на нём финализаторы и какая стратегия каскадного удаления выбрана. Механизм при этом универсален для любого ресурса: Pod, Deployment, ваш CRD — жизненный цикл у всех один.

В этой статье я постараюсь ответить, что происходит с объектом от его рождения до смерти. И отдельно поговорим про другое измерение — эволюцию его API-схемы.
