---
layout: post
title: "mysql, dumper seulement les données"
date: "2013-03-14 16:15:00"
---

```
mysqldump -u root dbname --no-create-info --skip-triggers --compact --complete-insert --skip-extended-insert
```

<div style="height: 0; overflow: hidden;">mysqldump -u root dbname --no-create-info --skip-triggers --compact --complete-insert --skip-extended-insert</div>
