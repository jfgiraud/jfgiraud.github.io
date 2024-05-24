---
title: "python, bash et encoding..."
date: 2012-07-16T12:31:00+01:00
tags: ["bash", "python", "encoding"]
---
En python, lorsque la sortie n'est pas de type tty, l'encoding est "ascii" ce qui provoque des erreurs sur les caractères accentués. La solution est d'exporter la variable PYTHONIOENCODING qui définit l'encoding à utiliser.  

```
$ python a.py 
é
$ python a.py | cat
Traceback (most recent call last):
  File "a.py", line 3, in <module>
    print u"\xe9";
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 0: 
ordinal not in range(128)
$ export PYTHONIOENCODING=utf-8 
$ python a.py | cat
é
$
``` 

Une autre solution est de changer l'encoding de stdout...  

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import locale

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

print u"é"
```
