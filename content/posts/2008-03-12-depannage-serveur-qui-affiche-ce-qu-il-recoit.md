---
title: "Dépannage: serveur qui affiche ce qu'il reçoit"
date: 2008-03-12T11:38:00+01:00
tags: [ "linux", "apt", "commande", "socat", "port" ]
description: "Voici un utilitaire bien utile pour afficher ce qu'il reçoit"
---
Le serveur affiche ce qu'il reçoit, c'est tout ce qu'il fait.

```text
# installation
sudo apt-get install socat

# lancement du serveur
socat tcp4-listen:1234,reuseaddr,fork stdio

# lancement du client où l'on envoie des données
telnet 127.0.0.1 1234
```