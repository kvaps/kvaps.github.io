---
title: Store SSH Keys Securely
date: 2019-05-14
link: https://medium.com/@kvaps/store-ssh-keys-safely-bba43779290a
---

![](https://miro.medium.com/max/852/0*JlXp6Hsyfcvk7LSi.png)

Let me tell you how you can safely store SSH keys on a local machine, for not having a fear that some application can steal or decrypt them.
This article will be especially useful to those who have not found an elegant solution after the [paranoia](https://latacora.singles/2018/08/03/the-default-openssh.html) in 2018 and continue storing keys in `$HOME/.ssh`.

To solve this problem, I suggest you using [KeePassXC](https://keepassxc.org/), which is one of the best password managers, it is using strong encryption algorithms, and also it have an integrated SSH agent.

This allows you to safely store all the keys directly in the password database and automatically add them to the system when it is opened. Once the base is closed, the use of SSH keys will also be impossible

<!--more-->
