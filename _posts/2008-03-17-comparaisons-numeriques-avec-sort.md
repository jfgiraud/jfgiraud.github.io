---
layout: post
title: "Comparaisons numériques avec sort"
date: "2008-03-17 10:35:00"
---
jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -g
1
5.0
2e1
21
jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -n
1
2e1
5.0
21
jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort
1
21
2e1
5.0
