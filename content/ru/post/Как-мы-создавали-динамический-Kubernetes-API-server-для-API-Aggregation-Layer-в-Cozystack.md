---
title: "Как мы создавали динамический Kubernetes API server для API Aggregation Layer в Cozystack"
date: 2024-11-26T11:28:40+00:00
link: https://habr.com/ru/companies/aenix/articles/832824/?utm_campaign=832824&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/ef4/892/4ae/ef48924aeece5591835a65f911cfb7ef.png)

Kubernetes действительно поражает своими могучими возможностями к расширению. Вы наверняка уже знаете про [operator-паттерн](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), а также фреймворки [kubebuilder](https://book.kubebuilder.io/) и [operator-sdk](https://sdk.operatorframework.io/) с помощью которых можно его реализовать. Если вкратце, то они позволяют расширять ваш Kubernetes через определение кастом-ресурсов (CRDs) и написание дополнительного контроллера, который будет выполнять вашу бизнес-логику для реконсиляции и управления этими ресурсами. Этот подход широко изучен, а в интернете можно найти огромное количество информации о том, как написать такой оператор.

Однако это [не единственный метод](https://kubernetes.io/docs/concepts/extend-kubernetes/#api-extensions) расширения Kubernetes API. Так, для более сложных кейсов, например реализации императивной логики, сабресурсов и формирования ответов на лету, можно рассмотреть механизм API aggregation layer, который поддерживается в Kubernetes. В рамках aggregation layer можно разработать свой собственный extension API server и бесшовно интегрировать его в общий Kubernetes API.

В этой статье мы разберем, что такое API aggregation layer, для решения каких задач его стоит использовать, когда его использовать не стоит и как мы использовали эту модель для реализации собственного extension API server в платформе [Cozystack](http://cozystack.io).
