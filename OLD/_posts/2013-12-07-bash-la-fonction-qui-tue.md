---
title: "bash, la fonction qui tue..."
date: "2013-12-07 10:01:00"
---
Voici une fonction qui tue... et simplifie la vie en ligne de commandes !


```
function ..() {
    ## .. <nombre> remonte de <nombre> repertoires
    ## .. /<chaine> remonte jusqu'a ce qu'un repertoire contient <chaine> dans son nom
    local level=$1
    if [[ ! "$level" =~ / ]]; then
	while [ $level -gt 0 ]; do
	    cd .. || break
	    level=$(($level-1))
	done
    else
	level=${level:1}
	local curdir=$(pwd)
	IFS='/' read -ra ADDR <<< "$curdir"
	for (( i = ${#ADDR[@]}-1; i>0; i-- )); do
	    if [[ "${ADDR[$i]}" =~ "$level" ]]; then
		break
	    fi
	    cd ..
	done
    fi
}
```

Les commentaires parlent d'eux-mêmes pour dire ce que fait la fonction ..

A vos .bashrc !!!
