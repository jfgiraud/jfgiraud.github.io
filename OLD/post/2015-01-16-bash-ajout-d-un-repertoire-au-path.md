---
layout: post
title: "Bash, ajout d'un répertoire au PATH"
date: "2015-01-16 10:47:00"
tags: bash path
---
Pour tester et ajouter un répertoire au PATH, on peut faire comme ceci dans son ~/.bashrc


```
if [[ ! "$PATH" =~ (^|:)"/path/to/the/directory/bin"(:|$) ]]; then
    export PATH="$PATH:/path/to/the/directory/bin"
fi
```

L'utilisation d'un test avec regexp permet de garder une variable avec un contenu "propre".
