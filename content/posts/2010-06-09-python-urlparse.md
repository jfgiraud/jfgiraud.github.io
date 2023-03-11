---
title: "Python - urlparse"
date: 2010-06-09T14:27:00+01:00
tags: [ "python", "parsing", "url" ]
description: "Snipset pour le parsing d'une url en python"
---

```text
$ python
>>> from urlparse import text
>>> o = urlparse('http://www.example.com:80/%7Eme/test.html;jsessionid=id?a=b&c=d#tag')
>>> o
ParseResult(scheme='http', netloc='www.example.com:80', path='/%7Eme/test.html', params='jsessionid=id', query='a=b&c=d', fragment='tag')
```
