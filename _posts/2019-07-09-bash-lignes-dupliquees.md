---
layout: post
title: "bash, lignes dupliquées"
date: "2019-07-09 15:52:00"
tags: bash commande uniq lignes dupliquées
---
Dans d'anciens post, j'avais parlé de la commande `uniq`

Il est possible de ne garder que les lignes dupliquées. Il faut utiliser l'option `-d`


```
$ for A in 1 3 4 2 3 1 1 1 3; do echo $A; done | sort | uniq -dc
      4 1
      3 3
```



