---
title: "bash, nombres en hexadécimal"
date: "2012-07-20 14:53:00"
---
Si pour une raison ou une autre, vous devez jouer à afficher des nombres héxadécimal en base 10 ou vice-versa, vous pouvez passer par la commande printf  <code><pre>$ printf "%x" 174
ae
$ printf "%d" 0xae
174
$ printf "%d\n" \'A
65
</pre></code>
