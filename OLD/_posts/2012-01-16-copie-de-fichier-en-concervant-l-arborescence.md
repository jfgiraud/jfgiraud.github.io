---
title: "Copie de fichier en concervant l'arborescence"
date: "2012-01-16 10:32:00"
---
$ mkdir toto/tutu/titi/
$ touch toto/tutu/titi/grosminet.txt
$ mkdir tata
$ cp --parents toto/tutu/titi/grosminet.txt tata
$ tree 
<pre>.
├── tata
│   └── toto
│       └── tutu
│           └── titi
│               └── grosminet.txt
└── toto
    └── tutu
        └── titi
            └── grosminet.txt
</pre>
