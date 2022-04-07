---
layout: post
title: "bash, composer une url depuis une url de référence avec sed"
date: "2016-09-21 17:08:00"
---

```
$ link="https://www.example.com/path/to/somewhere?q=xxx"
$ new_link="$(echo $link | sed -rn 's#([^:]*://[^/]*)/.*#\1#p')/another/path/to/somewhere?qq=yyy"
$ echo $new_link
https://www.example.com/another/path/to/somewhere?qq=yyy
```

<div style="height: 0; overflow: hidden;">bash sed nom de domaine url
</div>
