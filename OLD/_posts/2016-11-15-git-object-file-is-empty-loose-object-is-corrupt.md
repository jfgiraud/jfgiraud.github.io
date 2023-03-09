---
title: "git, object file is empty, loose object is corrupt"
date: 2016-11-15T10:21:00+01:00
tags: ["git"]
---
Sur des repo git sous jenkins, j'avais des problèmes... 


```
Caused by: hudson.plugins.git.GitException: Command "git -c core.askpass=true fetch --tags --progress uuuu@xxxx.yyyy.zzz:aaaaa/bbbbb.git +refs/heads/*:refs/remotes/origin/*" returned status code 128:
stdout: 
stderr: error: object file .git/objects/99/9de0c2f62f74a48912a0b407948f0e17fc12d3 is empty
error: object file .git/objects/99/9de0c2f62f74a48912a0b407948f0e17fc12d3 is empty
fatal: loose object 999de0c2f62f74a48912a0b407948f0e17fc12d3 (stored in .git/objects/99/9de0c2f62f74a48912a0b407948f0e17fc12d3) is corrupt
fatal: The remote end hung up unexpectedly

git stash
cd .git/ && find . -type f -empty -delete
git stash clear
```

Pour les résoudre, j'ai appliqué la solution de Nicolas disponible sur [http://stackoverflow.com/a/14850742/3550759](http://stackoverflow.com/a/14850742/3550759).
