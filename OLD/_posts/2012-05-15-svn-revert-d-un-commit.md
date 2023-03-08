---
title: "svn, revert d'un commit"
date: "2012-05-15 12:32:00"
---
Un mauvais commit sur un fichier ? Pas de problème, il peut être inversé :)
<code><pre>
svn merge -c -[bad_revision] [repository_url]
</pre></code> Attention au - devant la mauvaise révision...  Ne restera plus qu'à commiter l'inversion
