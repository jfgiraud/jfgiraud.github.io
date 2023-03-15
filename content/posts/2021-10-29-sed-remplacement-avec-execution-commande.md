---
title: "sed, remplacement avec exécution commande"
date: 2021-10-29T10:07:00+01:00
tags: [ "sed", "curl" ]
description: "Exécutez une commande dans sed"
---

Dans le code ci-dessous, imaginez que la partie avant le pipe soit une page contenant différents liens `pastebin`. Le `sed` cherche ces liens et exécute une commande pour les remplacer par leurs contenus.

J'ai utilisé cette commande pour migrer vers `github.io`.

```
$  echo "https://pastebin.com/embed_js/sVDYnaUX" | sed -r 's#https://pastebin.com/embed_js/(\w+)#curl -s https://pastebin.com/raw/\1#e'
public static void addNoCacheHeaders(HttpServletResponse resp) {
resp.addHeader(HttpHeaders.CACHE_CONTROL, "max-age=0, no-store, no-cache, must-revalidate, proxy-revalidate, private");
resp.addHeader(HttpHeaders.PRAGMA, "no-cache");
resp.addHeader(HttpHeaders.EXPIRES, "-1");
}

public static void addSecurityHeaders(HttpServletResponse resp) {
resp.addHeader(HttpHeaders.X_FRAME_OPTIONS, "DENY");
resp.addHeader(HttpHeaders.X_XSS_PROTECTION, "1; mode=block");
resp.addHeader(HttpHeaders.X_CONTENT_TYPE_OPTIONS, "nosniff");
}
```
