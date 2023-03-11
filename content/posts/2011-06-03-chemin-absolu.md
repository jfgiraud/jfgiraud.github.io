---
title: "Chemin absolu"
date: 2011-06-03T12:44:00+01:00
tags: [ "shell", "commande", "absolu", "relatif", "readlink" ]
description: "La commande readlink permet de retourner le chemin absolu d'un fichier/répertoire en suivant éventuellement les liens symboliques"
---

La commande readlink permet de retourner le chemin absolu d'un fichier/répertoire en suivant éventuellement les liens symboliques  
```
$ readlink -f ~/.emacs
/home/user/etc/emacs/dot_emacs.el
```
