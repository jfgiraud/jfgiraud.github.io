---
title: "bash, vérifier que le fichier est sourcé"
date: "2015-12-03 14:59:00"
tags: bash source
---
Le code suivant permet de vérifier que le script est sourcé et non exécuté


```
#!/bin/bash

if [[ ${BASH_SOURCE[0]} == $0 ]]; then
    echo "Le script doit être sourcé (commande : source $0)"
    exit 1
fi
```


```
$ ../tools/stats.sh 
Le script doit être sourcé (commande : source ../tools/stats.sh)
$ source ../tools/stats.sh 
Using /home/user/.rvm/gems/ruby-1.8.7-head
(env)$
```
