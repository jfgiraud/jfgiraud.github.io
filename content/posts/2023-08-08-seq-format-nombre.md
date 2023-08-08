---
title: "seq, format des nombres"
date: 2023-08-08T07:10:00+01:00
tags: [ "seq", "commande" ]
description: "Formater les nombres"
---

La commande seq permet de générer une liste de nombres.

L'option `-w` permet de faire en sorte que la sortie soit sur le même nombre de caractères. Dans le cas présent sur 2 (le nombre 31 est composé de 2 caractères).

```
$ seq -w 1 31
01
02
03
04
05
06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
```

Toutefois, il peut être utile de forcer.

Par exemple si on souhaite avoir 01 à 09 comme séquence (partie de date), l'option `-w`, ne permet pas d'avoir la sortie sur 2 caractères.

Il faut alors utiliser l'option `-f`

```
$ seq -f '%02g' 1 9
01
02
03
04
05
06
07
08
09
```
