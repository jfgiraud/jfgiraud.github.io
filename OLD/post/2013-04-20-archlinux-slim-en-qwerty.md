---
layout: post
title: "Archlinux, slim en qwerty"
date: "2013-04-20 09:17:00"
---
En installant archlinux, mon terminal en mode console était bien en mode azerty.

Cependant, dans le login manager SLIM, le texte frappé était en qwerty :/

La ligne suivante insérée insérée dans le .xsession ou .xinitrc n'a d'effet qu'une fois identifié.


```
$ cat .xsession 
xset dpms force on
xset s off
xset -b
setxkbmap -option terminate:ctrl_alt_bksp
export AWT_TOOLKIT=XToolkit
xsetroot -solid "#333333"
setxkbmap fr
exec i3
```

Pour que X passe en azerty, j'ai ajouté le fichier suivant :


```
$ cat /etc/X11/xorg.conf.d/10-keyboard.conf 
Section "InputClass"
    Identifier             "Keyboard Defaults"
    MatchIsKeyboard        "yes"
    Option                 "XkbLayout" "fr"
EndSection
```

Dès lors, X se retrouve en azerty :)

<div style="height: 0; overflow: hidden;">Section "InputClass"
    Identifier             "Keyboard Defaults"
    MatchIsKeyboard        "yes"
    Option                 "XkbLayout" "fr"
EndSection
setxkbmap fr</div>
