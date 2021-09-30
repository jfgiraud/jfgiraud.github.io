---
layout: post
title: "bash, copier les fichiers d'une sortie standard vers un répertoire en utilisant xargs et cp"
date: "2021-05-04 17:29:00"
tags: bash cp xargs
---

```text
find . -name *.tgz | xargs cp -t ~/OLD/
```
