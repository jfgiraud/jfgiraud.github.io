---
title: "linux, teams"
date: 2024-01-12T07:10:00+01:00
tags: [ "linux", "teams", "x11", "wayland" ]
description: "Partage de bureau impossible"
---

Un collègue vient de changer de PC linux et il n'arrivait plus à partager son écran via teams (via chrome).

Je lui ai repassé mon `/var/cache/apt/archives/teams_1.5.00.10453_amd64.deb` mais cela n'a pas changé grand chose

Le choix ne lui était plus proposé.

En cherchant sur google et particulièrement sur youtube, le problème vient de l'utilisation de Wayland (https://fr.wikipedia.org/wiki/Wayland) 

Pour se faire vérifier si c'est bien Wayland qui est utilisé dans votre terminal

Dans mon cas, c'est X11 :
```
$ echo $XDG_SESSION_TYPE
x11
```

Si c'est Wayland, vous pouvez suivre la procédure ci-dessous et le problème devrait être résolu en rebootant

Source: 

Fix MS Teams / zoom meeting sharing problem in Ubuntu (Linux)
https://youtu.be/4oaQYTwSD3k?si=w2MYIAkn7O8WrUgK
