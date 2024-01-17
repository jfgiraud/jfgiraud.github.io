---
title: "Xpath et dernier élément d'une liste..."
date: 2012-03-29T12:37:00+01:00
tags: ["xpath"]
---
Pour ne récupérer que le dernier élément d'une liste (attention aux parenthèses) : 

```
(.//td[@name='ID']/..)[last()]
```
