---
layout: post
title: "python, faire en sorte que stdin/stdout lisent et écrivent en binaire"
date: "2012-10-10 13:34:00"
---
J'ai écrit un petit programme qui s'inspire de cut en python.<br /><br />La lecture et l'écriture pouvant se faire sur l'entrée/sortie standard (sources <a href="https://github.com/jfgiraud/tools/blob/master/ucut">ucut</a>), j'avais des problèmes de "'ascii' codec can't decode byte"...<br /><br />Pour y remédier, j'ai "transformé" les flux standard (mode texte) en flux binaires de la manière suivante :<br /><br /><script src="http://pastebin.com/embed_js.php?i=47Nkp7Yj"></script><br /><br /><div style="height: 0; overflow: hidden;">python, binary, os, fileno</div>