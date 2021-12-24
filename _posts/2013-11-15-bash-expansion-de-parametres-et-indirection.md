---
layout: post
title: "bash, expansion de paramètres et indirection "
date: "2013-11-15 09:40:00"
---
Aujourd'hui, je viens de découvrir l'indirection de paramètres en bash.

La syntaxe est la suivante : ${!PARAMETER}

L'expansion ne donne pas la valeur du paramètre lui même mais la valeur du paramètre dont le nom est contenu dans PARAMETER.

<script src="https://pastebin.com/embed_js/bRT22fTD"></script>

Cela permet de faire de jolies choses comme ceci en s'abstrayant d'eval...

<script src="https://pastebin.com/embed_js/QqLJJqji"></script>

Ci-dessous une documentation bien claire sur l'expansion des paramètres en bash

[http://wiki.bash-hackers.org/syntax/pe](http://wiki.bash-hackers.org/syntax/pe)


