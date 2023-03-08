---
title: "sed, prefixer sur la première ligne et suffixer sur la dernière ligne sans modifier les lignes entre"
date: "2016-12-28 15:01:00"
tags: commande sed préfixer suffixer
---

```bash
$ printf "lorem\nipsum\ndolores\nest" | sed -e '1s/^/<</;$s/$/>>/;'
<<lorem
ipsum
dolores
est>>
```
