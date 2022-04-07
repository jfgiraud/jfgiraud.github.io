---
layout: post
title: "python, connaitre le dernier jour d'un mois..."
date: "2015-03-05 22:09:00"
tags: python calendrier jour day agenda dernier
---
Il est possible de déterminer facilement le dernier jour d'un mois.

Pour cela on peut utiliser le module calendar (bibliothèque standard) qui est assez méconnu.


```
>>> import calendar
>>> calendar.monthrange(2015,2)
(6, 28)
```

Le résultat indique pour Février 2015:
- que le mois comporte 28 jours
- que le premier jour du mois est un dimanche (0=Lundi, 1=Mardi, ... 6=Dimanche)


