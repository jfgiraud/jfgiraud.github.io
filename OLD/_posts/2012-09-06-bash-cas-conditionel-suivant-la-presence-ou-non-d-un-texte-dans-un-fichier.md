---
title: "bash, cas conditionel suivant la présence ou non d'un texte dans un fichier"
date: 2012-09-06T10:43:00+01:00
tags: ["if", "grep", "exit", "status", "bash"]
---
Cela se fait simplement avec un grep...  


```bash
$ if grep -Fq $mot $fichier; then
    echo "Le mot est dans le fichier"
  else
    echo "Le mot n'est pas dans le fichier"
  fi
```

Bien que le test semble inversé, il est correct car la sortie du grep avec un status à 0 est un succès.

Le paragraphe *Conditional Shell Control Structures* de la page [http://teaching.idallen.com/dat2330/04f/notes/exit_status.txt](http://teaching.idallen.com/dat2330/04f/notes/exit_status.txt) l'explique très bien.


