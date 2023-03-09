---
title: "commande, history"
date: 2018-04-20T15:26:00+01:00
tags: ["commande", "history"]
---
Parfois, on ne sait plus si on a relancé une commande dans le terminal...

Pour avoir un historique daté, voici une petite configuration à ajouter à son .bashrc


```bash
export HISTTIMEFORMAT="%d/%m %H:%M "
```

Désormais, l'appel à l'historique produit des lignes avec les informations jour/mois heure/minute 


```bash
$ history
  492  19/04 16:15 cat ko | sed -e 's/.*(//' -e 's/ seconds.*//' -e 's/^[[:space:]]*$//;/^$/d' | awk '{SUM += $1} END {print "Total : "SUM}'
  493  19/04 16:15 connect jenk
```
