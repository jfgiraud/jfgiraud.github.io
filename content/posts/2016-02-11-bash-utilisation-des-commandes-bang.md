---
title: "bash, utilisation des commandes bang !"
date: 2016-02-11T16:44:00+01:00
tags: ["shebang"]
---
Voici un gros post concernant les commandes bang de bash.

Je connaissais "!!", "!ligne" et "!commande" ce qui est déjà pas mal. Mais il y en a bien d'autres !!!

En les connaissant et les utilisant, il doit être possible de minimiser les contacts avec la souris ;)

Les commandes : 


```
Syntaxe
      
      !!              Exécute la dernière commande
      !509            Exécute la commande 509 de l'historique
      !-2             Exécute l'avant dernière commande 
      !foo            Exécute la dernière commande qui commance par 
                      'foo' (cad. !ls)
      !foo:p          Affiche la commande que !foo exécuterait et 
                      l'ajoute à l'historique
      !$              Exécute le dernier mot de la dernière commande 
                      (identique à Alt + .)
      !$:p            Affiche la commande que !$ exécuterait
      !*              Exécute la commande précédente sans le premier 
                      mot (cad la commande)
      !*:p            Affiche la commande que !* exécuterait
      ^foo^bar        Exécute la commande précédente en remplaçant 
                      'foo' par 'bar' dans le premier mot

Modificateurs de mots

      !509:2:h        Supprime le nom du fichier à la fin du chemin dans 
                      le 2e argument de la commande 509 de l'historique
      !509:2:t        Supprime le début du chemin jusqu'au nom du fichier 
                      dans le 2e argument de la commande 509 de l'historique
      !509:2:r        Supprime l'extension dans le 2e argument de la 
                      commande 509 de l'historique
      !509:2:e        Ne garde que l'extension du le 2e argument de la 
                      commande 509 de l'historique
      !509:2:gs/a/x/  Remplace les 'a' par des 'x' dans le 2e argument 
                      de la commande 509 de l'historique
```

Quelques cas d'usage simples :


```bash
$ touch a b c d e
$ !!
touch a b c d e
$ ls !:3
ls c
c
$ history | tail -n 3
  515  touch a b c d e
  516  ls c
  517  history | tail -n 3
$ ls !515:$ !516:^:p
ls e c
$ for a in !515:*; do echo $a; done
for a in a b c d e; do echo $a; done
a
b
c
d
e
$ history | tail -n 3
  518  ls e c
  519  for a in a b c d e; do echo $a; done
  520  history | tail -n 3
$ !ls
ls e c
c  e
$ ^ls^rm
rm e c
$ history | tail -n 6
  518  ls e c
  519  for a in a b c d e; do echo $a; done
  520  history | tail -n 3
  521  ls e c
  522  rm e c
  523  history | tail -n 6
$ !-3
ls e c
ls: impossible d'accéder à e: Aucun fichier ou dossier de ce type
ls: impossible d'accéder à c: Aucun fichier ou dossier de ce type
$ !-3:$:p
c
$ !523
history | tail -n 6
  521  ls e c
  522  rm e c
  523  history | tail -n 6
  524  ls e c
  525  c
  526  history | tail -n 6
$
```

D'autres cas d'usage avec modification des paramètres


```bash
$ ls /usr/local/lib/python3.4/dist-packages/aiohttp/client.py
/usr/local/lib/python3.4/dist-packages/aiohttp/client.py
$ !$:h:p
/usr/local/lib/python3.4/dist-packages/aiohttp
$ ls /usr/local/lib/python3.4/dist-packages/aiohttp/client.py
/usr/local/lib/python3.4/dist-packages/aiohttp/client.py
$ !$:t:p
client.py
$ ls /usr/local/lib/python3.4/dist-packages/aiohttp/client.py
/usr/local/lib/python3.4/dist-packages/aiohttp/client.py
$ !$:r:p
/usr/local/lib/python3.4/dist-packages/aiohttp/client
$ ls /usr/local/lib/python3.4/dist-packages/aiohttp/client.py
/usr/local/lib/python3.4/dist-packages/aiohttp/client.py
$ !$:e:p
.py
$ !-2:s/.py/.old/:p
ls /usr/local/lib/python3.4/dist-packages/aiohttp/client.old
```

Sources :
- [http://ss64.com/bash/bang.html](http://ss64.com/bash/bang.html)
- [http://samrowe.com/wordpress/advancing-in-the-bash-shell/](http://samrowe.com/wordpress/advancing-in-the-bash-shell/)
- [http://www.skorks.com/2009/09/bash-shortcuts-for-maximum-productivity/](http://www.skorks.com/2009/09/bash-shortcuts-for-maximum-productivity/)



