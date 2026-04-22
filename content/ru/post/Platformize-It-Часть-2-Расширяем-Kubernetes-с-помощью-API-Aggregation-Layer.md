---
title: "Platformize It! Часть 2: Расширяем Kubernetes с помощью API Aggregation Layer"
date: 2026-02-26T12:04:58+00:00
link: https://habr.com/ru/companies/aenix/articles/1004014/?utm_campaign=1004014&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/011/f25/b58/011f25b58ad180f472700718c07da0aa.jpg)

В [предыдущей части](https://habr.com/ru/users/kvaps/articles/) статьи мы разобрались, как построить платформу для развертывания управляемых приложений с единым API и UI. Сегодня мы сделаем следующий шаг — дополним стандартный API Kubernetes своим API-сервером для синхронизации состояния. Рассказываем по порядку, это сделать.
