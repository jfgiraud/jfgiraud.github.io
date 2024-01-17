---
title: "bash, presse-papier"
date: 2012-05-24T11:17:00+01:00
tags: ["presse papier", "bash", "commande", "xclip"]
---
Il est possible de copier un fichier ou la sortie standard dans le presse papier...  Il suffit d'utiliser la commande `xsel`. Exemple : 
```
$ cat /etc/fstab | xsel -b
```
La commande xclip un peu similaire permet la même chose...
```
$ sudo apt-get install xclip# Downloads and installs xclip
$ xclip -sel clip < ~/.ssh/id_rsa.pub
```
