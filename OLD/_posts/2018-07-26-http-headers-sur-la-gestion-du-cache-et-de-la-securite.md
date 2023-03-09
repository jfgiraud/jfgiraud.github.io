---
title: "http, headers sur la gestion du cache et de la sécurité"
date: 2018-07-26T11:41:00+01:00
tags: ["http", "html", "cache", "securité"]
---

```java
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
