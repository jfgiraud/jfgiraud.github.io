---
title: "mysql, importer un fichier csv"
date: 2012-07-16T17:30:00+01:00
tags: ["mysql", "import"]
---
Pour charger un fichier csv dans une table on peut utiliser la commande suivante :  

```
mysql> load data infile '/path/to/file.csv' into table mytable character 
set 'utf8' fields terminated by ';' IGNORE 1 lines;
Query OK, 786 rows affected (0.13 sec)
Records: 786  Deleted: 0  Skipped: 0  Warnings: 0
``` 

Ici, le charset est spécifié et la première ligne du fichier CSV est ignorée (titre des colonnes).
