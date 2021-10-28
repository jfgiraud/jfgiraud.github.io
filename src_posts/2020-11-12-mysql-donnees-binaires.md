---
layout: post
title: "mysql, données binaires"
date: "2020-11-12 15:47:00"
---
Dans certains cas, la commande LOAD_FILE n'est pas utilisable (problèmes de droits, etc..) pour alimenter un blob.<br/><br/> Dans ce cas, il peut être intéressant de convertir un fichier binaire (ici un fichier texte) en séquence hexadécimale...<br/><br/> <script src="https://pastebin.com/embed_js/CgdzECcm"></script> <br/>et utiliser cette séquence hexadécimale pour faire sa requête mysql.<br/><br/> On utilisera alors la commande UNHEX pour décoder la séquence hexadécimale et la remettre en binaire dans la requête SQL.<br/><br/> <script src="https://pastebin.com/embed_js/wnraYXCF"></script> <br/><br/> Le <kbd>xxd -p</kbd> permet de ne sortir que l'hexa sur la sortie standard tandis que le <kbd>tr -d '\n</kbd> concatène les lignes.
