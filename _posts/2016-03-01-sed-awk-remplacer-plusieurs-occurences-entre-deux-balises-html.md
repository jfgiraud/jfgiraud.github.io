---
layout: post
title: "sed/awk, remplacer plusieurs occurences entre deux balises html"
date: "2016-03-01 11:27:00"
---
<script src="https://pastebin.com/embed_js/h27EE9Gu"></script>

Attention, il faut prendre garde au cas où les tags html ne seraient pas uniques :

<script src="https://pastebin.com/embed_js/TeUKkfEA"></script>

Si on a la chance que le tag de fin est sur la même ligne :

<script src="https://pastebin.com/embed_js/m5S5JUH2"></script>

Toutefois, je conseille de préférer `awk` dont le comportement est plus sûr.

<script src="https://pastebin.com/embed_js/n5L0dzWr"></script>
