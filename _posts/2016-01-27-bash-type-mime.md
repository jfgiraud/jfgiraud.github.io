---
layout: post
title: "bash, type mime"
date: "2016-01-27 11:55:00"
---
On peut déterminer le type mime d'un fichier en bash en utilisant la commande file


```
$ file --mime-type tests-fitnesse.tgz
tests-fitnesse.tgz: application/gzip
$ file --mime-type -b tests-fitnesse.tgz
application/gzip
$ file -i -b tests-fitnesse.tgz
application/gzip; charset=binary
$ file --mime-encoding tests-fitnesse.tgz
tests-fitnesse.tgz: binary
$ file --mime-encoding -b tests-fitnesse.tgz
binary

-b : supprime le nom du fichier
--mime-type : type mime
--mime-encoding : encoding
-i : type mime + encoding
```
