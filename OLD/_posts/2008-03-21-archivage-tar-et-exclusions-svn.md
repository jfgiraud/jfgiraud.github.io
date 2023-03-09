---
title: "Archivage tar et exclusions .svn"
date: 2008-03-21T16:06:00+01:00
---
Pour exclure les répertoires lors de la création d'une archive avec tar,
il faut utiliser --exclude pattern <span style="font-weight: bold;">après le nom de l'archive.</span>

<span style="font-style: italic;">Exemple :</span>
<span style="font-style: italic;"></span><pre>
tar zcvf nomarchive.tgz --exclude '.svn' batch/
</pre>
