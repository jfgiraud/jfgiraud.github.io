---
title: "Tri de numéros de version"
date: 2011-11-25T14:20:00+01:00
tags: [ "commande", "shell", "sort" ]
description: "Trier des numéros de version"
---

```
$ cat ~/a 
9.1.1
9.4.14
9.4.6
$ export LC_ALL=C ; cat ~/a | sort -t. -n -k1 -k2 -k3
9.1.1
9.4.14
9.4.6
=> pas bon
$ export LC_ALL=fr_FR.UTF-8 ; cat ~/a | sort -t. -n -k1 -k2 -k3
9.1.1
9.4.6
9.4.14
=> bon
$ export LC_ALL=C ; cat ~/a | sort -t. -k1,1n -k2,2n -k3,3n
9.1.1
9.4.6
9.4.14
=> bon
```

Sinon si l'option est disponible (version récente de la commande)

```
cat ~a | sort --version
```
