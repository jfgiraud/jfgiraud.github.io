---
title: "sed/awk, remplacer plusieurs occurences entre deux balises html"
date: 2016-03-01T11:27:00+01:00
tags: ["commande", "sed", "awk"]
---

```bash
sed -ri "/<childProjects>/,/<\/childProjects>/ { s/monsvi-/MAINTENANCE-$GOROCO-monsvi-/g; }" $config_file
```

Attention, il faut prendre garde au cas où les tags html ne seraient pas uniques :


```bash
$ cat text.txt
<a>
  <b>toto</b>
  <c>toto</c>
  <b>toto</b>
</a>
$ cat text.txt | sed -r '/<b>/,/<\/b>/ { s/toto/t*t*/g; }'
<a>
  <b>t*t*</b>
  <c>t*t*</c>
  <b>t*t*</b>
</a>
```

Si on a la chance que le tag de fin est sur la même ligne :


```bash
$ cat text.txt | sed -r '/<b>/,0 { s/toto/t*t*/g; }'<a>
  <b>t*t*</b>
  <c>toto</c>
  <b>t*t*</b>
</a>
```

Toutefois, je conseille de préférer `awk` dont le comportement est plus sûr.


```bash
$ cat text.txt | awk '/<b>/,/<\/b>/ { gsub("toto", "t*t*"); print; next } { print } '
<a>
  <b>t*t*</b>
  <c>toto</c>
  <b>t*t*</b>
</a>
```
