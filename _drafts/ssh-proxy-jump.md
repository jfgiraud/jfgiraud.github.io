---
layout: post
title: "ssh, proxy jump"
date: "2020-11-25 12:14:00"
---
https://blog.octo.com/le-bastion-ssh/ https://doc.fedora-fr.org/wiki/SSH:_Simplifier_une_connexion_passant_par_un_Proxy  $ cat ~/.ssh/config~  Host dix-sqlxxx.dixxx.xxx     ProxyCommand ssh dix-batchxxx.dixxx.xxx -W %h:%p     User xxxx 
