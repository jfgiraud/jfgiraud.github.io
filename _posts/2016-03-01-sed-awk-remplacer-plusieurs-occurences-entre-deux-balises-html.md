---
layout: post
title: "sed/awk, remplacer plusieurs occurences entre deux balises html"
date: "2016-03-01 11:27:00"
---
<script src="//pastebin.com/embed_js/h27EE9Gu"></script><br /><br />Attention, il faut prendre garde au cas où les tags html ne seraient pas uniques :<br /><br /><script src="//pastebin.com/embed_js/TeUKkfEA"></script><br /><br />Si on a la chance que le tag de fin est sur la même ligne :<br /><br /><script src="https://pastebin.com/embed_js/m5S5JUH2"></script><br /><br />Toutefois, je conseille de préférer <kbd>awk</kbd> dont le comportement est plus sûr.<br /><br /><script src="//pastebin.com/embed_js/n5L0dzWr"></script>