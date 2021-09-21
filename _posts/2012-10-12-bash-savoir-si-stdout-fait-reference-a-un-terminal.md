---
layout: post
title: "bash, savoir si stdout fait référence à un terminal"
date: "2012-10-12 15:53:00"
---
Pour savoir si la sortie standard pointe sur un terminal, on peut utiliser l'opérateur "-t" en bash.<br /><br /><script src="http://pastebin.com/embed_js.php?i=3ZFV0srW"></script><br /><br />Dans le cas présenté, on utilisera colordiff pour le rendu sinon diff.<br /><br />En effet, un pipe avec less (sans l'option -R ou la variable LESS définie à -R) afficherait les caractères d’échappement servant à la colorisation des lignes<br /><br />Cf une page intéressante : <a href="http://unix.stackexchange.com/questions/9957/how-to-check-if-bash-can-print-colors">ici</a>
