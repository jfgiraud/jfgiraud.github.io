---
title: "bash, renverser un flux ligne à ligne"
date: 2013-12-07T10:07:00+01:00
tags: ["bash", "commande", "seq"]
---
Voici une commande que je ne connaissais pas avant le petit déjeuner...


```
$ for i in $(seq 1 10); do echo $i; done
1
2
3
4
5
6
7
8
9
10
$ for i in $(seq 1 10); do echo $i; done | tac
10
9
8
7
6
5
4
3
2
1
```

Fallait la découvrir celle-là ;) tac, la soeur de cat à l'envers...
