---
title: "mysql, regexp"
date: "2012-11-22 12:21:00"
---
Pour comptabiliser avec une regexp les numéros appelant valides (non masqués) 


```
mysql> select count(distinct numAppelant) from appels_201210 where numAppelant REGEXP '^[0-9]{10}$';
+-----------------------------+
| count(distinct numAppelant) |
+-----------------------------+
|                       16215 | 
+-----------------------------+
1 row in set (0.09 sec)
```

<div style="height: 0; overflow: hidden;">select count distinct REGEXP
</div>
