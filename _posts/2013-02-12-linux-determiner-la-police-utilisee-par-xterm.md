---
layout: post
title: "Linux, déterminer la police utilisée par xterm"
date: "2013-02-12 15:23:00"
---
On peut utiliser appres qui affiche la liste des ressources utilisées par xterm.

Dans mon cas :

<script src="https://pastebin.com/embed_js/9qz751z9"></script>


Donc, si je veux utiliser la même police dans un autre terminal, je n'ai plus qu'à utiliser : -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso10646-1

<div style="height: 0; overflow: hidden;">appres pacman xterm</div>

