---
title: "bash, lister les commandes disponibles"
date: 2012-08-03T10:41:00+01:00
---
Pour lister les commandes disponibles, on peut utiliser la commande bash intégrée compgen: 

 

- compgen -c liste la liste de toutes les commandes que l'on peut exécuter - compgen -a liste la liste de tous les alias que l'on peut exécuter - compgen -b liste la liste de toutes les commandes intégrées (built-in) que l'on peut exécuter - compgen -k liste la liste de tous les mots clés que l'on peut exécuter (if/then...) 

 Sur ma machine, la répartition des commandes en fonction de la première lettre...  <pre><code>
$ compgen -c | cut -c 1 | sort | uniq -c | sort -nr | column
    392 p     122 f      61 h      12 k       1 N
    359 _     118 r      37 w       8 V       1 M
    222 m     115 i       3 7       6 y       1 G
    222 g     114 u      33 j       6 q       1 C
    207 s     114 a      30 v       3 [       1 }
    154 x      96 t      25 z       2 X       1 {
    143 c      95 b      22 o       2 H       1 ]
    131 d      78 n       2 2       2 .       1 !
    130 l      77 e       1 4       1 P       1 :
</code></pre>
