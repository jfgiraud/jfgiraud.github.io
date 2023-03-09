---
title: "bash, récupérer les noms de fichiers renvoyés par diff -rb --brief"
date: 2012-07-16T14:05:00+01:00
---
La commande "diff -rb --brief" génère des lignes user-friendly qui sont malheureusement localisées. 
Pour récupérer le nom des fichiers qui diffèrent, il est possible d'utiliser la commande lsdiff du package patchutils.
 <code><pre>
$ sudo apt-get install patchutils
$ files_to_transfer=$(diff -x '*.zip' -x '.svn' -rb -U 1 
      fitnesse-install/FitNesseRoot/FrontPage/Project 
      $dist_install/FrontPage/Project | lsdiff)
</pre></code>
