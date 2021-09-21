---
layout: post
title: "ssh & scripts automatisés, The authenticity of host can't be established"
date: "2017-05-23 10:15:00"
---
Lors d'appels de scripts automatisés pour "calculer" ce qui est à mettre en préproduction, j'ai souvent des "The authenticity of host can't be established".<br />Peut-être parce que la machine est puppétisée...<br /><br />Soit il faut répondre manuellement, soit il faut éviter d'avoir le prompt...<br /><br />Pour éviter d'avoir à répondre, on peut ajouter l'option "-o StrictHostKeyChecking=no" à ses commandes SSH.<br /><br /><script src="https://pastebin.com/embed_js/r4U3Ak1X"></script><br /><br />Ce n'est pas beau, certes...<br /><br />Source : <a href="https://stackoverflow.com/questions/28461713/how-to-ignore-or-pass-yes-when-the-authenticity-of-host-cant-be-established-i">stackoverflow</a>