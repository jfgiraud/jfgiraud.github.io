---
layout: post
title: "ssh, local forwarding"
date: "2020-10-08 09:24:00"
tags: ssh forwarding
---
Exemple :  
- depuis le poste local, lancer firefox et aller sur http://127.0.0.1:7533
- les requêtes transitent dans le tunnel SSH (user@example.com)
- à la sortie, elles partent sur le host 127.0.0.1 port 7575 où tourne le fitnesse

```
ssh user@example.com -N -L 7533:127.0.0.1:7575
```

