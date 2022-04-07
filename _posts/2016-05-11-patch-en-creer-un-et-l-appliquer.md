---
layout: post
title: "patch, en créer un et l'appliquer"
date: "2016-05-11 11:26:00"
---
Voici un exemple pour utiliser la commande patch :


```
svn diff > patch.diff
svn revert -R .
patch -p0 < patch.diff
```

Parfois, elle peut-être utile. Ici c'est surtout pour retenir l'option -p0 que je poste cet article.
