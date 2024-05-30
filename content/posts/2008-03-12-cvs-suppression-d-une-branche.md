---
title: "CVS: suppression d'une branche"
date: 2008-03-12T11:07:00+01:00
tags: ["cvs", "versioning"]
description: "Découvrez la commande à utiliser pour supprimer une branche"
---
Ce matin, j'ai crée une branche à la place d'un tag. La correction n'est pas évidente pour nettoyer :

### renommage du tag en branche

```shell
cvs rtag -b -r VERSION_TAG VERSION_BRANCH APPLICATION
```

### suppression de la branche

```shell
cvs rtag -d -B VERSION_TAG APPLICATION
```

Lien externe : [http://www.delorie.com/gnu/docs/cvs/cvs_51.html](http://www.delorie.com/gnu/docs/cvs/cvs_51.html)
