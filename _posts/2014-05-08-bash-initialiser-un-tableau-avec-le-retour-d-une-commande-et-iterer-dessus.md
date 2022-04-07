---
layout: post
title: "bash, initialiser un tableau avec le retour d'une commande et itérer dessus"
date: "2014-05-08 03:24:00"
---

```
$ tree 
.
├── a
│   ├── a 1
│   └── a 2
├── b
│   ├── b 1
│   └── b 2
└── c
    ├── c 1
    └── c 2

3 directories, 6 files
$ mapfile -t files < <(find -type f)
$ for file in "${files[@]}"; do
> echo "file: $file"
> done
file: ./a/a 2
file: ./a/a 1
file: ./b/b 2
file: ./b/b 1
file: ./c/c 2
file: ./c/c 1
```

<div style="height: 0; overflow: hidden;">bash mapfile iterate loop array
</div>
Cette méthode est sûre concernant les espaces contenus dans les lignes renvoyées par la commande :)
