---
title: "Kubernetes-in-Kubernetes и ферма серверов с загрузкой по PXE"
date: 2021-05-25
link: https://habr.com/ru/company/oleg-bunin/blog/558900/
---

![](https://hsto.org/getpro/habr/upload_files/1c5/449/a3d/1c5449a3d5864b48ca0d6791742cc4be.png)

Когда у вас 2 собственных дата-центра, тысячи железных серверов, виртуалки и хостинг для сотен тысяч сайтов, Kubernetes может существенно упростить управление всем этим добром. Как показала практика, с помощью Kubernetes можно декларативно описывать и управлять не только приложениями, но и самой инфраструктурой. Я работаю в крупнейшем чешском хостинг-провайдере WEDOS Internet a.s и сегодня расскажу о двух своих проектах — [Kubernetes-in-Kubernetes](https://github.com/kvaps/kubernetes-in-kubernetes) и [Kubefarm](https://github.com/kvaps/kubefarm).

С их помощью можно буквально за пару команд, используя Helm, развернуть полностью рабочий Kubernetes внутри другого Kubernetes-кластера. Как и зачем? Добро пожаловать под кат

<!--more-->
