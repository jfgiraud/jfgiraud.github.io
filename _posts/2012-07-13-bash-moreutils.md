---
layout: post
title: "bash, moreutils"
date: "2012-07-13 11:18:00"
---
Je viens de découvrir un paquet mettant à disposition des outils bien sympathiques pour faciliter l'écriture de scripts bash.  Il s'agit du paquet moreutils  <code><pre><br />$ sudo apt-get install moreutils<br /></pre></code> Exemples d'utilisation :  <code><pre><br />Pour envoyer un mail si des données sont lues sur l'entrée standard...<br />$ find . -name core | ifne mail -s "Core files found" root<br /><br />Pour réécrire dans un même fichier sans avoir à créer un fichier temporaire...<br />$ sed '...' file | grep '...' | sponge file<br /></pre></code>
