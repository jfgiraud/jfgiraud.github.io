---
title: "python, marre des accents en java : remplacez les par de l'unicode !"
date: 2012-05-24T11:13:00+01:00
tags: ["python", "unicode", "utf8"]
---

```python
$ cat tounicode.py
#!/usr/bin/python

import re
import sys

s = sys.argv[1].decode('utf8')

print re.sub('\\\\x', '\\u00', re.sub('\'$', '', re.sub('^u\'', '', repr(s))))

$ python tounicode.py "salut beaut&eacute;"
salut beaut\u00e9
```
