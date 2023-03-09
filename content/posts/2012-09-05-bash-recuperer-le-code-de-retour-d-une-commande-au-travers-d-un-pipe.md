---
title: "bash, récupérer le code de retour d'une commande au travers d'un pipe"
date: 2012-09-05T17:20:00+01:00
tags: ["bash", "pipe", "code", "erreur"]
---

L'exemple se passe de commentaires !  

```bash
$ ls toto | head -n 1
ls: impossible d'accéder à toto: Aucun fichier ou dossier de ce type
$ echo $?
0
$ set -o pipefail 1
$ ls toto | head -n 1
ls: impossible d'accéder à toto: Aucun fichier ou dossier de ce type
$ echo $?
2
```

Pratique dans le cas d'un `curl $url | sed ... > $output` pour savoir si une erreur est remontée.  
