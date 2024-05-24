---
title: "python, unicode..."
date: 2012-07-16T12:56:00+01:00
tags: ["bash", "python", "encoding"]
---

```
>>> unicodedata.name(u"é")
'LATIN SMALL LETTER E WITH ACUTE'
>>> print u"e accent aigu : \N{LATIN SMALL LETTER E WITH ACUTE}"
e accent aigu : é
```
