---
layout: post
title: "Archlinux, imprimante samung ML-1865"
date: "2013-04-21 14:15:00"
---
Tout d'abord, il faut installer yaourt (cf http://archlinux.fr/yaourt)<br /><br />Ensuite, utiliser yaourt pour installer les drivers :<br /><br />yaourt -S samsung-ml1860<br /><br />Dans cups (cf install de cups) sur 127.0.0.1, installer ensuite l'imprimante avec le fichier PPD suivant (connexion en USB)<br /><br /><a href="http://pastebin.com/KeZFgAG1">http://pastebin.com/KeZFgAG1</a><br /><br />Imprimez ensuite votre page de test :)<br /><br />N'oubliez pas :<br /><br />systemctl start cups<br /><br />systemctl enable cups