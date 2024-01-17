---
title: "mysqlimport"
date: 2012-05-04T15:41:00+01:00
tags: ["mysqlimport"]
---
Le fichier doit porter le nom de la table à l'extension près.  Ici les options utilisées sont : 
- `--delete` pour vider la table avant l'import
- `--fields-terminated-by` pour le séparateur entre les champs
- `--lines-terminated-by` pour le caractère de fin de ligne (ici DOS/WINDOWS) 

```
mysqlimport --fields-terminated-by=\; --lines-terminated-by="\\r\\n" -v --delete -utest -ptest -hlocalhost BASE TABLE.csv
```
