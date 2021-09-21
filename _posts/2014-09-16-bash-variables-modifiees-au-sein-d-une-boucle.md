---
layout: post
title: "bash, variables modifiées au sein d'une boucle"
date: "2014-09-16 06:07:00"
---
Il y a quelques temps déjà, je m'étais cassé la tête sur des variables que je modifiais dans une boucle et dont les modifications avaient disparues une fois sorti de celle-ci.<br /><br />Cela s'expliquait par le fait que les variables étaient dans un sous-processus et non dans le process courrant.<br /><br />La bonne syntaxe pour modifier des variables au sein d'une boucle while est la suivante :<br /><br /><script src="https://pastebin.com/embed_js/jcr2UaEJ"></script><br /><br />Il faut passer par <code>done &lt; ...</code> et non <code>... | while</code>
