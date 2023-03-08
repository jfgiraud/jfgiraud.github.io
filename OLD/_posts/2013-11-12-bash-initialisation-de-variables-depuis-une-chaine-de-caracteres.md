---
layout: post
title: "bash, initialisation de variables depuis une chaine de caractères"
date: "2013-11-12 22:31:00"
---
Il est possible d'initialiser des variables depuis une chaine de caractères
et en redéfinissant le séparateur si nécessaire (ici la redéfinition est locale au read)


```
$ line=abc:def:567
$ IFS=: read c1 c2 c3 <<< "$line"
$ echo $c1
abc
$ echo $c2
def
$ echo $c3
567
```
