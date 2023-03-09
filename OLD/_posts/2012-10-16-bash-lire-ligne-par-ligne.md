---
title: "bash, lire ligne par ligne"
date: 2012-10-16T11:36:00+01:00
tags: ["bash", "read", "line"]
---
Pour un fichier :

```bash
$ while read line ; 
do 
  echo $line; 
done < /etc/shells
# /etc/shells: valid login shells
/bin/csh
/bin/sh
/usr/bin/es
/usr/bin/ksh
/bin/ksh
/usr/bin/rc
/usr/bin/tcsh
/bin/tcsh
/usr/bin/esh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/screen
```

Et encore mieux, sur la sortie d'une commande :)


```bash
$ while read line ; 
do 
  echo $line; 
done < <(head -n 3 /etc/shells)
# /etc/shells: valid login shells
/bin/csh
/bin/sh
```

