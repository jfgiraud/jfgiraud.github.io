---
title: "Fichiers, ajout/retrait BOM dans un fichier"
date: 2014-09-14T07:55:00+01:00
tags: ["bom"]
---
Il est possible d'ajouter/retirer le caractère bom en début de fichier en utilisant la commande uconv.


```
UCONV(1)                                       ICU 53.1 Manual                                       UCONV(1)

NAME
       uconv - convert data from one encoding to another

SYNOPSIS
       uconv  [  -h,  -?,  --help  ]  [ -V, --version ] [ -s, --silent ] [ -v, --verbose ] [ -l, --list | -l,
       --list-code code | --default-code | -L, --list-transliterators ] [ --canon ] [ -x transliteration ]  [
       --to-callback callback | -c ] [ --from-callback callback | -i ] [ --callback callback ] [ --fallback |
       --no-fallback ] [ -b, --block-size size ] [ -f, --from-code encoding ] [ -t, --to-code  encoding  ]  [
       --add-signature ] [ --remove-signature ] [ -o, --output file ] [ file...  ]

...
       --add-signature
              Add a U+FEFF Unicode signature character (BOM) if the output charset supports it and  does  not
              add one anyway.

       --remove-signature
              Remove a U+FEFF Unicode signature character (BOM).
```

Exemple d'utilisation : 


```
$ echo a;b > example.csv
$ echo d;e >> example.csv
$ hexdump -C example.csv 
00000000  61 3b 62 0a 64 3b 65 0a                           |a;b.d;e.|
00000008
$ uconv --add-signature example.csv | hexdump -C
00000000  ef bb bf 61 3b 62 0a 64  3b 65 0a                 |...a;b.d;e.|
0000000b
```
