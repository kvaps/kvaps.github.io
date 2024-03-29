---
title: 'Restic: эффективное резервное копирование из Stdin'
date: 2023-10-24
link: https://habr.com/ru/articles/769622/
---

![](https://habrastorage.org/r/w1560/getpro/habr/upload_files/089/e74/c08/089e74c08dad86a266fa154d5fe169a5.png)

Про restic я уже рассказывал в статье [Бэкап-хранилище для тысяч виртуальных машин свободными инструментами](https://habr.com/ru/articles/504152/), с тех пор он остаётся моим любимым инструментом для бэкапа.

Сегодня я опишу вам готовый рецепт того как настроить эффективное бэкапирование чего угодно прямо из stdin, с дедупликацией и автоматической очисткой репозитория от старых копий.

Несмотря на то, что restic отлично подходит для сохранения целых каталогов с данными в этой статье мне хотелось бы сделать упор на сохранении резервных копий на лету прямо из Stdin.

Как правило это бывает актуально для сохранения бэкапов виртуальных машин, баз данных и других, представленных одним большим файлом, данных, которые можно последовательно вычитывать и сразу отправлять в систему бэкапирования.

<!--more-->
