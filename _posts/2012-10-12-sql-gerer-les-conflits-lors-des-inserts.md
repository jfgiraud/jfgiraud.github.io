---
layout: post
title: "sql, gérer les conflits lors des inserts"
date: "2012-10-12 13:28:00"
---
Lors d'un insert, si la clé primaire existe déjà, il est possible de faire un traitement comme dans l'exemple ci-dessous.<br /><br /><script src="http://pastebin.com/embed_js.php?i=sR0pSAh8"></script><br /><br />Ici, on tente de peupler la table enveloppesTTS avec des valeurs.<br /><br />Si l'entrée n'existe pas, on la crée.<br /><br />Sinon on met à jour un champ de cette table uniquement si sa valeur n'est pas déjà renseigné.<br /><br /><div style="height: 0; overflow: hidden;">mysql, on duplicate key, insert into, values, select, if, tts</div>