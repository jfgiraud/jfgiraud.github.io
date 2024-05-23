---
title: "bash, sommer une colonne...."
date: 2012-05-24T16:11:00+01:00
tags: ["bash", "commande", "awk", "tr", "paste", "bc", "sed"]
---
Comment sommer des valeurs provenant d'un fichier ou de la sortie standard.  Voici plusieurs solutions...

A la `awk` :
```bash
printf "1\n2\n3\n" | awk '{s+=$1} END {print s}'
```
A la `tr` : 
```bash
printf "1\n2\n3\n"| tr '\n' '+' | sed -e 's/+$/\n/' | bc
```
A la `paste` : 
```bash
printf "1\n2\n3\n" | paste -sd+ | bc
```

Moi je choisis la troisième solution. Elle est plus courte, simple et efficace !!

