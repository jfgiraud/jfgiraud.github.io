---
title: "bash, uniformisation de numéros de version"
date: "2020-04-23 19:21:00"
tags: linux bash numéros versions version numéro
---
Sur notre projet, les numéros de version des lots s'appellent des GOROCO. 

Ils regroupent tout un tas d'applicatifs ayant chacun leur propres numéros de version (format x.y.z).

Ils peuvent être saisis de différentes manières, avec des 0, sans 0... du coup pour uniformiser les valeurs, j'ai réussi à trouver les commandes bash pour les avoir sur 1 caractère si possible (GOROCO) ou bien sur 2 (GOOROOCOO).

```
#!/bin/bash

function uniformize() {
    local GOROCO="$1"
    BEFORE="$GOROCO"
    GOROCO=$(echo $GOROCO | sed -E 's/(G|R|C|P)0([0-9])/\1\2/g')
    GOOROOCOO=$(echo $GOROCO | sed -e 's/\([RCP]\)/\n\1/g' -e 's/\<\(.\)\([0-9]\)\>/\10\2/g' | tr -d '\n')
    printf "$BEFORE\t$GOROCO\t$GOOROOCOO\n"
}

for v in G2R01C0 G0R1C20 G10R5C3 G2R3C01 G02R03C05; do
    uniformize $v
done
```


```
G2R01C0	G2R1C0	G02R01C00
G0R1C20	G0R1C20	G00R01C20
G10R5C3	G10R5C3	G10R05C03
G2R3C01	G2R3C1	G02R03C01
G02R03C05	G2R3C5	G02R03C05
```

