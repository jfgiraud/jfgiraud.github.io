---
title: "mysql, export d'une table au format csv"
date: "2012-06-26 14:20:00"
---
Il est possible d'exporter le contenu d'une table dans un fichier via une requête mysql. Voici la syntaxe :  <code><pre>
SELECT champ1,champ2 FROM matable INTO OUTFILE 'lefichier.csv' 
FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"';
</pre></code>
