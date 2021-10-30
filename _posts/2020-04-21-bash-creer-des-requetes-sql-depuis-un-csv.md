---
layout: post
title: "bash, créer des requêtes sql depuis un csv"
date: "2020-04-21 18:39:00"
---
Il y a quelques temps, j'avais utilisé la commande `awk` pour générer des requêtes sql depuis un fichier CSV.

Dans le cas présent, j'utilise simplement un script bash.

Au final, la solution bash -bien que plus verbeuse- me semble plus lisible à lire et modifier.

```
#!/bin/bash


fichier=~/Téléchargements/groupmotifs.csv
tail -n +2 $fichier | tr -d $'\r' | while IFS=$'\n' read line || [[ $line ]]
do
    IFS=';' read id name type_group nas <<< "$line"
    cat <<EOF
insert into group_motifs (id, name, type_group, nas) values ($id, "$name", "$type_group", "$nas") on duplicate key update nas="$nas", type_group="$type_group", name="$name";
EOF
done > requetes.sql

fichier=~/Téléchargements/motifsroutage.csv
tail -n +2 $fichier | tr -d $'\r' | while IFS=$'\n' read line || [[ $line ]]
do
    IFS=';' read id motif_routage libelle mot motif_sup id_group_motif nas <<< "$line"
    if [[ -z "$mot" || "$mot" == "NULL" ]]; then mot="NULL"; else mot="\"$mot\""; fi
    if [[ -z "$id_group_motif" || "$id_group_motif" == "NULL" ]]; then id_group_motif="NULL"; fi
    cat <<EOF
replace into listeMotifsRoutage (id, motif_routage, libelle, mot, motif_sup, id_group_motif, nas) values ($id, "$motif_routage", "$libelle", $mot, "$motif_sup", $id_group_motif, "$nas");
EOF
done >> requetes.sql
```

