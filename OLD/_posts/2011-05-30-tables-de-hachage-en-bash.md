---
title: "tables de hachage en bash"
date: 2011-05-30T14:27:00+01:00
tags: ["hash", "declare", "animals", "key", "value", "hachage", "iterate"]
---
Voici comment déclarer une table de hachage en bash et itérer sur ses clés pour récupérer les valeurs :


```bash
declare -A animals
animals=( ["moo"]="cow" ["miaou"]="cat" )

animals['dog']='wouaf'

for i in "${!animals[@]}"
do
  echo "key  : $i"
  echo "value: ${animals[$i]}"
done

echo "There are ${#animals[@]} animals."
```
