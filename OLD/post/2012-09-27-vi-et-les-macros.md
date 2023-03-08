---
layout: post
title: "vi et les macros"
date: "2012-09-27 10:31:00"
---
Via un petit exemple...

<pre><code>
ggqqdwj@q<ESC>q@q
</code></pre>
Permet de supprimer le premier mot de chaque ligne du buffer.



  - gg permet d'aller en début de fichier
  - qq démarre l'enregistrement de la macro de nom q (la 2e lettre)
  - dwj supprime le premier mot et descend de ligne
  - @q appelle la macro q
  - <ESC> pour revenir au mode de vi "normal"
  - q pour terminer l'enregistrement de la macro
  - @q pour appeler la macro



