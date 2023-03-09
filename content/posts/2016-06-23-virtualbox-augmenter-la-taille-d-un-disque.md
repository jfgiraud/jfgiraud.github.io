---
title: "virtualbox, augmenter la taille d'un disque"
date: 2016-06-23T15:37:00+01:00
tags: ["virtualbox"]
---
Voici la procédure pour augmenter la taille d'un disque :

[http://blog.francis-fustier.fr/en/virtualbox-augmenter-la-taille-du-disque-virtuel/](http://blog.francis-fustier.fr/en/virtualbox-augmenter-la-taille-du-disque-virtuel/)


```
sudo vboxmanage modifyhd « path / volume name» –resize [size]


Size : 15360 = 15 GB, 20480 = 20 GB, 30720 = 30 GB, etc..
```

J'ai adapté la partie #2 de la procédure comme suit :



- Sous windows 7, il faut rechercher l'utilitaire "créer et formater des partitions de disque dur" et l'ouvrir
- Ensuite, il faut sélectionner le disque que l'on veut étendre et sélectionner "étendre le volume" (clic droit)


Lien additionnel Dérick (juin 2019) : [https://memo-linux.com/comment-augmenter-la-taille-dune-machine-virtuelle-sous-virtualbox/](https://memo-linux.com/comment-augmenter-la-taille-dune-machine-virtuelle-sous-virtualbox/)
