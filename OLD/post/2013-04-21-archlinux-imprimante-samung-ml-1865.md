---
layout: post
title: "Archlinux, imprimante samung ML-1865"
date: "2013-04-21 14:15:00"
---
Tout d'abord, il faut installer yaourt (cf [http://archlinux.fr/yaourt](http://archlinux.fr/yaourt)

Ensuite, utiliser yaourt pour installer les drivers :

yaourt -S samsung-ml1860

Dans cups (cf install de cups) sur 127.0.0.1, installer ensuite l'imprimante avec le fichier PPD suivant (connexion en USB)

[https://pastebin.com/KeZFgAG1](https://pastebin.com/KeZFgAG1)

Imprimez ensuite votre page de test :)

N'oubliez pas :

systemctl start cups

systemctl enable cups
