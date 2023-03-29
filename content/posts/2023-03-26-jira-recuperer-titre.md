---
title: "jira, récupérer le titre d'une fiche"
date: 2023-03-26T07:10:00+01:00
tags: [ "jira", "api" ]
description: "Voici comment je récupère le titre d'une fiche Jira pour le copier/coller dans mes changelogs"
---

Dans mon `~/.bashrc` :

```
#!/bin/bash

function cl() {
    local n=$1
    TOKEN=$(grep -F -A4 "machine portail.example.com" ~/.netrc | grep -E '^account ' | cut -d ' ' -f 2)
    mapfile -t table < <(curl -s -X GET -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://portail.example.com/rest/api/latest/issue/MSVI-$n | jq '.key,.fields.summary')
    f=$(echo ${table[0]} | tr -d '"')
    t=$(echo ${table[1]} | sed -e 's#^"##' -e 's#"$##' | sed -e 's#\\"#"#g')
    t=$(echo $t | sed -e 's/^\[[^\]+]\s*//')
    t=$(echo $t | tr -s ' ')
    shift 1
    echo "$f: $t" | xclip -sel c
    xclip -o -sel c
    echo "Copié dans le presse papier"
}

```

Dans mon `~/.netrc` (seules les entrées `machine`/`account` sont utilisés dans la fonction `cl`) :

```
machine portail.example.com
login <your-jira-login>
account <your-jira-token>
password <your-password>
```

A l'usage :

```
$ cl 1971
MSVI-1971: Ceci est le titre de la fiche modifié volontairement
Copié dans le presse papier
```
