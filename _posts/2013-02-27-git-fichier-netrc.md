---
layout: post
title: "Git, fichier .netrc"
date: "2013-02-27 23:45:00"
---
Il y a plusieurs mois, j'ai découvert l'existence du fichier .netrc et l'utilisation que l'on peut en faire.<br /><br />Dans le cadre de l'un de mes projets, j'y ai stocké les informations de connexion vers le wiki de l'entreprise à des fins de scripting.<br /><br />En python, la lecture se fait simplement en utilisant le module netrc.<br /><br />Aujourd'hui, je viens de découvrir que git peut l'utiliser afin d'éviter d'avoir à retaper son login et mot de passe à chaque push...<br /><br /><script src="http://pastebin.com/embed_js.php?i=d5K8xe60"></script><br /><br />Ce fichier me plaît bien : centralisation et simplicité :) 