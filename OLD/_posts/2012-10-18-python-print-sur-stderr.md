---
layout: post
title: "python, print sur stderr"
date: "2012-10-18 10:33:00"
---

```
$ cat example.py 
#!/usr/bin/python
import sys
print >> sys.stderr, "Hello world!"
$ python example.py 2> /dev/null
$
```

<div style="height: 0; overflow: hidden;">print, sys, stderr</div>
