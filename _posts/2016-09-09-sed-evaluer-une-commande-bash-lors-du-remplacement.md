---
layout: post
title: "sed, évaluer une commande bash lors du remplacement"
date: "2016-09-09 16:53:00"
---
Je souhaitai décoder des valeurs encodées en base64 via sed.

Le paramètre final "/e" de sed permet d'évaluer l'expression remplacée.

Ici c'est la commande bash qui affiche l'attribut suivi d'un ':' et de la valeur décodée.

Comme vous le constatez, l'utilisation des valeurs capturées est possible.

<script src="//pastebin.com/embed_js/mVyjBJUC"></script>

Le code a été difficile à trouver, c'est pourquoi je le partage :)
