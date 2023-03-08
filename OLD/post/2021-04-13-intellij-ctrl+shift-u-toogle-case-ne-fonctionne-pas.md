---
layout: post
title: "intellij, ctrl+shift u (toogle case) ne fonctionne pas"
date: "2021-04-13 17:18:00"
tags: intellij
---

Le raccourci `ctrl` `shift` `u` (toogle case) ne fonctionne pas, il propose de saisir un code unicode (Linux Ubuntu : Unity).

Ajouter après le shebang du fichier `bin/idea.sh` :

```text
export XMODIFIERS=""
```
   
