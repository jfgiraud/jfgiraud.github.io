---
title: "web, utiliser pastebin et permettre une recherche sur son blog"
date: 2012-09-12T17:48:00+01:00
tags: ["pastebin", "mot clé", "search engine", "moteur de recherche"]
---
Inclure du code déposé sur pastebin c'est bien... Malheureusement, le moteur de recherche du blog ne recherche pas dans le contenu déposé sur pastebin.

Pour permettre une recherche, on peut positionner des mots clés "invisibles" dans sa page.


```
<script src="http://pastebin.com/embed_js.php?i=2TwEyffe"></script>
<div style="overflow:hidden; height:0;">grant insert select on mysql user privileges flush</div>
```

Le moteur de recherche les verra et remontera l'article :)
