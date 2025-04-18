---
title: "Driver imprimante Ricoh SP 277 snwx"
date: 2021-12-21T07:10:00+01:00
tags: [ "imprimante", "ricoh" ]
description: "Installer les drivers de l'imprimante Ricoh SP 277 snwx"
---

```
http://support.ricoh.com/bb/html/dr_ut_e/re1/model/sp221/sp221.htm
Red Hat Enterprise Linux 7(x86-64)
Download
unzip r78185en.exe
# extrait sp-200-series-gdi-1.01-0.x86_64.rpm
sudo apt install alien
sudo alien -i sp-200-series-gdi-1.01-0.x86_64.rpm
```

Choisir une connexion en IPP avec l'IP de l'imprimante et imprimer une page de test.