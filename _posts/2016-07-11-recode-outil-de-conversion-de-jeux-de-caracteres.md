---
layout: post
title: "recode, outil de conversion de jeux de caractères"
date: "2016-07-11 15:00:00"
tags: html commande recode decode encode
---

```
$ echo 'a&lt;b&amp;&nbsp;c&eacute;' | recode html
a<b& cé
```
