---
title: "awk, créer des requêtes SQL depuis un fichier csv"
date: 2012-10-11T16:31:00+01:00
tags: ["awk", "fs", "insert into table"]
---
Par exemple :

```
$ cat masscomment.csv | tail -n +2 | awk 'BEGIN {FS=";" } ; { print "insert into descriptions (\""$1"\", \""$2"\", \""$3"\", \""$4"\");"}' | head
insert into descriptions ("3900configb", "Parametres", "description", "Descriptif du paramètre");
insert into descriptions ("3900configb", "Parametres", "valeur", "Valeur du paramètre");
```

