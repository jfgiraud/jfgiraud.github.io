---
layout: post
title: "automatisation, créer un document pdf à partir d'une page web"
date: "2016-02-10 07:41:00"
---
Il est facile de créer un document PDF à partir d'une page web.<br /><br />Pour cela on peut utiliser le programme wkhtmltopdf<br /><br /><script src="//pastebin.com/embed_js/CdSghvxB"></script><br /><br />ou bien phantomjs avec le script rasterize.js<br /><br /><script src="//pastebin.com/embed_js/v7tfRHHG"></script><br /><br />A noter :<br /><ul><li>wkhtmltopdf peut produire des documents avec des tailles de polices différentes entre 2 pages web d'un mếme site web (vu au travail), il coupait aussi une ligne entre deux pages du document pdf<br /><li>rasterize.js a produit un document PDF avec une police moins jolie que wkhtmltopdf chez moi <br /></ul><div style="height: 0; overflow: hidden;">wkhtmltopdf, phantomjs, rasterize.js, pdf</div>