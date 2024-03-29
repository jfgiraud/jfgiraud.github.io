---
title: "bash, séquences"
date: 2012-09-11T13:13:00+01:00
---

Pour obtenir une suite de nombre qui font partie d'une séquence, il y a la commande `seq`. Il existe aussi une manière de le faire directement en bash en utilisant une expression du genre {x..y[..inc]}.  <code><pre>

```bash
$ for i in {1..30..2}; do echo $i; done
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
$ seq 1 2 30
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
```

Attention toutefois, si les bornes sont définies dans des variables, il faudra un petit coup d'évaluation :  

```
$ for i in $(eval echo "{$a..$b}"); do echo $i; done
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
```