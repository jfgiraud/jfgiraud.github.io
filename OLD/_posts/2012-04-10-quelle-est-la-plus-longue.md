---
title: "Quelle est la plus longue..."
date: 2012-04-10T11:12:00+01:00
---
... ligne !  Elle peut être donnée via l'option méconnue -L de la commande wc...  <code><pre>
$ find . -name '*.java' | sed -e 's/.*\///' | wc -L
73
</pre></code>
