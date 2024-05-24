---
title: "url et mot de passe"
date: 2012-07-03T18:24:00+01:00
tags: ["encodage", "url"]
---
Pour réduire mes logs, je viens d'utiliser la syntaxe suivante :  
```
http://user:password@host:port...
```
Ici, le mot de passe doit être encodé lorsque des caractères non alphanumériques sont utilisés (comprenez 0-9a-zA-Z).  Chaque caractère non alphanumérique doit être encodé avec le format "%xx" où xx sera remplacé par le code hexadécimal du caractère.  

Exemple: 

```python
def conv(pw):
    r = ''
    for c in pw:
 if not c.isalpha():
     r += '%' + '%X' % ord(c)
 else:
     r += c
    return r 

>>> conv(u'tuéàtu')
u'tu\xe9\xe0tu'

```
