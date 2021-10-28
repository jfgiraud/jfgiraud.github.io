---
layout: post
title: "bash, ajouter du contenu en début de fichier"
date: "2014-09-18 15:06:00"
---
Voici deux techniques pour ajouter du contenu en début de fichier.<br /><br />L'une utilise le programme <code>sponge</code> mais nécessite l'installation du paquet <code>moreutils</code>, l'autre est "plus" standard puisqu'utilise <code>tee</code> disponible dans <code>coreutils</code>.<br /><br /><script src="http://pastebin.com/embed_js.php?i=zrKWnyXB"></script><br /><br />Une différence existe toutefois entre les deux. En effet <code>tee</code> produit sur la sortie standart le texte généré. 
