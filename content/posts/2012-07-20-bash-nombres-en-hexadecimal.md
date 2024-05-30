---
title: "bash, nombres en hexadécimal"
date: 2012-07-20T14:53:00+01:00
tags: ["bash", "nombre", "hexa"]
---
Si pour une raison ou une autre, vous devez jouer à afficher des nombres héxadécimal en base 10 ou vice-versa, vous pouvez passer par la commande printf

```console
$ printf "%x" 174
ae
$ printf "%d" 0xae
174
$ printf "%d\n" \'A
65
```
