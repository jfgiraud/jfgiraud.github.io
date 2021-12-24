---
layout: post
title: "bash, supprimer les tags html avec sed..."
date: "2012-09-06 10:29:00"
tags: sed tag html
---
Dans certains scripts bash, on peut souhaiter supprimer les tags html d'un flux ou d'un fichier. Pour cela on peut utiliser la commande sed.  


```bash
$ echo $texte
<div class='descriptionwrapper'> <p class='description'><span>J'entrepose ici mes découvertes linux, bash, python et java que je souhaite partager et mettre de côté...</span></p> </div>
$ texte | sed -e 's/<[^>]*>//g'
 J'entrepose ici mes découvertes linux, bash, python et java que je souhaite partager et mettre de côté...
```

