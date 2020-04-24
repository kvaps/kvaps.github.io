---
title: Как работает дисковая подсистема в OpenNebula 
date: 2020-03-21 18:17:00
link: https://habr.com/ru/post/493406/
---

![](https://hsto.org/webt/nr/4p/bb/nr4pbbjdpjjvghyiapezxwhgna0.png)

В последнее время я получаю достаточно много вопросов по поводу организации стораджа в OpenNebula. В виду своей специфики она имеет аж три разных типа хранилища: images, system и files. Давайте разберёмся зачем нужен каждый из них и как их использовать чтобы планировать размещение данных наиболее эфективно.

Этот пост — частичная расшифровка моего [доклада про OpenNebula](https://www.youtube.com/watch?v=47Mht_uoX3A&feature=youtu.be) на [HighLoad++ 2019](https://www.highload.ru/moscow/2019/abstracts/5506) с упором на дисковую составляющую.

<!--more-->
