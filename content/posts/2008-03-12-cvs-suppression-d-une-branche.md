---
title: "CVS: suppression d'une branche"
date: 2008-03-12T11:07:00+01:00
tags: ["cvs", "versioning"]
description: "Découvrez la commande à utiliser pour supprimer une branche"
---
Ce matin, j'ai crée une branche à la place d'un tag. La correction n'est pas évidente pour nettoyer :

```text
# renommage du tag en branche
cvs rtag -b -r &lt;version&gt;_TAG &lt;version&gt;_BRANCH &lt;application&gt;
# suppression de la branche
cvs rtag -d -B &lt;version&gt;_TAG &lt;application&gt;
```

Lien externe : [http://www.delorie.com/gnu/docs/cvs/cvs_51.html](http://www.delorie.com/gnu/docs/cvs/cvs_51.html)
