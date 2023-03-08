---
layout: post
title: "mysql, afficher les colonnes d'une table matchant un pattern"
date: "2016-09-16 10:31:00"
tags: mysql colonne
---

```
mysql> show columns from Sessions where Field like '%date%';
+------------+----------+------+-----+---------+-------+
| Field      | Type     | Null | Key | Default | Extra |
+------------+----------+------+-----+---------+-------+
| date_debut | datetime | NO   | MUL | NULL    |       |
| date_fin   | datetime | NO   | MUL | NULL    |       |
+------------+----------+------+-----+---------+-------+
2 rows in set (0.01 sec)
```
