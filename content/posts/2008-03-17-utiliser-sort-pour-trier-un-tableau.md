---
title: "Utiliser sort pour trier un tableau"
date: 2008-03-17T10:53:00+01:00
tags: ["linux", "commande", "sort" ]
description: "Comment faire pour trier un tableau sur la sortie standard en fonction de certaines colonnes"
---

Trie les données sur les colonnes 2 et 3.

```text
$ printf "D,3,5,D\nA,1,10,A\nB,1,7,B\nC,3,2,C\n"
D,3,5,D
A,1,10,A
B,1,7,B
C,3,2,C
$ !! | sort  -t ',' -k 2n,2n -k 3n,3n
B,1,7,B
A,1,10,A
C,3,2,C
D,3,5,D
```
