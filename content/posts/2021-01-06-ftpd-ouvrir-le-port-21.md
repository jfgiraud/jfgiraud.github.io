---
title: "ftpd, ouvrir le port 21"
date: 2021-01-06T10:56:00+01:00
tags: ["ftp", "firewall"]
---

En installant mon nouveau poste, j'ai eu un souci lors de la reconfiguration de mon scanner.

La résolution de nom se faisait mais le scanner n'arrivait pas à se connecter au serveur ftp fraichement installé.

Le telnet sur le port 21 bloquait...

La solution était d'ouvrir le port 21 avec la commande suivante :

```text
$ sudo ufw allow in ftp
La règle a été ajoutée
La règle a été ajoutée (v6)
```