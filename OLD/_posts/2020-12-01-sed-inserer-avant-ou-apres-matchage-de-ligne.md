---
title: "sed, insérer avant ou après matchage de ligne"
date: "2020-12-01 11:15:00"
tags: sed
---

Peut-être pratique pour modifier un fichier de configuration par exemple

```text
$ printf "[section1]\\n\\n[section2]\\ncle1=valeur1\\n" | sed '/^\\[section2\\]/i cle2=valeur2'
[section1]

cle2=valeur2
[section2]
cle1=valeur1

$ printf "[section1]\\n\\n[section2]\\ncle1=valeur1\\n" | sed '/^\\[section2\\]/a cle2=valeur2'
[section1]

[section2]
cle2=valeur2
cle1=valeur1
 ```