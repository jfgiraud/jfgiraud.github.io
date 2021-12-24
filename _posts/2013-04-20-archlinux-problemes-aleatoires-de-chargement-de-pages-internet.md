---
layout: post
title: "Archlinux, problèmes aléatoires de chargement de pages internet"
date: "2013-04-20 09:47:00"
---
En installant archlinux il y a quelques temps, j'avais constaté que j'avais des problèmes de connexion internet de manière aléatoire. Un rafraichissement de la page la faisait apparaître :) mais j'ai galéré à comprendre que cela venait des DNS déclarés.
La machine utilisait le DNS de ma livebox et comme par hasard, celui-ci résout aléatoirement les adresses :/

J'ai alors configuré de la manière suivante en spécifiant les DNS à utiliser et en forçant DHCP à ne pas écraser le fichier /etc/resolv.conf

<script src="https://pastebin.com/embed_js/PV1FECQw"></script>

<div style="height: 0; overflow: hidden;">nameserver etc resolv.conf
</div>
Depuis, que du bonheur !

