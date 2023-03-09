---
title: "MySQL : ERROR 1215 (HY000): Cannot add foreign key constraint"
date: 2020-10-14T12:22:00+01:00
tags: ["mysql"]
---

Echec de l'import du dump.  Ajouter en haut du script :  

```
SET foreign_key_checks = 0;
```

