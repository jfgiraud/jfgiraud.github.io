---
layout: post
title: "sed, mettre sur une ligne après avoir matché un pattern"
date: "2016-09-09 14:57:00"
---
<script src="https://pastebin.com/embed_js/d4M43kPz"></script>
(source: [http://stackoverflow.com/questions/12833714/the-concept-of-hold-space-and-pattern-space-in-sed](http://stackoverflow.com/questions/12833714/the-concept-of-hold-space-and-pattern-space-in-sed)


La commande ldapsearch peut renvoyer des attributs avec leur valeur en base64 (présence :: après le nom de l'attribut) sur une ou plusieurs lignes (commençant par un espace).

Je souhaitais donc les merger facilement.

En regardant du côté de sed, il est possible de le faire facilement.

L'exemple ci-dessous montre la commande :

<script src="https://pastebin.com/embed_js/cuqgnzMr"></script>

On recherche les attributs suivis de '::' puis on commence une boucle (:loop) dans laquelle on rajoute la ligne suivante (N) dans le "pattern space". On effectue alors le remplacement du retour chariot suivi de l'espace et on reboucle.


