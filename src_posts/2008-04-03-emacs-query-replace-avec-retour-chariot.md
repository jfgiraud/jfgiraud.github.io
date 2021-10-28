---
layout: post
title: "emacs : query replace avec retour chariot !"
date: "2008-04-03 11:05:00"
---
Ayant un document xml avec plein de données, je souhaite séparer les blocs "&lt;Event&gt;<event>" pour mieux distinguer. Voici comment faire...<br /><br /></event><br /><pre>M-%<br />&lt;Event&gt;<br /><event>C-q C-j C-q C-j </event>&lt;Event&gt;<br /><br /><br /></pre>
