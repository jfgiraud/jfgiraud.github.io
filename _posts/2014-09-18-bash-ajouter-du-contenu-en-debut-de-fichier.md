---
layout: post
title: "bash, ajouter du contenu en début de fichier"
date: "2014-09-18 15:06:00"
---
Voici deux techniques pour ajouter du contenu en début de fichier.

L'une utilise le programme <code>sponge</code> mais nécessite l'installation du paquet <code>moreutils</code>, l'autre est "plus" standard puisqu'utilise <code>tee</code> disponible dans <code>coreutils</code>.

<script src="https://pastebin.com/embed_js/zrKWnyXB"></script>

Une différence existe toutefois entre les deux. En effet <code>tee</code> produit sur la sortie standart le texte généré. 
