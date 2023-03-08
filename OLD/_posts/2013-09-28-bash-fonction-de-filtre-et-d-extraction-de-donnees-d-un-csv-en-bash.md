---
title: "bash, fonction de filtre et d'extraction de données d'un csv en bash"
date: "2013-09-28 09:56:00"
---
J'ai mis à disposition sur mon repository git un utilitaire [csv-functions.sh](https://github.com/jfgiraud/config/tree/master/home/jfgiraud/bin/csv-functions.sh) pour filtrer et extraire des données d'un fichier csv en bash.

Voici un exemple d'utilisation :


```
csvexample() {
    (cat <<-EOF
lastname;firstname;birth;number_of_child
doe;john;1975;2
doe;foo;1990;1
doe;jane;1985;2
EOF
) > example.csv
    declare -A persons
    csvindexes persons example.csv
    for tuple in $(csvvalues example.csv | csvfilter persons "lastname=doe" "birth=1985" "number_of_child=2")
    do
	eval $(csvextract persons $tuple "vara=lastname" "varb=firstname" "varc=birth" "vard=number_of_child")
	echo "vara=$vara"
	echo "varb=$varb"
	echo "varc=$varc"
	echo "vard=$vard"
    done
    rm -f example.csv
}
```

avec son résultat :


```
$ bash csv-functions.sh 
vara=doe
varb=jane
varc=1985
vard=2
```
