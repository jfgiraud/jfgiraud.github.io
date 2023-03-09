---
title: "mysql, n'afficher que les vraies tables"
date: 2012-08-07T11:49:00+01:00
---
[//]: # (TODO: virer les code pre)

Lorsque l'on utilise plusieurs bases de données, il arrive que l'on crée des vues d'une base vers une autre base...

La commande `show tables` n'est pas suffisante pour distinguer les tables des vues... 

Mais voilà, on peut associer l'option full et compléter d'un where pour récupérer ce que l'on souhaite :  

```
mysql> show full tables where Table_type='BASE TABLE';
``` 

où Table_type peut être : 
- `BASE TABLE` 
- `VIEW` 


