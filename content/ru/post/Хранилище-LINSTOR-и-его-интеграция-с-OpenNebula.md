---
title: "Хранилище LINSTOR и его интеграция с OpenNebula"
date: 2019-05-13T01:18:00+03:00
link: https://habr.com/post/451186/
---

![](https://habrastorage.org/webt/e-/3z/h-/e-3zh-bbwjnljyazm68edln7muw.png)

Не так давно ребята из LINBIT представили свое новое SDS-решение - Linstor. Это полностью свободное хранилище в основе которого используются проверенные технологии: DRBD, LVM, ZFS. Linstor сочетает в себе простоту и хорошо проработанную архитектуру, что позволяет добиться стабильности и достаточно внушительных результатов.

Сегодня я хотел бы рассказать про него чуть подробнее и показать насколько просто его можно интегрировать с OpenNebula используя linstor_un - новый драйвер, который я разработал специально для этой цели.

Linstor в сочетании с OpenNebula позволяет построить быстрое и надежное облако, которое можно без проблем развернуть на собственной инфраструктуре

<!--more-->
