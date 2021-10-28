---
layout: post
title: "mysqlimport"
date: "2012-05-04 15:41:00"
---
Le fichier doit porter le nom de la table à l'extension près.  Ici les options utilisées sont : <ul><li>--delete pour vider la table avant l'import <li>--fields-terminated-by pour le séparateur entre les champs <li>--lines-terminated-by pour le caractère de fin de ligne (ici DOS/WINDOWS) </ul> <br /><pre><code>mysqlimport <br />--fields-terminated-by=\; <br />--lines-terminated-by="\\r\\n" <br />-v <br />--delete <br />-utest -ptest -hlocalhost BASE TABLE.csv</code></pre>
