---
layout: post
title: "bash, cas conditionel suivant la présence ou non d'un texte dans un fichier"
date: "2012-09-06 10:43:00"
---
Cela se fait simplement avec un grep...  

<script src="https://pastebin.com/embed_js/QCiWY0US"></script>

<div style="overflow:hidden; height:0;">if, grep, exit, status, bash</div>
Bien que le test semble inversé, il est correct car la sortie du grep avec un status à 0 est un succès.

Le paragraphe "Conditional Shell Control Structures" de la page [http://teaching.idallen.com/dat2330/04f/notes/exit_status.txt](http://teaching.idallen.com/dat2330/04f/notes/exit_status.txt) l'explique très bien.


