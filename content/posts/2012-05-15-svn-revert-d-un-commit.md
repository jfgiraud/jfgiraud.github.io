---
title: "svn, revert d'un commit"
date: 2012-05-15T12:32:00+01:00
tags: ["svn", "revert"]
---
Un mauvais commit sur un fichier ? Pas de problème, il peut être inversé :)

```
svn merge -c -[bad_revision] [repository_url]
```

Attention au - devant la mauvaise révision...  Ne restera plus qu'à commiter l'inversion
