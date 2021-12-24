---
layout: post
title: "csv, visualiser en ligne de commande"
date: "2020-02-15 10:19:00"
tags: linux bash csv visualiser
---
Voici une commande à ajouter dans son .bashrc afin de visualiser le contenu d'un fichier CSV sans avoir à ouvrir une application spécifique.

```
function lesscsv() {
    local file="$1"
    local sep="${2:-;}"
    column -s$sep -nt "$file" | less -#2 -N -S
}
```


```
lesscsv /usr/share/distro-info/ubuntu.csv ,
```

[//]: # (TODO: migrer image)
<div class="separator" style="clear: both; text-align: center;"><a href="https://4.bp.blogspot.com/-Ug-JYvSjRtc/Xke4R0ha3kI/AAAAAAAAEN8/gkK-gvy7vvAZ29k5wH-C7dQHCB-OSOgTACNcBGAsYHQ/s1600/Capture%2Bdu%2B2020-02-15%2B10-20-49.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-Ug-JYvSjRtc/Xke4R0ha3kI/AAAAAAAAEN8/gkK-gvy7vvAZ29k5wH-C7dQHCB-OSOgTACNcBGAsYHQ/s400/Capture%2Bdu%2B2020-02-15%2B10-20-49.png" width="400" height="248" data-original-width="578" data-original-height="359" /></a></div>
