---
title: "Linux, alternatives"
date: 2013-02-02T11:09:00+01:00
tags: [ "alternatives", "linux", "java" ]
description: "Lister et positionner une alternative java"
---

A chaque fois, on fait des bidouilles pour utiliser une version d'un exécutable (par exemple java) plutôt qu'une autre...

Pourtant il existe les alternatives sous linux qui permettent de basculer vers une version particulière...

#### Installer une alternative

```
$ sudo update-alternatives --install "/usr/bin/java" "java" "/home/me/Logiciels/jre1.7.0_13/bin/java" 1
[sudo] password for me: 
```

# choisir une alternative avec intéraction

```
$ sudo update-alternatives --config java
Il existe 2 choix pour l'alternative java (qui fournit /usr/bin/java).

  Sélection   Chemin                                          Priorité  État
------------------------------------------------------------
* 0            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1071      mode automatique
  1            /home/me/Logiciels/jre1.7.0_13/bin/java          1         mode manuel
  2            /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java   1071      mode manuel

Appuyez sur <Entrée> pour conserver la valeur par défaut[*] ou choisissez le numéro sélectionné :
$
```


Page de manuel : [https://man7.org/linux/man-pages/man1/update-alternatives.1.html](https://man7.org/linux/man-pages/man1/update-alternatives.1.html)