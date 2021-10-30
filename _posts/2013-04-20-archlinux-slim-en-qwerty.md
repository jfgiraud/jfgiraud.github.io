---
layout: post
title: "Archlinux, slim en qwerty"
date: "2013-04-20 09:17:00"
---
En installant archlinux, mon terminal en mode console était bien en mode azerty.

Cependant, dans le login manager SLIM, le texte frappé était en qwerty :/

La ligne suivante insérée insérée dans le .xsession ou .xinitrc n'a d'effet qu'une fois identifié.

<script src="http://pastebin.com/embed_js.php?i=63999Zwf"></script>

Pour que X passe en azerty, j'ai ajouté le fichier suivant :

<script src="http://pastebin.com/embed_js.php?i=cXFSCFpc"></script>

Dès lors, X se retrouve en azerty :)

<div style="height: 0; overflow: hidden;">Section "InputClass"
    Identifier             "Keyboard Defaults"
    MatchIsKeyboard        "yes"
    Option                 "XkbLayout" "fr"
EndSection
setxkbmap fr</div>
