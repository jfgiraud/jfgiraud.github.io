---
layout: post
title: "vi et les macros"
date: "2012-09-27 10:31:00"
---
Via un petit exemple...<br /><br /><pre><code><br />ggqqdwj@q<ESC>q@q<br /></code></pre><br />Permet de supprimer le premier mot de chaque ligne du buffer.<br /><br /><ul>  <li>gg permet d'aller en début de fichier<br />  <li>qq démarre l'enregistrement de la macro de nom q (la 2e lettre)<br />  <li>dwj supprime le premier mot et descend de ligne<br />  <li>@q appelle la macro q<br />  <li><ESC> pour revenir au mode de vi "normal"<br />  <li>q pour terminer l'enregistrement de la macro<br />  <li>@q pour appeler la macro<br /></ul>
