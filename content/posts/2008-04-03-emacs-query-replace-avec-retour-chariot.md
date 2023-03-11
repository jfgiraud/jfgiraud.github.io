---
title: "emacs : query replace avec retour chariot !"
date: 2008-04-03T11:05:00+01:00
tags: [ "emacs", "manipilation" ]
description: "Utiliser des retours chariot lors des remplacements emacs"
---

Ayant un document XML avec plein de données, je souhaite séparer les blocs "&lt;Event&gt;<event>" pour mieux distinguer. Voici comment faire...

    <pre>M-%
    &lt;Event&gt;
    <event>C-q C-j C-q C-j </event>&lt;Event&gt;
