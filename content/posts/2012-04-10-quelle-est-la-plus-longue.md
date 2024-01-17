---
title: "Quelle est la plus longue ligne"
date: 2012-04-10T11:12:00+01:00
tags: ["commande", "wc"]
---

La plus longue ligne peut être donnée via l'option méconnue -L de la commande wc...

```
$ find . -name '*.java' | sed -e 's/.*\///' | wc -L
73
```
