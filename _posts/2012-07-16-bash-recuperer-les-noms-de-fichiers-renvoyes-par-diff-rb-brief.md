---
layout: post
title: "bash, récupérer les noms de fichiers renvoyés par diff -rb --brief"
date: "2012-07-16 14:05:00"
---
La commande "diff -rb --brief" génère des lignes user-friendly qui sont malheureusement localisées. <br />Pour récupérer le nom des fichiers qui diffèrent, il est possible d'utiliser la commande lsdiff du package patchutils.<br /> <code><pre><br />$ sudo apt-get install patchutils<br />$ files_to_transfer=$(diff -x '*.zip' -x '.svn' -rb -U 1 <br />      fitnesse-install/FitNesseRoot/FrontPage/Project <br />      $dist_install/FrontPage/Project | lsdiff)<br /></pre></code>