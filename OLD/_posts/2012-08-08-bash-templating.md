---
layout: post
title: "Bash, templating..."
date: "2012-08-08 14:37:00"
tags: bash templating
---

Pour faire un système de templating en bash (par exemple pour du mailing) on peut faire ainsi si l'on souhaite que le modèle soit dans un fichier à part :

```bash
$ cat template.txt 
<b>Hello '"${firstname}"</b>
Bye '"${firstname}"'

$ for firstname in luc jeff gwen
> do 
>   while read line 
>   do 
>      eval echo "'$line'"
>   done < template.txt
> done
<b>Hello luc</b>
Bye luc
<b>Hello jeff</b>
Bye jeff
<b>Hello gwen</b>
Bye gwen
``` 

Avec les Here Documents, cela aurait été plus simple...
