---
layout: post
title: "python, obtenir la liste des fichiers .java"
date: "2012-07-23 11:56:00"
---
Pour récupérer la liste des .java dans une arborescence et sa sous-arborescence, on peut utiliser le code suivant :  <code><pre><br />import fnmatch<br />import os<br /><br />matches = []<br />for root, dirnames, filenames in os.walk('/path/to/the/directory'):<br />  for filename in fnmatch.filter(filenames, '*.java'):<br />      matches.append(os.path.join(root, filename))<br /></pre></code>
