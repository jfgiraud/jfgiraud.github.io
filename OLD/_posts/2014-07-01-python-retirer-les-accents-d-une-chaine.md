---
layout: post
title: "Python, retirer les accents d'une chaine"
date: "2014-07-01 07:03:00"
tags: python accent accents retirer supprimer unicode unicodedata
---

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import unicodedata

def deaccent(some_unicode_string):
    return ''.join(c for c in unicodedata.normalize('NFD', some_unicode_string)
               if unicodedata.category(c) != 'Mn')



>>> s="Dès Noël où un zéphyr haï me vêt de glaçons würmiens je dîne d’exquis rôtis de bœuf au kir à l’aÿ d’âge mûr & cætera !"
>>> deaccent(s)
'Des Noel ou un zephyr hai me vet de glacons wurmiens je dine d’exquis rotis de bœuf au kir a l’ay d’age mur & cætera !'
```

