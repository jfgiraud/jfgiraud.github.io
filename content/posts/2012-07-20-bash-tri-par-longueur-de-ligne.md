---
title: "bash, tri par longueur de ligne"
date: 2012-07-20T11:32:00+01:00
tags: ["tri", "longueur", "sort", "awk"]
---
La commande sort ne permet pas de trier en fonction de la longueur des lignes. C'est dommage mais on peut utiliser awk, combiné avec sort pour avoir le même résultat.  

```
$ cat /usr/share/dict/words 
   | awk '{ print length(), $0 | "sort -n" }' 
   | cut -d ' ' -f 2-
```
