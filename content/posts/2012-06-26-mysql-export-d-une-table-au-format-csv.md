---
title: "mysql, export d'une table au format csv"
date: 2012-06-26T14:20:00+01:00
tags: ["mysql", "export"]
---
Il est possible d'exporter le contenu d'une table dans un fichier via une requête mysql. Voici la syntaxe :  

```
SELECT champ1,champ2 FROM matable INTO OUTFILE 'lefichier.csv' 
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"';
```
