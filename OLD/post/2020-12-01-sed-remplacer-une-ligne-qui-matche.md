---
layout: post
title: "sed, remplacer une ligne qui matche"
date: "2020-12-01 11:16:00"
tags: sed 
---

Voici comment remplacer une ligne qui matche avec la commande `sed`

```text
$ printf "[section1]\\n\\n[section2]\\ncle1=valeur1\\n" | sed '/^\\[section2\\]/c cle2=valeur2'
[section1]

cle2=valeur2
cle1=valeur1
```
