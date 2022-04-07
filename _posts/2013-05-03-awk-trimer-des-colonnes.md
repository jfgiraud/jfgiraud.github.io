---
layout: post
title: "awk, trimer des colonnes"
date: "2013-05-03 03:20:00"
---

```
$ printf "two columns\t:  with values  to trim\n" | awk -F ':' '{gsub(/^[[:space:]]+|[[:space:]]+$/,"",$1); gsub(/^[[:space:]]+|[[:space:]]+$/,"",$2); print $1":"$2}'
two columns:with values  to trim
```

<div style="height: 0; overflow: hidden;">awk re regex gsub trim strip space { }</div>
