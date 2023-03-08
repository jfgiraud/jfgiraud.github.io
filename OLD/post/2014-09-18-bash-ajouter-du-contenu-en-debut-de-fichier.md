---
layout: post
title: "bash, ajouter du contenu en début de fichier"
date: "2014-09-18 15:06:00"
---
Voici deux techniques pour ajouter du contenu en début de fichier.

L'une utilise le programme <code>sponge</code> mais nécessite l'installation du paquet <code>moreutils</code>, l'autre est "plus" standard puisqu'utilise <code>tee</code> disponible dans <code>coreutils</code>.


```
$ echo 'Le contenu de mon super fichier' >> fichier.txt
$ echo 'Le contenu de mon super fichier' > fichier.txt
$ echo ajouter la ligne | cat - fichier.txt | sponge fichier.txt
$ cat fichier.txt 
ajouter la ligne
Le contenu de mon super fichier
$ echo ajouter la ligne | cat - fichier.txt | tee fichier.txt
ajouter la ligne
ajouter la ligne
Le contenu de mon super fichier
$ cat fichier.txt 
ajouter la ligne
ajouter la ligne
Le contenu de mon super fichier
$ echo ajouter la ligne | cat - fichier.txt | tee fichier.txt > /dev/null
$ cat fichier.txt 
ajouter la ligne
ajouter la ligne
ajouter la ligne
Le contenu de mon super fichier
```

Une différence existe toutefois entre les deux. En effet <code>tee</code> produit sur la sortie standart le texte généré. 
