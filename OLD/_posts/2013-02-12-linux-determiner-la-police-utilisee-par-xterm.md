---
layout: post
title: "Linux, déterminer la police utilisée par xterm"
date: "2013-02-12 15:23:00"
---
On peut utiliser appres qui affiche la liste des ressources utilisées par xterm.

Dans mon cas :


```
$ pacman -S xorg-appres
$ appres XTerm | grep -i font | grep -vi label
*tek4014*fontLarge:     9x15
*tek4014*font2: 8x13
*tek4014*font3: 6x13
*tek4014*fontSmall:     6x10
*VT100.utf8Fonts.font5: -misc-fixed-medium-r-normal--18-120-100-100-c-90-iso10646-1
*VT100.utf8Fonts.font3: -misc-fixed-medium-r-normal--14-130-75-75-c-70-iso10646-1
*VT100.utf8Fonts.font:  -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso10646-1
*VT100.utf8Fonts.font4: -misc-fixed-medium-r-normal--13-120-75-75-c-80-iso10646-1
*VT100.utf8Fonts.font2: -misc-fixed-medium-r-normal--8-80-75-75-c-50-iso10646-1
*VT100.utf8Fonts.font6: -misc-fixed-medium-r-normal--20-200-75-75-c-100-iso10646-1
*VT100.font5:   9x15
*VT100.font3:   6x10
*VT100.font1:   nil2
*VT100.font4:   7x13
*VT100.font2:   5x7
*VT100.font6:   10x20
*IconFont:      nil2
```


Donc, si je veux utiliser la même police dans un autre terminal, je n'ai plus qu'à utiliser : -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso10646-1

<div style="height: 0; overflow: hidden;">appres pacman xterm</div>

