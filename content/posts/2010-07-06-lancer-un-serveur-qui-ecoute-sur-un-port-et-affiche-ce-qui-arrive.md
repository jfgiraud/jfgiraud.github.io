---
title: "Lancer un serveur qui écoute sur un port et affiche ce qui arrive"
date: 2010-07-06T11:27:00+01:00
tags: [ "commande", "socat" ]
description: "Lancer un serveur qui écoute sur un port et affiche ce qui arrive"
---

```text
    socat TCP4-LISTEN:7533,reuseaddr STDOUT
```
