---
layout: post
title: "awk, un exemple pour bien débuter et comprendre..."
date: "2012-10-15 17:05:00"
tags: awk, base, for
---

```bash
$ cat file.txt 
Firstname;Lastname
John;Doe
Jane;Doe
Paul;Smith
#end of file with a ; character
```


```bash
$ for b in b b1 b2; 
do 
  awk -F ';' -v base=$b -v fmt='use %s; insert into Users values ("%s", "%s");\n' 'NR>=2 && /;/ && !/^#/ {printf fmt, base, $1, $2}' file.txt
done

use b; insert into Users values ("John", "Doe");
use b; insert into Users values ("Jane", "Doe");
use b; insert into Users values ("Paul", "Smith");
use b1; insert into Users values ("John", "Doe");
use b1; insert into Users values ("Jane", "Doe");
use b1; insert into Users values ("Paul", "Smith");
use b2; insert into Users values ("John", "Doe");
use b2; insert into Users values ("Jane", "Doe");
use b2; insert into Users values ("Paul", "Smith");
```

`awk` n'est pas si compliqué que ça lorsque l'on comprend la philosophie...

La commande se décompose de la manière suivante :

```
BEGIN { CODE_DEBUT } MATCHAGE { CODE } END { CODE_FIN }
```

- `CODE_DEBUT` est exécuté au début du traitement du fichier ou flux
- `CODE_FIN` est exécuté à la fin du traitement du fichier ou flux
- `CODE` est exécuté sur les lignes du fichier ou flux matchées par les règles de `MATCHAGE`

Dans l'exemple ci-dessus,
- `-F ';'` indique que le séparateur de champs est le `;`
- les `-v` permettent de déclarer une variable awk à partir d'une variable bash (pour transmettre les informations)
- `NR` correspond au numéro de la ligne traitée (on ignore l'entête du fichier avec le test supérieur ou égal à 2)
- `/;/` correspond aux lignes qui contiennent un `;`
- `!/^#/` correspond aux lignes qui ne débutent pas par un dièse

Le programme ci-dessus crée les requêtes à exécuter sur chacune des bases de données pour chacun des enregistrements du fichier `file.txt`

Comme quoi, on peut démystifier `awk` ;) 

