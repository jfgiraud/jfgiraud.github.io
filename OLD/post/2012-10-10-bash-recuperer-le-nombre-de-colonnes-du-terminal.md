---
layout: post
title: "bash, récupérer le nombre de colonnes du terminal"
date: "2012-10-10 17:58:00"
tags: tput, printf
---
Pour centrer :


```bash
$ COLUMNS=$(tput cols)
$ title="Hello mister"
$ printf "%*s\n" $(((${#title}+$COLUMNS)/2)) "$title"
                                       Hello mister
```

Ou afficher un séparateur :


```bash
printf -v separator "%*s " $(( $(tput cols) - ${#file} - 5 ))
echo "-- $file ${separator// /-}"
```


