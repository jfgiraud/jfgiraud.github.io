---
layout: post
title: "python, faire en sorte que stdin/stdout lisent et écrivent en binaire"
date: "2012-10-10 13:34:00"
---
J'ai écrit un petit programme qui s'inspire de cut en python.

La lecture et l'écriture pouvant se faire sur l'entrée/sortie standard (sources [ucut](https://github.com/jfgiraud/tools/blob/master/ucut)), j'avais des problèmes de "'ascii' codec can't decode byte"...

Pour y remédier, j'ai "transformé" les flux standard (mode texte) en flux binaires de la manière suivante :

<script src="https://pastebin.com/embed_js/47Nkp7Yj"></script>

<div style="height: 0; overflow: hidden;">python, binary, os, fileno</div>
