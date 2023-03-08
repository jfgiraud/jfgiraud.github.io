---
layout: post
title: "sed, évaluer une commande bash lors du remplacement"
date: "2016-09-09 16:53:00"
tags: commande sed evaluation
---
Je souhaitai décoder des valeurs encodées en base64 via sed.

Le paramètre final "/e" de sed permet d'évaluer l'expression remplacée.

Ici c'est la commande bash qui affiche l'attribut suivi d'un ':' et de la valeur décodée.

Comme vous le constatez, l'utilisation des valeurs capturées est possible.


```
$ cat /tmp/example.txt 
cn: John Doe @ Home
displayName:: Sm9obiBEb2UK
mail: johndoe@home.com
$ cat /tmp/example.txt | sed -re "s/([^:]+):: (.*)$/echo \\1: \$(echo \\2 | base64 -d)/e"
cn: John Doe @ Home
displayName: John Doe
mail: johndoe@home.com
```

Le code a été difficile à trouver, c'est pourquoi je le partage :)
