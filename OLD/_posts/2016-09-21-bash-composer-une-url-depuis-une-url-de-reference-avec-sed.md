---
title: "bash, composer une url depuis une url de référence avec sed"
date: 2016-09-21T17:08:00+01:00
tags: ["bash", "sed", "nom", "de", "domaine", "url"]
---

```bash
$ link="https://www.example.com/path/to/somewhere?q=xxx"
$ new_link="$(echo $link | sed -rn 's#([^:]*://[^/]*)/.*#\1#p')/another/path/to/somewhere?qq=yyy"
$ echo $new_link
https://www.example.com/another/path/to/somewhere?qq=yyy
```

