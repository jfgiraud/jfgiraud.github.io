---
title: "python, ouvrir un fichier en utf8"
date: 2012-07-20T15:23:00+01:00
tags: ["python", "open", "file", "encoding"]
---

Pour ouvrir un fichier en utilisant un encodage particulier, il est possible de passer par le module codecs...  

```python
with codecs.open('the_file.csv', 'r', 'utf8') as f:
    l = f.readline()
    ...
```
