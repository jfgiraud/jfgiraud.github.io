---
layout: post
title: "grep, extraire des données"
date: "2021-03-04 14:50:00"
---
Il est possible d'utiliser grep pour extraire des données. Dans l'exemple qui suit, on récupère le nom des compagnies dans un fichier json.   <script src="https://pastebin.com/embed_js/hbJAtY97"></script> L'option <kbd>-P</kbd> active la compatibilité aux regexp PERL, le <kbd>-o</kbd> la récupération du terme matché et enfin le <kbd>\K</kbd> la suppression de la partie gauche dans le terme matché.  <script src="https://pastebin.com/embed_js/Cxurb7as"></script> C'est plus simple que sed ou awk mais apparemment, le <kbd>-P</kbd> ne serait pas supporté sur toutes les distributions. 