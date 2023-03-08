---
layout: post
title: "sed, garder les lignes qui matchent un pattern tout en faisant un remplacement"
date: "2019-01-15 16:38:00"
tags: commande cpuinfo
---

```
$ cat /proc/cpuinfo | sed -rn 's/(fpu.*): (\w+)/\1 \2/gp'
fpu		 yes
fpu_exception	 yes
fpu		 yes
fpu_exception	 yes
fpu		 yes
fpu_exception	 yes
fpu		 yes
fpu_exception	 yes
```

L'option `-n` permet de ne pas afficher les lignes tandis que l'ajout de `/p` indique d'afficher lors d'un matchage.
