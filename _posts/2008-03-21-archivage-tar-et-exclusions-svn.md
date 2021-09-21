---
layout: post
title: "Archivage tar et exclusions .svn"
date: "2008-03-21 16:06:00"
---
Pour exclure les répertoires lors de la création d'une archive avec tar,<br />il faut utiliser --exclude pattern <span style="font-weight: bold;">après le nom de l'archive.</span><br /><br /><span style="font-style: italic;">Exemple :</span><br /><span style="font-style: italic;"></span><pre><br />tar zcvf nomarchive.tgz --exclude '.svn' batch/<br /></pre>
