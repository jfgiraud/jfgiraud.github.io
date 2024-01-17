---
title: "XPath et recherche vide..."
date: 2012-03-29T09:48:00+01:00
tags: ["xpath"]
---
Recherche des lignes d'un tableau ayant dans la 3e colonne une valeur à XXX :

Si XXX est vide :
```
//table/tr/td[3][not(text())]/..
```

Sinon
```
//table/tr/td[3][text() = '" + XXX + "']/..
```
