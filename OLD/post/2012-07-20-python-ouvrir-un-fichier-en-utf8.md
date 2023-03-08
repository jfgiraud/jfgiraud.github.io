---
layout: post
title: "python, ouvrir un fichier en utf8"
date: "2012-07-20 15:23:00"
---
Pour ouvrir un fichier en utilisant un encodage particulier, il est possible de passer par le module codecs...  <code><pre>
with codecs.open('the_file.csv', 'r', 'utf8') as f:
    l = f.readline()
    ...
</pre></code>
