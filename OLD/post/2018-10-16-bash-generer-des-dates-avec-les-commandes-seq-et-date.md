---
layout: post
title: "bash, générer des dates avec les commandes seq et date"
date: "2018-10-16 11:28:00"
tags: commande seq date
---
Parfois il peut être utile d'avoir une liste de dates pour appeler un script particulier.

Cette liste peut être générée à partir des commandes `seq` et `date` comme dans l'exemple ci-dessous.


```bash
$ for i in $(seq 0 5); do date -d "20180705 $i day" +'%Y%m%d'; done
20180705
20180706
20180707
20180708
20180709
20180710
$ for i in $(seq 0 5); do date -d "20180705 $i day ago" +'%Y%m%d'; done
20180705
20180704
20180703
20180702
20180701
20180630
```
