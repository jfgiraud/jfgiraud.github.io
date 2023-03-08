---
layout: post
title: "automatisation, créer un document pdf à partir d'une page web"
date: "2016-02-10 07:41:00"
tags: wkhtmltopdf phantomjs rasterize.js pdf
---
Il est facile de créer un document PDF à partir d'une page web.

Pour cela on peut utiliser le programme wkhtmltopdf


```bash 
$ wkhtmltopdf "http://mezalor-sc.blogspot.com" mezalor-sc.pdf
Loading page (1/2)
Printing pages (2/2)                                               
Done
```

ou bien phantomjs avec le script rasterize.js


```bash
phantomjs <( curl -s https://raw.githubusercontent.com/ariya/phantomjs/master/examples/rasterize.js ) http://mezalor-sc.blogspot.com mezalor-sc.pdf
```

A noter :

- wkhtmltopdf peut produire des documents avec des tailles de polices différentes entre 2 pages web d'un mếme site web (vu au travail), il coupait aussi une ligne entre deux pages du document pdf
- rasterize.js a produit un document PDF avec une police moins jolie que wkhtmltopdf chez moi 


