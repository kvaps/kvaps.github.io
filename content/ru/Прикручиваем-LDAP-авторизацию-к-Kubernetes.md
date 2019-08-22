---
title: "Прикручиваем LDAP-авторизацию к Kubernetes"
date: 2019-02-21 03:17:00
link: https://habr.com/post/441112/
---

![](https://habrastorage.org/webt/kj/60/vi/kj60vi6ugv7bunlqdts2nlr2vja.png)

Небольшая инструкция о том, как используя Keycloak можно связать Kubernetes с вашим LDAP-сервером и настроить импорт пользователей и групп. Это позволит настраивать RBAC для ваших пользователей и использовать auth-proxy чтобы защитить Kubernetes Dashboard и другие приложения, которые не умеют производить авторизацию самостоятельно.

<!--more-->
