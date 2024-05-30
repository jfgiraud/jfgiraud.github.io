---
title: "Comptabiliser le nombre d'occurences"
date: 2008-03-12T11:52:00+01:00
tags: ["linux", "commande", "uniq"]
description: "Voici une commande qui permet de ne merger les lignes adjacentes (les dédupliquer) et de compter le nombre d'occurence qu'il y avait"
---
Utiliser la commande <span style="font-style: italic;">uniq </span>pour afficher ou omettre des lignes récupérées de l'entrée standard. L'option -c permet de comptabiliser les lignes (qui doivent être ordonnées)

Associer avec sort.

```shell
for A in 1 3 4 2 3 1 1 1 3; do 
    echo $A; 
done | sort | uniq -c
```
```
      4 1
      1 2
      3 3
      1 4
```

La page de manuel : [https://man7.org/linux/man-pages/man1/uniq.1.html](https://man7.org/linux/man-pages/man1/uniq.1.html)