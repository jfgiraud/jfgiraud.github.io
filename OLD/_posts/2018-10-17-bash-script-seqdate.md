---
title: "bash, script seqdate"
date: "2018-10-17 10:07:00"
tags: commande date seq
---
Script réutilisable pour générer des dates avec `date` et `seq`


```bash
#!/bin/bash

usage() {
    local msg="$1"
    if [[ -n "$msg" ]]; then
    echo $msg
    fi
    echo "usage: $0 <FROM=YYYY-MM-DD> <TO=YYYY-MM-DD>" >&2
    exit 1
}

if [[ "$#" -ne 2 ]]; then
    usage 
fi

FORMAT="%Y-%m-%d"
FROM=$(date --d "$1" +"$FORMAT")
TO=$(date --d "$2" +"$FORMAT")

if [[ "$FROM" > "$TO" ]]; then
    read FROM TO <<< "$TO $FROM"
fi

echo $FROM
while [[ "$FROM" != "$TO" ]]; do
    FROM=$(date -d "$FROM 1 day" +"$FORMAT")
    echo $FROM
done
```


```bash
$ ./seqdate.sh 2018-08-01 2018-08-10
2018-08-01
2018-08-02
2018-08-03
2018-08-04
2018-08-05
2018-08-06
2018-08-07
2018-08-08
2018-08-09
2018-08-10
```
