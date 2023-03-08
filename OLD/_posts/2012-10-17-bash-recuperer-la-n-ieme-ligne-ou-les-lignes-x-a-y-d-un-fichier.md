---
title: "bash, récupérer la n-ième ligne ou les lignes x à y d'un fichier"
date: "2012-10-17 11:05:00"
tags: awk, sed
---
On peut utiliser `awk` avec `NR` (numéro de ligne tout fichier confondus) ou `FNR` (numéro de ligne du fichier) :


```bash 
### afficher la 3e ligne

$ awk 'NR==3 { print; exit; }' /etc/passwd
bin:x:2:2:bin:/bin:/bin/sh

### afficher les lignes 3 à 6

$ awk '3<=NR && NR<=6 { print; }' /etc/passwd
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
```

Ou bien avec sed : 


```bash
$ cat /etc/passwd | sed '3!d'
bin:x:2:2:bin:/bin:/usr/sbin/nologin
$ cat /etc/passwd | sed '3,6!d'
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
```

En bonus, 10 astuces awk :

[http://www.catonmat.net/blog/ten-awk-tips-tricks-and-pitfalls/](http://www.catonmat.net/blog/ten-awk-tips-tricks-and-pitfalls/)
