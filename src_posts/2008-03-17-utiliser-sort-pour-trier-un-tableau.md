---
layout: post
title: "Utiliser sort pour trier un tableau"
date: "2008-03-17 10:53:00"
---
Trie les données sur les colonnes 2 et 3.<br /><br /><pre>jfgiraud@jfgiraud1:~$ printf "D,3,5,D\nA,3,07,A\nB,3,10,B\nC,5,2,C\n"<br />| sort  -t ',' -k 2n,2n -k 3n,3n<br /><br />D,3,5,D<br />A,3,07,A<br />B,3,10,B<br />C,5,2,C<br /></pre>
