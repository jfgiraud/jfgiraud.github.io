---
layout: post
title: "base64, encoder/décoder sous bash"
date: "2016-09-09 15:11:00"
tags: commande base64 recode
---

On peut utiliser les programmes base64 (GNU coreutils) voir recode.

```
$ echo "Tralala pouet pouet"
Tralala pouet pouet
$ echo "Tralala pouet pouet" | base64
VHJhbGFsYSBwb3VldCBwb3VldAo=
$ echo VHJhbGFsYSBwb3VldCBwb3VldAo= | base64 -d
Tralala pouet pouet
$ echo VHJhbGFsYSBwb3VldCBwb3VldAo= | recode /b64
Tralala pouet pouet
$ echo "Tralala pouet pouet" | recode ../b64
VHJhbGFsYSBwb3VldCBwb3VldAo=
```



