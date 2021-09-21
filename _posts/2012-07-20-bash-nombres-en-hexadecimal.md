---
layout: post
title: "bash, nombres en hexadécimal"
date: "2012-07-20 14:53:00"
---
Si pour une raison ou une autre, vous devez jouer à afficher des nombres héxadécimal en base 10 ou vice-versa, vous pouvez passer par la commande printf  <code><pre>$ printf "%x" 174<br />ae<br />$ printf "%d" 0xae<br />174<br />$ printf "%d\n" \'A<br />65<br /></pre></code>
