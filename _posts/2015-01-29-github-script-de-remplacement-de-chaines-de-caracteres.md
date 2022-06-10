---
layout: post
title: "Github, script de remplacement de chaines de caractères"
date: "2015-01-29 21:39:00"
tags: commande sed awk sandr
---
`sed` et `awk` sont très bien pour remplacer des chaines par d'autres. 

Toutefois, le fait que ce soit des regexp qu'ils attendent complique l'utilisation lorsque la chaine fixe recherchée contient des caractères pouvant être interprétés comme des "opérateurs" de rexexp (`?` par exemple)

`sandr` est un outil qui permet de faire des recherches de chaines fixes ou non. Des options permettent d'extraire les chaines matchées/remplacées dans un fichier et d'appliquer des remplacements de masse (via une table de hachage).

D'autres options bien utiles sont disponibles mais je vous laisse les découvrir sur le projet github [sandr](https://github.com/jfgiraud/sandr).

Bonne découverte !
