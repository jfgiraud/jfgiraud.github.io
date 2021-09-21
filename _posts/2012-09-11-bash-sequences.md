---
layout: post
title: "bash, séquences"
date: "2012-09-11 13:13:00"
---
Pour obtenir une suite de nombre qui font partie d'une séquence, il y a la commande <tt>seq</tt>. Il existe aussi une manière de le faire directement en bash en utilisant une expression du genre {x..y[..inc]}.  <code><pre><br />$ for i in {1..30..2}; do echo $i; done<br />1<br />3<br />5<br />7<br />9<br />11<br />13<br />15<br />17<br />19<br />21<br />23<br />25<br />27<br />29<br />$ seq 1 2 30<br />1<br />3<br />5<br />7<br />9<br />11<br />13<br />15<br />17<br />19<br />21<br />23<br />25<br />27<br />29<br /></pre></code> Attention toutefois, si les bornes sont définies dans des variables, il faudra un petit coup d'évaluation :  <code><pre><br />$ for i in $(eval echo "{$a..$b}"); do echo $i; done<br />1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br /></pre></code>
