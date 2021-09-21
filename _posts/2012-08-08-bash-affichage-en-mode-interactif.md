---
layout: post
title: "bash, affichage en mode intéractif"
date: "2012-08-08 13:17:00"
---
Dans un script bash, j'ai souhaité afficher un numéro de version lorsque celui-ci est lancé interactivement (ne reçoit pas de données depuis un pipe ou bien une redirection &lt;).<br/><br/>Cela peut-être fait en utilisant l'option -t de la commande test.   <code><pre><br />if [ -t 0 ]; then<br />    echo "Version: $VERSION"<br />fi<br /></pre></code>