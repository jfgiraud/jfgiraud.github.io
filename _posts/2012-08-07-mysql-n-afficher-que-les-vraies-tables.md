---
layout: post
title: "mysql, n'afficher que les vraies tables"
date: "2012-08-07 11:49:00"
---
Lorsque l'on utilise plusieurs bases de données, il arrive que l'on crée des vues d'une base vers une autre base...<br/><br/>La commande "show tables" n'est pas suffisante pour distinguer les tables des vues... <br/>Mais voilà, on peut associer l'option full et compléter d'un where pour récupérer ce que l'on souhaite :  <pre><code><br />mysql> show full tables where Table_type='BASE TABLE';<br /></code></pre> où Table_type peut être : <ul><li>BASE TABLE <li>VIEW </ul>