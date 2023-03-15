---
title: "at, commande"
date: 2021-12-07T10:07:00+01:00
tags: [ "at", "commande" ]
description: "Exécutez une commande dans sed"
---

La commande `at` permet de lancer une commande dans le futur sans passer par une crontab.

Voici un exemple :

```
$ at now + 1 minute <<EOF
echo Hello >> toto
EOF

warning: commands will be executed using /bin/sh
job 4 at Tue Dec  7 11:41:00 2021
$ atq
4	Tue Dec  7 11:41:00 2021 a jfgiraud
$ cat toto
Hello
```

Ne gère pas les secondes, utiliser sleep
