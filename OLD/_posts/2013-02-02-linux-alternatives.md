---
title: "Linux, alternatives"
date: "2013-02-02 11:09:00"
---
A chaque fois, on fait des bidouilles pour utiliser une version d'un exécutable (par exemple java) plutôt qu'une autre...

Pourtant il existe les alternatives sous linux qui permettent de basculer vers une version particulière...


```
$ sudo update-alternatives --install "/usr/bin/java" "java" "/home/me/Logiciels/jre1.7.0_13/bin/java" 1
[sudo] password for me: 

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

<div style="height: 0; overflow: hidden;">update-alternatives config java install
</div>
