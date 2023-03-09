---
title: "Chemin absolu"
date: 2011-06-03T12:44:00+01:00
---
La commande readlink permet de retourner le chemin absolu d'un fichier/répertoire en suivant éventuellement les liens symboliques  
<pre><code>
$ readlink -f ~/.emacs
/home/user/etc/emacs/dot_emacs.el
</code></pre>
