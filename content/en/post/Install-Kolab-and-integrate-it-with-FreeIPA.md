---
title: "Install Kolab and integrate it with FreeIPA"
date: 2018-10-04
link: https://medium.com/@kvaps/install-kolab-and-integrate-it-with-freeipa-c80c3b34b7b7
---

![](https://miro.medium.com/max/751/1*nR-RW_hUa89nBl1OmWaPuQ.png)

Here is written steps for install [Kolab Groupware](https://kolab.org/) server and integrate it with [FreeIPA](https://www.freeipa.org/page/Main_Page) server.

Most of actions requires basic understanding in LDAP mechanism.
FreeIPA should be already installed before preparing Kolab installation.
We will connect only users from the existing tree (which provided by FreeIPA), and we will create new tree for the rest Kolab resources, like mail groups, shared mailboxes, etc.

In the end, we will can authenticate them, edit their parameters via kolab-webadmin, and manage other resources.

<!--more-->
