---
layout: post
title: "wget, récupérer un site "
date: "2016-01-25 10:58:00"
---
Petite commande utilisée dans le cadre de mon projet pour récupérer l'ensemble de tests fitnesse afin de les packager et les livrer au client.


```
wget -k -p -r -l inf http://localhost:7575/MonSvi  --reject-regex '.*(/FitNesse|/files/|[?]).*'


-r
--recursive
Turn on recursive retrieving.    The default maximum depth is 5.

-l depth
--level=depth
Specify recursion maximum depth level depth.

-k
--convert-links
After the download is complete, convert the links in the document to make them suitable for local viewing.  This affects not only the visible hyperlinks, but any part of the document that links to external content, such as embedded images, links to style sheets, hyperlinks to non-HTML content, etc.

-p
--page-requisites
This option causes Wget to download all the files that are necessary to properly display a given HTML page.  This includes such things as inlined images, sounds, and referenced stylesheets.

--accept-regex urlregex
--reject-regex urlregex
Specify a regular expression to accept or reject the complete URL.
```

<div style="height: 0; overflow: hidden;">wget, fitnesse, web</div>
