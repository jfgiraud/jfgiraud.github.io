---
title: "socat, sert de proxy et passe le plat..."
date: "2013-12-26 14:59:00"
---
Sur un de mes projets, un flux a été interrompu... en attendant sa réouverture j'utilise un proxy qui sert de passe plat
depuis une machine où le flux en question est ouvert...


```
# le serveur écoute sur le port 1231 et passe le plat à somewhere.example.com:80
socat TCP-LISTEN:1231,reuseaddr,fork TCP:somewhere.example.com:80
```

<div style="height: 0; overflow: hidden;">socat tcp listen reuseaddr fork example proxy</div>
