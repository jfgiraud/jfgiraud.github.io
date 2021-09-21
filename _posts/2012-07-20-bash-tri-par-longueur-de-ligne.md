---
layout: post
title: "bash, tri par longueur de ligne"
date: "2012-07-20 11:32:00"
---
La commande sort ne permet pas de trier en fonction de la longueur des lignes. C'est dommage mais on peut utiliser awk, combiné avec sort pour avoir le même résultat.  <code><pre><br />$ cat /usr/share/dict/words <br />   | awk '{ print length(), $0 | "sort -n" }' <br />   | cut -d ' ' -f 2-<br /></pre></code>
