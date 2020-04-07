---
title: Forwarding USB to a virtual network via UsbRedir and QEMU [machine translation]
date: 2015-08-20 11:55:00
link: https://weekly-geekly.github.io/articles/265065/index.html
---

![](https://hsto.org/files/e6a/1bc/05d/e6a1bc05d70c460399d3276fdec28d2c.png)

To date, there are quite a few ways to forward a USB device to another computer or virtual machine over the network.

Of the most popular, hardware such as AnywhereUSB and purely software products, from those that I tried myself: USB Redirector and USB / IP.

I would like to tell you about another interesting method that works directly with the QEMU emulator.

It is also part of the spice project, officially supported by RedHat.



UsbRedir, is an open protocol for forwarding usb-devices via tcp to a remote virtual server, developed with the support of RedHat in the framework of the spice project. But as it turned out they can be quite successfully used without spice. The server is usbredirserver, which fumbles a usb device on a specific port, and QEMU itself as a client, which emulates the connection of an exported usb device to a specific usb controller of your virtual machine. Thanks to this approach, absolutely any OS can be used as a guest system, since it does not even know that the device is remotely forwarded, and all the logic rests on QEMU. 

<!--more-->
