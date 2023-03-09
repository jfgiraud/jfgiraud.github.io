---
title: "python, lire et écrire des fichiers xls"
date: 2012-10-15T11:36:00+01:00
tags: ["python", "excel"]
---
Si l'on a des fichiers Excel que l'on souhaite lire ou écrire, on peut utiliser les paquets xlrd (reader) et xlwt (writer).

Voici un petit exemple de ce que l'on peut faire :


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xlrd
import codecs
import os

files = [u"FormatBDD_XXX_backend.xls", u"FormatBDD_XXXdata.xls", u"FormatBDD_XXX_desc.xls", u"FormatBDD_XXX_dm.xls", u"FormatBDD_dimension.xls"]

for f in files:
    book = xlrd.open_workbook(f)
    for sheet_name in book.sheet_names():
        base = f.replace('FormatBDD_', '')
        base = base.replace('.xls', '')
        sheet = book.sheet_by_name(sheet_name) 
        headers = sheet.row_values(0)
        for rownum in range(1, sheet.nrows):
            row = sheet.row_values(rownum)
            nom = row[headers.index(u'Nom')]
            description = row[headers.index(u'Description')]
            try:
                commentaire = u" Commentaires: " + row[headers.index(u'Commentaires')].replace('"', '\"')
            except ValueError:
                commentaire = u''
            description = description + commentaire
            print u'replace into descriptions (b, t, c, d) values ("%s", "%s", "%s", "%s");' % (base, sheet_name, nom.strip(), description.strip().replace('"', '\\"'))
```

La page suivante propose des exemples clairs et rapides pour bien commencer :
[http://www.dev-explorer.com/articles/excel-spreadsheets-and-python](http://www.dev-explorer.com/articles/excel-spreadsheets-and-python)
