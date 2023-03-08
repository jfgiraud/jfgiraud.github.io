---
layout: post
title: "mysql, importer un fichier csv"
date: "2012-07-16 17:30:00"
---
Pour charger un fichier csv dans une table on peut utiliser la commande suivante :  <pre><code>
mysql> load data infile '/path/to/file.csv' into table mytable character 
set 'utf8' fields terminated by ';' IGNORE 1 lines;
Query OK, 786 rows affected (0.13 sec)
Records: 786  Deleted: 0  Skipped: 0  Warnings: 0
</code></pre> Ici, le charset est spécifié et la première ligne du fichier CSV est ignorée (titre des colonnes).
