---
layout: post
title: "html/java, input file sympa avec bootstrap"
date: "2014-01-28 13:50:00"
---
Dans le cadre d'un projet, j'ai redesigné un formulaire qui permet d'importer un fichier csv (utilise bootstrap).<br /><br />Le rendu est le suivant :<br /><br /><div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-GbpePebl9sw/Uuek_yww54I/AAAAAAAADuw/gMzZw1TdYRA/s1600/Untitled.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-GbpePebl9sw/Uuek_yww54I/AAAAAAAADuw/gMzZw1TdYRA/s320/Untitled.png" /></a></div><br />Le code HTML utilisé est le suivant :<br /><br /><script src="http://pastebin.com/embed_js.php?i=CD00ksSn"></script><br /><br />Le code java est le suivant (attention, lorsque le type du formulaire est enctype="multipart/form-data", les paramètres ne se récupèrent plus avec HttpServletRequest.getParameter):<br /><br /><script src="http://pastebin.com/embed_js.php?i=aDMX7AUq"></script><br /><br />
