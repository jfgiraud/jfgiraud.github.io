---
layout: post
title: "sql, gérer les conflits lors des inserts"
date: "2012-10-12 13:28:00"
tags: mysql, on duplicate key, insert into, values, select, if, tts
---
Lors d'un insert, si la clé primaire existe déjà, il est possible de faire un traitement comme dans l'exemple ci-dessous.


```
insert into enveloppesTTS (enveloppe, tts) select enveloppe, '' as tts from enveloppes on duplicate key update enveloppesTTS.tts=if(enveloppesTTS.tts<>'',enveloppesTTS.tts,values(tts));
```

Ici, on tente de peupler la table enveloppesTTS avec des valeurs.

Si l'entrée n'existe pas, on la crée.

Sinon on met à jour un champ de cette table uniquement si sa valeur n'est pas déjà renseigné.

