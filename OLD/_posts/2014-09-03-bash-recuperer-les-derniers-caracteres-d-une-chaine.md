---
title: "Bash, récupérer les derniers caractères d'une chaine"
date: "2014-09-03 14:33:00"
---
On connaissait ${s:2} pour récupérer à partir du 3e caractère depuis le début de la chaîne... Mais à partir de la fin ???


```
$ s='abcde'
$ echo ${s: -2}
de
```

Fallait penser à mettre un espace... C'était bien caché ;)
