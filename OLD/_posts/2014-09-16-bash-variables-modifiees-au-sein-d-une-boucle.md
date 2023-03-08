---
title: "bash, variables modifiées au sein d'une boucle"
date: "2014-09-16 06:07:00"
---
Il y a quelques temps déjà, je m'étais cassé la tête sur des variables que je modifiais dans une boucle et dont les modifications avaient disparues une fois sorti de celle-ci.

Cela s'expliquait par le fait que les variables étaient dans un sous-processus et non dans le process courrant.

La bonne syntaxe pour modifier des variables au sein d'une boucle while est la suivante :


```
function parse() {
    local command="$1"
    tempf=$(mktemp)
    $command --help 2>&1 | sed -e 's/^[[:space:]]\{16,\}.*//' -e 's/^[[:space:]]*//' | grep -E '^-' | sed -e 's/[[:space:]]\{2,\}.*//' > $tempf
    local longopts=""
    local shortopts=""
    while read line || [[ $line ]];
    do
        required=""
        if grep -Fq '[=' <<< "$line"; then
            required="::"
        elif grep -Fq '=' <<< "$line"; then
            required=":"
        fi
        while read option || [[ $option ]];
        do
            option=${option%%=*}
            option=${option%[}
            if [ ${option:0:2} == '--' ]; then
                if [ -n "$longopts" ]; then
                    longopts="${longopts},"
                fi
                longopts="${longopts}${option:2}${required}"
            else
                shortopts="${shortopts}${option:1}${required}"
            fi
        done < <(echo $line | tr ',' '\n' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]\+.*//')
    done < $tempf
    rm -f $tempf
    echo "-o '$shortopts' -l '$longopts'"
}
```

Il faut passer par <code>done &lt; ...</code> et non <code>... | while</code>
