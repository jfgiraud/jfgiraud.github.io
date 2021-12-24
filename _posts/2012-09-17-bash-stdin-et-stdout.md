---
layout: post
title: "bash, stdin et stdout"
date: "2012-09-17 10:33:00"
tags: bash, stdout, stderr, write, io, redirections
---
Un petit rappel sur les redirections.

Le document [http://tldp.org/LDP/abs/html/io-redirection.html#IOREDIRREF](http://tldp.org/LDP/abs/html/io-redirection.html#IOREDIRREF) est très bien aussi. 


```bash
$ ( echo quelque chose sur stderr >&2; echo autre chose sur stdout ) > /dev/null
quelque chose sur stderr
$ ( echo quelque chose sur stderr >&2; echo autre chose sur stdout ) 2> /dev/null
autre chose sur stdout
$ ( echo quelque chose sur stderr >&2; echo autre chose sur stdout ) &> /dev/null
$
```

