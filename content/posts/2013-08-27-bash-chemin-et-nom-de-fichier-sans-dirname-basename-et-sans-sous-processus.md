---
title: "bash, chemin et nom de fichier sans dirname/basename (et sans sous-processus)"
date: 2013-08-27T10:37:00+01:00
---
Voici une astuce pour récupérer le chemin et le nom d'un fichier sans utiliser les commandes dirname/basename (et sans la création de sous-processus lors de l'appel à ces commandes)


```
$ s='abc/def/ghi/klmnop.ext'
$ echo ${s##*/}
klmnop.ext
$ echo ${s%/*}
abc/def/ghi
```

Cela permet d'optimiser la récupération de ces informations lors de traitements sur un grand nombre de fichiers par exemple.
