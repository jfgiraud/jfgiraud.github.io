---
layout: post
title: "bash, convertir la casse d'un flux"
date: "2012-07-25 11:21:00"
---
Pour faire des recherches de noms de fichiers correspondant à un certain pattern, j'ai eu besoin de changer la casse des noms...<br/><br/>Ici je recherche les fichiers qui contiennent "erreur" dans leur noms.  <code><pre><br />$ ls | tr '[:upper:]' '[:lower:]' | grep erreur<br /></pre></code>
