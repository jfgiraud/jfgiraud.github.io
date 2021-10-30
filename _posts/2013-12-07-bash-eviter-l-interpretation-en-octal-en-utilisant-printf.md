---
layout: post
title: "bash, éviter l'interprétation en octal en utilisant printf"
date: "2013-12-07 08:25:00"
---
J'ai eu un petit soucis dans un script de renommage qui tentait d'interprêter les valeurs commençant par 08 et 09 en octal lors d'un printf.

La solution consiste à spécifier que la valeur est en base 10 comme dans l'exemple ci-dessous :

<script src="http://pastebin.com/embed_js.php?i=EczZmbtz"></script> 
