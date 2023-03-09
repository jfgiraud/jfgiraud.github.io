---
title: "Utiliser sort pour trier un tableau"
date: 2008-03-17T10:53:00+01:00
---
Trie les données sur les colonnes 2 et 3.

<pre>jfgiraud@jfgiraud1:~$ printf "D,3,5,D\nA,3,07,A\nB,3,10,B\nC,5,2,C\n"
| sort  -t ',' -k 2n,2n -k 3n,3n

D,3,5,D
A,3,07,A
B,3,10,B
C,5,2,C
</pre>
