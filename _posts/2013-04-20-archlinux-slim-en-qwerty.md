---
layout: post
title: "Archlinux, slim en qwerty"
date: "2013-04-20 09:17:00"
---
En installant archlinux, mon terminal en mode console était bien en mode azerty.<br /><br />Cependant, dans le login manager SLIM, le texte frappé était en qwerty :/<br /><br />La ligne suivante insérée insérée dans le .xsession ou .xinitrc n'a d'effet qu'une fois identifié.<br /><br /><script src="http://pastebin.com/embed_js.php?i=63999Zwf"></script><br /><br />Pour que X passe en azerty, j'ai ajouté le fichier suivant :<br /><br /><script src="http://pastebin.com/embed_js.php?i=cXFSCFpc"></script><br /><br />Dès lors, X se retrouve en azerty :)<br /><br /><div style="height: 0; overflow: hidden;">Section "InputClass"<br />    Identifier             "Keyboard Defaults"<br />    MatchIsKeyboard        "yes"<br />    Option                 "XkbLayout" "fr"<br />EndSection<br />setxkbmap fr</div>