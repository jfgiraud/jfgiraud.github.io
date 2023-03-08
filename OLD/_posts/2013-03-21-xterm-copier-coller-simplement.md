---
title: "xterm, copier/coller simplement"
date: "2013-03-21 12:33:00"
---
Par défaut, la sélection avec xterm se fait de la manière suivante



- Passage: sélectionner le début du texte en maintenant le bouton gauche de la souris enfoncé et déplacer la souris jusqu'à la fin du texte. Relachez

- Mot: double cliquez sur le mot

- Ligne: triple cliquez sur la ligne


Pour changer la définition du mot pour prendre plus de choses comme des urls, il faut modifier son fichier ~/.Xresources  


```
xterm*charClass: 33:48, 37:48, 42:48, 45-47:48, 58:48, 63-64:48, 126:48
```  

Dès lors le double clic améliore le confort d'utilisation :) 


<a href="http://3.bp.blogspot.com/-7PPcwLDC6IE/UUrwPmqGYGI/AAAAAAAADrk/7A2eKDQUcnM/s1600/after.jpg" imageanchor="1" ><img border="0" src="http://3.bp.blogspot.com/-7PPcwLDC6IE/UUrwPmqGYGI/AAAAAAAADrk/7A2eKDQUcnM/s320/after.jpg" /></a>
