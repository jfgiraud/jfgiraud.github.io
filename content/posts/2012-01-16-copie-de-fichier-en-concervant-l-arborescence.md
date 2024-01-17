---
title: "Copie de fichier en concervant l'arborescence"
date: 2012-01-16T10:32:00+01:00
tags: ["bash", "tree"]
---

```
$ mkdir toto/tutu/titi/
$ touch toto/tutu/titi/grosminet.txt
$ mkdir tata
$ cp --parents toto/tutu/titi/grosminet.txt tata
$ tree 
.
├── tata
│   └── toto
│       └── tutu
│           └── titi
│               └── grosminet.txt
└── toto
    └── tutu
        └── titi
            └── grosminet.txt
```
