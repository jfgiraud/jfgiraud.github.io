---
layout: post
title: "bash, mv en masse"
date: "2012-09-25 13:36:00"
tags: commande, mmv, renommage en masse
---
Il y a quelques années, j'avais écris un petit programme qui permettait de changer l'extension de fichiers.

A cette époque, je ne connaissais pas la commande mmv (comprendre "mass"mv) :


```
$ sudo apt-get install mmv
$ ls -l *.abc
-rw-r--r-- 1 root root 0 2012-09-25 13:34 x.abc
-rw-r--r-- 1 root root 0 2012-09-25 13:34 y.abc
-rw-r--r-- 1 root root 0 2012-09-25 13:34 zzz.abc
$ mmv "*.abc" "#1.ABC"
$ ls -l *.abc
ls: impossible d'accéder à *.abc: Aucun fichier ou dossier de ce type
$ ls -l *.ABC
-rw-r--r-- 1 root root 0 2012-09-25 13:34 x.ABC
-rw-r--r-- 1 root root 0 2012-09-25 13:34 y.ABC
-rw-r--r-- 1 root root 0 2012-09-25 13:34 zzz.ABC
```

A noter : cette commande permet aussi de supprimer l'extension des fichiers...
