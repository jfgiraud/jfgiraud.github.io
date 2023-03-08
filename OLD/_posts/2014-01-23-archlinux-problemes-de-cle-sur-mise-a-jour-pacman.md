---
title: "archlinux, problèmes de clé sur mise à jour pacman"
date: "2014-01-23 08:56:00"
---
Parfois, lors d'une mise à jour ou tentative d'installation d'un paquet, une erreur de clé corrompue survient.

Il suffit simplement de mettre à jour les clés de son trousseau comme dans l'exemple ci-dessous et de relancer la mise à jour.

Ensuite, ça roule ma poule :) 


```
$ pacman -Syu
...
error: i3-wm: signature from "Thorsten Töpper <atsutane@freethoughts.de>" is unknown trust
error: failed to commit transaction (invalid or corrupted package (PGP signature))
...

 $ pacman-key --refresh-keys
 $ pacman -Syh
```
