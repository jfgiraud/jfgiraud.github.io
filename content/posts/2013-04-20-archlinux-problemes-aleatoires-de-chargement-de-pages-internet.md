---
title: "Archlinux, problèmes aléatoires de chargement de pages internet"
date: 2013-04-20T09:47:00+01:00
---
En installant archlinux il y a quelques temps, j'avais constaté que j'avais des problèmes de connexion internet de manière aléatoire. Un rafraichissement de la page la faisait apparaître :) mais j'ai galéré à comprendre que cela venait des DNS déclarés.
La machine utilisait le DNS de ma livebox et comme par hasard, celui-ci résout aléatoirement les adresses :/

J'ai alors configuré de la manière suivante en spécifiant les DNS à utiliser et en forçant DHCP à ne pas écraser le fichier /etc/resolv.conf


```
$ cat /etc/resolv.conf.head 
nameserver 127.0.0.1
search home
$ cat /etc/resolv.conf.tail
nameserver 208.67.222.222
nameserver 208.67.220.220
$ tail /etc/dhcpcd.conf 
# Respect the network MTU.
option interface_mtu
# A ServerID is required by RFC2131.
require dhcp_server_identifier

# A hook script is provided to lookup the hostname if not set by the DHCP
# server, but it should not be run by default.
nohook lookup-hostname
nohook resolv.conf
noipv4ll
```

<div style="height: 0; overflow: hidden;">nameserver etc resolv.conf
</div>
Depuis, que du bonheur !

