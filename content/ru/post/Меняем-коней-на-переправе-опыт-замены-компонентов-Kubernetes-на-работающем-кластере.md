---
title: "«Меняем коней на переправе»: опыт замены компонентов Kubernetes на работающем кластере"
date: 2022-04-01T10:37:00+03:00
link: https://habr.com/ru/company/vk/blog/653035/
---

![](https://habrastorage.org/webt/ch/gl/xn/chglxn53qb8qqo-hou3qxtcx5xc.png)
*Fix by [MacRebisz](https://www.deviantart.com/macrebisz)*

Привет, я Андрей Квапил, Solution Architect в компании «Флант». Моя специализация — архитектурные решения на базе Kubernetes, в том числе на bare metal, а также разработка и эксплуатация облачных платформ и software-defined storage. 

В Kubernetes часто можно столкнуться с ограничениями, immutable-полями и прочими особенностями. Я хочу показать, что при необходимости такие ограничения можно обходить, а также познакомить вас с паттерном controller и наглядно продемонстрировать работу CNI-, CSI- и CRI-плагинов.

<!--more-->
