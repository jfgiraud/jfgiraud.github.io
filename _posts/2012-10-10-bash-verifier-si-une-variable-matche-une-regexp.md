---
layout: post
title: "bash, vérifier si une variable matche une regexp"
date: "2012-10-10 10:09:00"
tags: bash, regexp, re
---
On peut facilement vérifier si une donnée contenue dans une variable est au bon format.

Dans l'exemple ci-dessous, on vérifie si le numéro de version fourni est correct.


```bash
if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Le numéro de version donné '$version' n'a pas le bon format."
    exit 1
fi
```

Dans celui-ci si la valeur contient localhost ou itg


```bash
[[ $environnement =~ localhost|itg ]] && echo 1
```

Attention, la regexp n'est pas entre quote ni double-quote.

