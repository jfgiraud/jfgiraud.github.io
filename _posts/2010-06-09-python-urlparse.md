---
layout: post
title: "Python - urlparse"
date: "2010-06-09 14:27:00"
---
<pre><br />>>> from urlparse import urlparse<br />>>> o = urlparse('http://www.example.com:80/%7Eme/test.html;jsessionid=id?a=b&c=d#tag')<br />>>> o<br />ParseResult(scheme='http', netloc='www.example.com:80', <br />path='/%7Eme/test.html', params='jsessionid=id', <br />query='a=b&c=d', fragment='tag')<br /></pre>
