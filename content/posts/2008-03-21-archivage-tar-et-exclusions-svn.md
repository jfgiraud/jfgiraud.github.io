---
title: "Archivage tar et exclusions .svn"
date: 2008-03-21T16:06:00+01:00
tags: [ "commande", "tar", "option" ]
description: "Quelle option pour exclure certains parttern de la commande tar ?"
---

Pour exclure les répertoires lors de la création d'une archive avec tar,
il faut utiliser `--exclude pattern` après le nom de l'archive.

Exemple :

    tar zcvf nomarchive.tgz --exclude '.svn' batch/
