---
layout: post
title: "VirtualBox, connaitre l'IP de la machine hôte"
date: "2021-05-21 12:12:00"
tags: virtualbox ipconfig commandes
---

Dans le terminal de la VM, `ipconfig` donne l'information dans 
```text
Passerelle par défaut. . . . . . . . . : xxx
```  

`netstat -rn` donne l'information dans "Adr. passerelle"

```text
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
0.0.0.0               0.0.0.0        xxx               yyy            10
```  
