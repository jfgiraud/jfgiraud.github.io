---
title: "bash, affichage en mode intéractif"
date: 2012-08-08T13:17:00+01:00
tags: ["bash", "interactif"]
---
Dans un script bash, j'ai souhaité afficher un numéro de version lorsque celui-ci est lancé interactivement (ne reçoit pas de données depuis un pipe ou bien une redirection <).

Cela peut-être fait en utilisant l'option `-t` de la commande test.   

```
if [ -t 0 ]; then
    echo "Version: $VERSION"
fi
```
