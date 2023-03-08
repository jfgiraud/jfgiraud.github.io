---
title: "bash, voir autour des occurences avec grep..."
date: "2012-10-12 12:18:00"
tags: grep
---

Voici comment on peut voir les lignes proches des occurences matchées par `grep`

```bash 
$ grep -C 5 Msg_Motif_Reit etc/centralisation.yml 
      ref_db: desc
      ref_table: motif
      select_column: motifId
      where_column: motifName

  - name: Msg_Motif_Reit
    comment: "nom de l'enveloppe associée au micro motif utilisé pour la reiteration"
    value_regex: '[\w/]+'

  - name: reit_ACC
    comment: "détermine si le client est en reiteration"
```

Avec l'option :
- `A` : affiche les lignes après l'occurence trouvée (after)
- `B` : affiche les lignes avant l'occurence trouvée (before)
- `C` : affiche les lignes avant et après l'occurence trouvée


