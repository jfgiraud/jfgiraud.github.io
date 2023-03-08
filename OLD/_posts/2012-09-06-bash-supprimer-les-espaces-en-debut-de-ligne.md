---
title: "bash, supprimer les espaces en début de ligne"
date: "2012-09-06 10:33:00"
tags: awk space espace trim strip
---
Pour supprimer les espaces en début de ligne...  


```bash
$ cat fichier | sed -e 's/^[ \t]*//g'
$ cat fichier | sed -re 's/^[[:space:]]*//g'
```

ou alors avec awk


```bash
$ cat fichier | awk -F ':' '{ gsub(/^[[:space:]]+$/,"",$2); print $2; }'
```

