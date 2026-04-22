---
title: "Flux-aio, Kubernetes mTLS и проблема курицы и яйца"
date: 2025-12-10T11:24:57+00:00
link: https://habr.com/ru/companies/aenix/articles/975324/?utm_campaign=975324&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/40d/d67/b1a/40dd67b1aed6b3241312503f31be2a0c.png)

Мы тут в Cozystack в очередной раз решаем проблему курицы и яйца: как задеплоить CNI и kube-proxy через Flux, но при этом обеспечить работу самого flux без CNI и kube-proxy.

Сам Flux запустить без CNI и kube-proxy можно используя проект flux-aio (от создателя Flux), который запускает единый deployment со всеми контроллерами настроенными на коммуникацию друг с другом через localhost.

Специфика Cozystack заключается в том, что на каждый кластер мы деплоим внутри небольшой HTTP-сервер с Helm-чартами и другими ассетами используемыми в платформе. Flux эти чарты читает и устанавливает в систему.

Но вот как организовать доступ флюксу к внутреннему HTTP-серверу, запущенному как под внутри того же кластера?

 [Читать далее](https://habr.com/ru/articles/975324/?utm_campaign=975324&utm_source=habrahabr&utm_medium=rss#habracut)

[Читать на Хабре →](https://habr.com/ru/companies/aenix/articles/975324/?utm_campaign=975324&utm_source=habrahabr&utm_medium=rss)
