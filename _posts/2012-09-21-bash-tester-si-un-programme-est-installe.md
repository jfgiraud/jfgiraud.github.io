---
layout: post
title: "bash, tester si un programme est installé"
date: "2012-09-21 10:03:00"
---
Pour tester si un programme est installé, on peut utiliser la commande `which`
de différentes manières.

La première en comptabilisant le nombre de lignes retournées.

<script src="https://pastebin.com/embed_js/zYiQWwVn"></script>

La seconde en utilisant le code de retour de la commande.

<script src="https://pastebin.com/embed_js/cU9AC5Qy"></script>

<div style="overflow:hidden; height:0;">which, apt-get install, sudo</div>
La seconde est plus lisible, pas besoin de décrypter. 

C'est seulement dommage qu'on ne puisse pas ajouter un paramètre à la commande pour ne pas écrire sur la sortie standard et que l'on soit obligé de rediriger dans `/dev/null`.

A chacun sa préférence. 
