---
title: "Тонкая настройка маршрутизации для MetalLB в режиме L2"
date: 2020-05-13T23:29:17+00:00
link: https://habr.com/ru/companies/aenix/articles/501842/?utm_campaign=501842&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/webt/og/nl/oo/ognloookahnkbs3mwjjdogbuhq4.png)

Не так давно я столкнулся с весьма нестандартной задачей настройки маршрутищации для MetalLB. Всё бы ничего, т.к. обычно для MetalLB не требуется никаких дополнительных действий, но в нашем случае имеется достаточно большой кластер с весьма нехитрой конфигурацией сети.

В данной статье я расскажу как настроить source-based и policy-based routing для внешней сети вашего кластера.

Я не буду подробно останавливаться на установке и настройке MetalLB, так как предполагаю вы уже имеете некоторый опыт. Предлагаю сразу перейти к делу, а именно к настройке маршрутизации. Итак мы имеем четыре кейса:

 [Читать дальше →](https://habr.com/ru/articles/501842/?utm_campaign=501842&utm_source=habrahabr&utm_medium=rss#habracut)

<!--more-->
