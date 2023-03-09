---
title: "Linux Mint Cinnamon & Samsung ML-1865 (2)"
date: 2012-09-04T22:26:00+01:00
---
En installant l'imprimante, le daemon smfpd se met en place et démarre automatiquement à chaque allumage.

Ce daemon n'est utile que dans le cas où l'imprimante Samsung est connectée à un port parallèle... Ce qui n'est pas le cas de ma ML-1865 !

Or ce daemon est gourmand en ressources et donc la batterie du portable diminue plus vite :(

Pour l'économiser, editer le fichier /etc/inid.d/smfpd et décommenter la ligne "exit 0". Le programme se terminera aussitôt lancé. Cette modification sera prise en compte au prochain démarrage. 
