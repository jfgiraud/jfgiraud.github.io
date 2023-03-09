---
title: "sed, supprimer une ou des lignes en fonction de leurs numéros"
date: 2016-07-12T10:36:00+01:00
tags: ["sed", "ligne", "lignes", "supprimer", "entre"]
---
Il est possible d'utiliser sed pour supprimer une ligne en fonction de son numéro ou un ensemble de lignes défini par le numéro de ligne de départ et de fin.

Voici un exemple :


```
$ free 
             total       used       free     shared    buffers     cached
Mem:      11997816    4512068    7485748     360084     283812    1716000
-/+ buffers/cache:    2512256    9485560
Swap:     12270588          0   12270588
$ free | sed '2d'
             total       used       free     shared    buffers     cached
-/+ buffers/cache:    2514236    9483580
Swap:     12270588          0   12270588
$ free | sed '2,3d'
             total       used       free     shared    buffers     cached
Swap:     12270588          0   12270588
```

Ceci permet d'éviter de jouer avec une succession de head/tail...

