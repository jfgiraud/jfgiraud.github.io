---
title: "socat, simuler un serveur http qui renvoie toujours le même fichier"
date: 2014-02-11T10:23:00+01:00
tags: ["socat", "tcp", "listen", "reuseaddr", "fork", "example", "file", "serve"]
---



```
socat TCP-LISTEN:1231,crlf,reuseaddr,fork SYSTEM:"echo HTTP/1.0 200; echo Content-Type\: text/xml; echo; cat /path/to/the/file.xml"
```

<div style="height: 0; overflow: hidden;">socat tcp listen reuseaddr fork example file serve</div>
