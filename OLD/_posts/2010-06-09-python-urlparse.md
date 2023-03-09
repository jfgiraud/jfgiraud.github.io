---
title: "Python - urlparse"
date: 2010-06-09T14:27:00+01:00
---
<pre>
>>> from urlparse import urlparse
>>> o = urlparse('http://www.example.com:80/%7Eme/test.html;jsessionid=id?a=b&c=d#tag')
>>> o
ParseResult(scheme='http', netloc='www.example.com:80', 
path='/%7Eme/test.html', params='jsessionid=id', 
query='a=b&c=d', fragment='tag')
</pre>
