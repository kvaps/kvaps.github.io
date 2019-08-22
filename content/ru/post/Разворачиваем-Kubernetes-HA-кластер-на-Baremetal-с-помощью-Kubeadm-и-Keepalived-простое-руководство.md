---
title: "Разворачиваем Kubernetes HA-кластер на Baremetal с помощью Kubeadm и Keepalived (простое руководство)"
date: 2018-10-27T14:38:00+03:00
link: https://habr.com/post/427941/
---

Эта статья является свободной интерпретацей официального руководства <a href="https://kubernetes.io/docs/setup/independent/high-availability/">Creating Highly Available Clusters with kubeadm</a> для <a href="https://kubernetes.io/docs/setup/independent/high-availability/#stacked-control-plane-nodes">Stacked control plane nodes</a>. Мне не нравятся сложный язык и примеры использованные в нем, поэтому я написал свое руководство.

Если у вас появятся какие-либо вопросы или вам будет что-то неясно, обратитесь к официальной документации или спросите <a href="https://www.google.com/">Google</a>. Все этапы описаны здесь в максимально простой и сдержанной форме.

<!--more-->
