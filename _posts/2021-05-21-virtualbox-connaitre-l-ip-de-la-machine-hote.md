---
layout: post
title: "VirtualBox, connaitre l'IP de la machine hôte"
date: "2021-05-21 12:12:00"
---
Dans le terminal de la VM,    <kbd>ipconfig</kbd> donne l'information dans  <pre><br />   Passerelle par défaut. . . . . . . . . : xxx<br /></pre>  <kbd>netstat -rn</kbd> donne l'information dans "Adr. passerelle" <pre><br />Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique<br />0.0.0.0               0.0.0.0        xxx               yyy            10<br /></pre>  
