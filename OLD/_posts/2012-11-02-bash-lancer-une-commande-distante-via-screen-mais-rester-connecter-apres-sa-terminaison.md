---
title: "bash, lancer une commande distante via screen mais rester connecter après sa terminaison"
date: 2012-11-02T16:05:00+01:00
---

```
screen -t "Lancer une commande sur machine distante puis passer sur le prompt bash à la fin de celle-ci" ssh -X machine_distante.example.com "(tail -f /usr2/logs/local7.log; bash)"
```
