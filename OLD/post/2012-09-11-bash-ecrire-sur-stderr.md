---
layout: post
title: "bash, écrire sur stderr"
date: "2012-09-11 13:11:00"
tags: bash redirection
---

Pour écrire sur `stderr`

```bash
$ cat stderr.txt
echo "Mon texte sur stderr" >&2

cat >&2 <<-EOF
    et pourquoi pas
    encore du texte sur stderr
EOF
$ bash stderr.txt > /dev/null
Mon texte sur stderr
    et pourquoi pas
    encore du texte
$ bash stderr.txt 2> /dev/null
$
```

