---
title: "bash, savoir si stdout fait référence à un terminal"
date: 2012-10-12T15:53:00+01:00
tags: ["diff", "colordiff"]
---
Pour savoir si la sortie standard pointe sur un terminal, on peut utiliser l'opérateur "-t" en bash.


```bash
diffutil=diff
if [ -t 1 ]; then
        if which colordiff > /dev/null; then
                diffutil=colordiff
        fi
fi
```

Dans le cas présenté, on utilisera colordiff pour le rendu sinon diff.

En effet, un pipe avec less (sans l'option `-R` ou la variable LESS définie à `-R`) afficherait les caractères d’échappement servant à la colorisation des lignes

Cf une page intéressante : [ici](http://unix.stackexchange.com/questions/9957/how-to-check-if-bash-can-print-colors)
