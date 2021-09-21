---
layout: post
title: "Chemin absolu"
date: "2011-06-03 12:44:00"
---
La commande readlink permet de retourner le chemin absolu d'un fichier/répertoire en suivant éventuellement les liens symboliques  <br /><pre><code><br />$ readlink -f ~/.emacs<br />/home/user/etc/emacs/dot_emacs.el<br /></code></pre>
