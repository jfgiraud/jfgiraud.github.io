---
title: "sniffage réseau"
date: 2011-08-12T11:55:00+01:00
tags: ["sniffage", "réseau", "network", "ngrep"]
description: "Sniffer le réseau avec ngrep"
---

```
$ sudo ngrep -x '^(GET|POST)' 'src host somewhere.example.com and port 80'
interface: eth0 (10.33.2.0/255.255.255.0)
filter: (ip or ip6) and ( src host somewhere.example.com and port 80 )
match: ^(GET|POST)
#########
T 10.33.99.21:33050 -> 10.33.2.87:80 [AP]
50 4f 53 54 20 2f 68 65 6c 6c 6f 20 48 54 54 50 POST /hello HTTP
2f 31 2e 30 0d 0a /1.0..
```    

Sur somewhere.example.com 


```
$ telnet here 80 
POST /hello HTTP/1.0
```

EDIT: essayer -d lo si besoin 


```
$ sudo ngrep -d lo -x '^(POST)' 'port 8080'
```
