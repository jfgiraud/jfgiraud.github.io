---
title: "bash, éviter l'interprétation en octal en utilisant printf"
date: "2013-12-07 08:25:00"
---
J'ai eu un petit soucis dans un script de renommage qui tentait d'interprêter les valeurs commençant par 08 et 09 en octal lors d'un printf.

La solution consiste à spécifier que la valeur est en base 10 comme dans l'exemple ci-dessous :


```
s="09"
$ printf "%.02d" $s
bash: printf: 09: Nombre octal non valable
00
$ printf "%.02d" $(( 10#$s))
09
``` 
