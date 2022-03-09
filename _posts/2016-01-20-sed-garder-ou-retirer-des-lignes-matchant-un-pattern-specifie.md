---
layout: post
title: "sed, garder ou retirer des lignes matchant un pattern spécifié"
date: "2016-01-20 11:36:00"
tags: commande sed delete
---
Il est possible d'utiliser sed pour filter des lignes et garder/ne pas garder celles qui matchent un pattern spécifié

Dans l'exemple suivant, on garde ou ne garde pas les lignes contenant le terme *ou*


```bash
$ cat content.txt 
Ceci est un texte
    avec une tabulation avant
  ou bien deux espaces
        ou encore un mix des deux
$ cat content.txt | sed '/ou/d'
Ceci est un texte
    avec une tabulation avant
$ cat content.txt | sed '/ou/!d'
  ou bien deux espaces
        ou encore un mix des deux
```

Il est tout à fait possible d'utiliser l'option in-place de sed pour travailler sur le fichier lui même.
