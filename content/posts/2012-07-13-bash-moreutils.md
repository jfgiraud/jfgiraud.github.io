---
title: "bash, moreutils"
date: 2012-07-13T11:18:00+01:00
tags: ["bash", "moreutils"]
---
Je viens de découvrir un paquet mettant à disposition des outils bien sympathiques pour faciliter l'écriture de scripts bash.  Il s'agit du paquet moreutils  
```bash
$ sudo apt-get install moreutils
``` 

Exemples d'utilisation :  

```bash
Pour envoyer un mail si des données sont lues sur l'entrée standard...
$ find . -name core | ifne mail -s "Core files found" root

Pour réécrire dans un même fichier sans avoir à créer un fichier temporaire...
$ sed '...' file | grep '...' | sponge file
```
