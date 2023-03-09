---
title: "html, liste des balises html"
date: 2020-06-04T10:47:00+01:00
tags: ["html", "balises"]
---
Liste des balises HTML pouvant être utilisées pour vérifier que des entrées de formulaires ne contiennent pas de code HTML.

```
A
ABBR
ACRONYM
ADDRESS
AREA
B
BASE
BDO
BIG
BLOCKQUOTE
BODY
BR
BUTTON
CAPTION
CITE
CODE
COL
COLGROUP
DD
DEL
DFN
DIV
DL
DT
EM
FIELDSET
FORM
H1
H2
H3
H4
H5
H6
HEAD
HR
HTML
I
IMG
INPUT
INS
KBD
LABEL
LEGEND
LI
LINK
MAP
META
NOSCRIPT
OBJECT
OL
OPTGROUP
OPTION
P
PARAM
PRE
Q
SAMP
SCRIPT
SELECT
SMALL
SPAN
STRONG
STYLE
SUB
SUP
TABLE
TBODY
TD
TEXTAREA
TFOOT
TH
THEAD
TITLE
TR
TT
UL
VAR
```


Sous forme de liste (avec quote and join disponible [ici](https://github.com/jfgiraud/quote-and-join))

```
$ cat ~/balises.txt | tr -d '",' | tr ' ' '\n' | sort -u | ~/bin/qaj -qq -j ', '
"A", "ABBR", "ACRONYM", "ADDRESS", "AREA", "B", "BASE", "BDO", "BIG", "BLOCKQUOTE", "BODY", "BR", "BUTTON", "CAPTION", "CITE", "CODE", "COL", "COLGROUP", "DD", "DEL", "DFN", "DIV", "DL", "DT", "EM", "FIELDSET", "FORM", "H1", "H2", "H3", "H4", "H5", "H6", "HEAD", "HR", "HTML", "I", "IMG", "INPUT", "INS", "KBD", "LABEL", "LEGEND", "LI", "LINK", "MAP", "META", "NOSCRIPT", "OBJECT", "OL", "OPTGROUP", "OPTION", "P", "PARAM", "PRE", "Q", "SAMP", "SCRIPT", "SELECT", "SMALL", "SPAN", "STRONG", "STYLE", "SUB", "SUP", "TABLE", "TBODY", "TD", "TEXTAREA", "TFOOT", "TH", "THEAD", "TITLE", "TR", "TT", "UL", "VAR"
```


Source: extrait de [http://www.w3.org/TR/html4/strict.dtd](http://www.w3.org/TR/html4/strict.dtd)
