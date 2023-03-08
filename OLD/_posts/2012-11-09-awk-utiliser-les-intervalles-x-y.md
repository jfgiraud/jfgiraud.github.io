---
title: "awk, utiliser les intervalles {x,y}"
date: "2012-11-09 11:46:00"
---
Pour utiliser les intervalles avec awk, il suffit de rajouter l'option --re-interval


```
$ date +'%A  %e %B  %Y     %H:%M' | awk --re-interval '{ gsub(/[[:space:]]{2,}/, " ", $0); print $0 }'
vendredi 9 novembre 2012 11:45
```

<div style="height: 0; overflow: hidden;">awk re regex intervalle { }</div>
