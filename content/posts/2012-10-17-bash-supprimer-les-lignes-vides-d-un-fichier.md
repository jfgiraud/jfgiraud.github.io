---
title: "bash, supprimer les lignes vides d'un fichier"
date: 2012-10-17T10:06:00+01:00
tags: ["bash", "supprimer lignes vides", "sed", "awk", "remove empty lines"]
---

Voici plusieurs solutions

```bash
$ cat ~/fichier |  sed -e 's/^[[:space:]]*$//;/^$/d'
```


```bash
$ cat ~/fichier | awk NF
```

où NF indique le nombre de champs. Si ce n'est pas une ligne vide, le nombre de champs est positif et la commande par défaut de awk est d'afficher.
Ce qui équivaut à : 


```bash
$ cat ~/fichier | awk 'NF!=0 { print }'
```





