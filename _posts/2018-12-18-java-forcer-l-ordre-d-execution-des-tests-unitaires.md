---
layout: post
title: "java, forcer l'ordre d'exécution des tests unitaires"
date: "2018-12-18 11:59:00"
---
Parfois, des tests unitaires plantent lorsqu'ils sont exécutés dans un certain ordre.<br /><br />Aujourd'hui, c'est le cas et pour reproduire le problème, j'ai utilisé cette annotation qui permet de spécifier l'ordre que l'on souhaite utiliser lors de l'exécution de tous les tests de la classe.<br /><br /><script src="https://pastebin.com/embed_js/FqxuEzGi"></script><br /><br />Source : <a href="https://github.com/junit-team/junit4/wiki/Test-execution-order">https://github.com/junit-team/junit4/wiki/Test-execution-order</a>