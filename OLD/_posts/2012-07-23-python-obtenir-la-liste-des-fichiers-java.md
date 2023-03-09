---
title: "python, obtenir la liste des fichiers .java"
date: 2012-07-23T11:56:00+01:00
---
Pour récupérer la liste des .java dans une arborescence et sa sous-arborescence, on peut utiliser le code suivant :  <code><pre>
import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('/path/to/the/directory'):
  for filename in fnmatch.filter(filenames, '*.java'):
      matches.append(os.path.join(root, filename))
</pre></code>
