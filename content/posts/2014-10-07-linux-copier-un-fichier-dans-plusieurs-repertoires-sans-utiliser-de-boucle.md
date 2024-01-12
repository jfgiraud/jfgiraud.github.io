---
title: "linux, copier un fichier dans plusieurs répertoires sans utiliser de boucle"
date: 2014-10-07T15:55:00+01:00
tags: ["bash", "cp", "xargs", "astuce"]
---
Un truc et astuce pour copier un fichier à plusieurs endroits dans utiliser une boucle for...

Il suffit d'utiliser la commande <code>xargs</code> avec le paramètre <code>-n 1</code> comme dans l'exemple ci-dessous : 


```
$ ls
$ mkdir a b c
$ echo hello > test.txt
$ tree 
.
├── a
├── b
├── c
└── test.txt

3 directories, 1 file
$ echo a b c | xargs -n 1 cp test.txt 
$ tree 
.
├── a
│   └── test.txt
├── b
│   └── test.txt
├── c
│   └── test.txt
└── test.txt

3 directories, 4 files
```
