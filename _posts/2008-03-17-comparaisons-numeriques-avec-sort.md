---
layout: post
title: "Comparaisons numériques avec sort"
date: "2008-03-17 10:35:00"
---
jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -g<br />1<br />5.0<br />2e1<br />21<br />jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -n<br />1<br />2e1<br />5.0<br />21<br />jfgiraud@jfgiraud1:~$ printf "1 21 5.0 2e1" | tr " " "\n" | sort<br />1<br />21<br />2e1<br />5.0
