---
title: "ssh, tester l'état d'une connexion"
date: "2016-07-12 14:18:00"
tags: ssh test
---
Voici un petit code qui permet de tester l'état d'une connexion ssh (avec un timeout de 10s) :


```
ssh -q -o BatchMode=yes -o ConnectTimeout=10 user@example.com exit
# ou:
# timeout -k 10 10 ssh user@example.com exit
res=$?
if [ $res -ne 0 ]; then
	echo Accès KO
else
	echo Accès OK
fi
```
