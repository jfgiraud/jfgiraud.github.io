---
title: "Bash, comment faire pour exécuter du code en fonction de la présence de fichier*s*"
date: 2015-01-14T16:47:00+01:00
tags: ["bash", "if"]
---
Bash met à disposition des opérateurs pour tester l'existence de fichiers, leur type, droits d'accès...

Toutefois, dans certains cas, on peut souhaiter tester la présence de fichiers et appliquer un traitement si l'un d'entre eux existe.

On peut utiliser la commande ls couplée à if comme le montre l'exemple ci-dessous


```
$ touch /tmp/{a,b}.done
$ if ls /tmp/*.done &> /dev/null; then echo des fichiers done existent; fi 
des fichiers done existent
$ if ls /tmp/xxx*.done &> /dev/null; then echo des fichiers xxxdone existent; fi 
$
```
