---
title: "Mysqldump : un insert par tuple..."
date: 2012-03-15T14:38:00+01:00
tags: ["mysqldump"]
description: "générer un insert par ligne"
---

```
mysqldump --skip-extended-insert ...
```

génère un INSERT par ligne de la table.
