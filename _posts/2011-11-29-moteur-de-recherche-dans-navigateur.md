---
layout: post
title: "Moteur de recherche dans navigateur"
date: "2011-11-29 11:22:00"
tags: open search description moteur recherche navigateur
---
Il est relativement simple de permettre à un site web de proposer un moteur de recherche dans le navigateur d'un client...

Pour cela il faut proposer un fichier mysearch.xml


```xml
<?xml version="1.0"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/">
  <ShortName>mysearch</ShortName>
  <Description>Ma petite description</Description>
  <Image height="16" width="16" type="image/x-icon">http://yoursite.example.com/favicon.ico</Image>
  <Url type="text/html" method="get" template="http://yoursite.example.com/search?q={searchTerms}"/>
</OpenSearchDescription>
```

Et le proposer dans votre page html via la balise link


```html
<html>
<head>
<title>Example - Moteur de recherche OpenSearch</title>
<link rel="search" type="application/opensearchdescription+xml" href="mysearch.xml" title="mysearch" />
</head>
<body>
Votre page...
</body>
</html>
```

