---
layout: post
title: "bash, expansion de paramètres et indirection "
date: "2013-11-15 09:40:00"
---
Aujourd'hui, je viens de découvrir l'indirection de paramètres en bash.<br /><br />La syntaxe est la suivante : ${!PARAMETER}<br /><br />L'expansion ne donne pas la valeur du paramètre lui même mais la valeur du paramètre dont le nom est contenu dans PARAMETER.<br /><br /><script src="http://pastebin.com/embed_js.php?i=bRT22fTD"></script><br /><br />Cela permet de faire de jolies choses comme ceci en s'abstrayant d'eval...<br /><br /><script src="http://pastebin.com/embed_js.php?i=QqLJJqji"></script><br /><br />Ci-dessous une documentation bien claire sur l'expansion des paramètres en bash<br /><br /><a href="http://wiki.bash-hackers.org/syntax/pe">http://wiki.bash-hackers.org/syntax/pe</a><br /><br />
