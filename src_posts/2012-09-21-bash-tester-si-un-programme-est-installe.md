---
layout: post
title: "bash, tester si un programme est installé"
date: "2012-09-21 10:03:00"
---
Pour tester si un programme est installé, on peut utiliser la commande <tt>which</tt><br />de différentes manières.<br /><br />La première en comptabilisant le nombre de lignes retournées.<br /><br /><script src="http://pastebin.com/embed_js.php?i=zYiQWwVn"></script><br /><br />La seconde en utilisant le code de retour de la commande.<br /><br /><script src="http://pastebin.com/embed_js.php?i=cU9AC5Qy"></script><br /><br /><div style="overflow:hidden; height:0;">which, apt-get install, sudo</div><br />La seconde est plus lisible, pas besoin de décrypter. <br /><br />C'est seulement dommage qu'on ne puisse pas ajouter un paramètre à la commande pour ne pas écrire sur la sortie standard et que l'on soit obligé de rediriger dans <tt>/dev/null</tt>.<br /><br />A chacun sa préférence. 
