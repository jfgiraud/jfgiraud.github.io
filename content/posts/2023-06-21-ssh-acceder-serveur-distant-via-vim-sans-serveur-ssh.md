---
title: "ssh, socat, accéder à des serveurs distant en utilisant un terminal sous Windows (pas de serveur ssh sur le poste Windows)"
date: 2023-06-21T07:10:00+01:00
tags: [ "ssh", "socat" ]
description: "ssh, socat, accéder à des serveurs distant en utilisant un terminal sous Windows (pas de serveur ssh sur le poste Windows)"
---

Dans la VM Windows :

```
ssh -N -R 2222:127.0.0.1:1337 moncuid@10.0.2.2
socat TCP-LISTEN:1337,reuseaddr,fork EXEC:bash,pty,stderr,setsid,sigint,sane
```

Dans le terminal Linux :

```
socat FILE:`tty`,raw,echo=0 TCP:localhost:2222
```

Source : https://blog.stalkr.net/2015/12/from-remote-shell-to-remote-terminal.html
Source : https://blog.arcoptimizer.com/comment-comprendre-le-tunneling-ssh-et-ses-cas-dutilisation