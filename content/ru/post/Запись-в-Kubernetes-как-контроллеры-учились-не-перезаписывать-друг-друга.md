---
title: "Запись в Kubernetes: как контроллеры учились не перезаписывать друг друга"
date: 2026-05-26T05:46:53+00:00
link: https://habr.com/ru/companies/aenix/articles/1039282/?utm_campaign=1039282&utm_source=habrahabr&utm_medium=rss
source: habr
---

![](https://habrastorage.org/getpro/habr/upload_files/f6e/e36/b4a/f6ee36b4acbcd49bec647228a82048ac.png)

Привет. В [прошлой статье](https://habr.com/ru/companies/aenix/articles/1031818/) мы в основном говорили про **чтение** — кэш в `controller-runtime`, informer’ы, `Reflector`, `DeltaFIFO`, почему `r.Get` в реконсайле не ходит в apiserver. Сегодня поговорим больше про **запись**.

Kubernetes по своей природе спроектирован так, что **одним и тем же объектом могут управлять разные контроллеры — и это нормально**. На один Deployment смотрят и `deployment-controller` (правит status), и HPA (правит `spec.replicas`), и admission-мутаторы (расставляют labels), и `cert-manager` (дописывает свои аннотации), и пользователь с `kubectl apply`. Каждый из них отвечает за свои поля и не лезет в чужие. И всё это работает.

Сегодня будем разбираться, какие механизмы в Kubernetes позволяют разным компонентам делить ответственность за части одного и того же объекта, не превращая запись в гонку — и как ими правильно пользоваться, когда оператор пишете вы сами. Добро пожаловать под кат.
