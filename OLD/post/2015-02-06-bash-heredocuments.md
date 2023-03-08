---
layout: post
title: "bash, heredocuments"
date: "2015-02-06 11:01:00"
tags: bash heredocuments
---
Il est possible de désactiver les substitutions dans les heredocuments en bash.

Pour se faire, il suffit de quoter son nom.


```
#!/bin/bash

text="hello the world!"

cat<<EOF
$text
`date`
$((3+1))
EOF

cat<<"EOF"
$text
`date`
$((3+1))
EOF
```

Produit : 


```
hello the world!
vendredi 6 février 2015, 10:56:26 (UTC+0100)
4
$text
`date`
$((3+1))
```
