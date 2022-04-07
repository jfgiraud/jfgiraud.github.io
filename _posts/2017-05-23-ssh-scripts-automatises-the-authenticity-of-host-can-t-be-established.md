---
layout: post
title: "ssh & scripts automatisés, The authenticity of host can't be established"
date: "2017-05-23 10:15:00"
---
Lors d'appels de scripts automatisés pour "calculer" ce qui est à mettre en préproduction, j'ai souvent des "The authenticity of host can't be established".
Peut-être parce que la machine est puppétisée...

Soit il faut répondre manuellement, soit il faut éviter d'avoir le prompt...

Pour éviter d'avoir à répondre, on peut ajouter l'option "-o StrictHostKeyChecking=no" à ses commandes SSH.


```
$ ssh user@host.example.com
Pseudo-terminal will not be allocated because stdin is not a terminal.
The authenticity of host 'host.example.com (xx.xx.xx.xx)' can't be established.
ECDSA key fingerprint is XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX.
Are you sure you want to continue connecting (yes/no)? ^C

$ ssh -o StrictHostKeyChecking=no "user@host.example.com"
Linux host 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64
########################################
#    Attention Machine Puppetisee      #
########################################
Last login: Tue May 23 10:02:42 2017 from yy.yy.yy.yy
$
```

Ce n'est pas beau, certes...

Source : [stackoverflow](https://stackoverflow.com/questions/28461713/how-to-ignore-or-pass-yes-when-the-authenticity-of-host-cant-be-established-i)
