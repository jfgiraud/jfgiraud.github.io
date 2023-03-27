---
title: "cat, afficher un fichier avant et après la sortie standard"
date: 2021-12-07T10:07:00+01:00
tags: [ "cat", "commande" ]
description: "Afficher un fichier avant et après la sortie standard"
---


```
$ echo toto > before
$ echo tata > after
$ echo tutu | cat before - after
toto
tutu
tata
$ 
```
