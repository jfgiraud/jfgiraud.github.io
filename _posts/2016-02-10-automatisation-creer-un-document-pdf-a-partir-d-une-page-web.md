---
layout: post
title: "automatisation, créer un document pdf à partir d'une page web"
date: "2016-02-10 07:41:00"
---
Il est facile de créer un document PDF à partir d'une page web.

Pour cela on peut utiliser le programme wkhtmltopdf

<script src="//pastebin.com/embed_js/CdSghvxB"></script>

ou bien phantomjs avec le script rasterize.js

<script src="//pastebin.com/embed_js/v7tfRHHG"></script>

A noter :


- wkhtmltopdf peut produire des documents avec des tailles de polices différentes entre 2 pages web d'un mếme site web (vu au travail), il coupait aussi une ligne entre deux pages du document pdf
- rasterize.js a produit un document PDF avec une police moins jolie que wkhtmltopdf chez moi 


<div style="height: 0; overflow: hidden;">wkhtmltopdf, phantomjs, rasterize.js, pdf</div>
