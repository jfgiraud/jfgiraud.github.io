---
title: "bash, tester si un programme est installé"
date: 2012-09-21T10:03:00+01:00
tags: ["which", "apt-get install", "sudo", "commande", "sponge"]
---
Pour tester si un programme est installé, on peut utiliser la commande `which`
de différentes manières.

La première en comptabilisant le nombre de lignes retournées.


```bash
if [ $(which sponge | wc -l) -eq 0 ]; then
    echo "Installer le paquet 'moreutils'."
    echo "sudo apt-get install moreutils"
    exit 1
fi
```

La seconde en utilisant le code de retour de la commande.


```bash
if ! which sponge >/dev/null; then
    echo "Installer le paquet 'moreutils'."
    echo "sudo apt-get install moreutils"
    exit 1
fi
```

La seconde est plus lisible, pas besoin de décrypter. 

C'est seulement dommage qu'on ne puisse pas ajouter un paramètre à la commande pour ne pas écrire sur la sortie standard et que l'on soit obligé de rediriger dans `/dev/null`.

A chacun sa préférence. 
