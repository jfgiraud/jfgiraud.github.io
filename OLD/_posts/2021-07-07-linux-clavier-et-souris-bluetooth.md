---
title: "linux, clavier et souris bluetooth"
date: "2021-07-07 22:32:00"
tags: bluetooth
---

Procédure pour appairer clavier &amp; souris bluetooth sur linux.  

```text
$ bluetoothctl
> scan on
[NEW] Device D8:2A:5E:FB:5C:9C Trackpad de System Administrator
> pair D8:2A:5E:FB:5C:9C
> connect D8:2A:5E:FB:5C:9C
> trust D8:2A:5E:FB:5C:9C
[NEW] Device 60:BF:42:05:D6:33 Keyboard de System Administrator
> pair 60:BF:42:05:D6:33
[agent] PIN code: 899777
[CHG] Device 60:BF:42:05:D6:33 Paired: yes
Pairing successful
> connect 60:BF:42:05:D6:33
> trust 60:BF:42:05:D6:33
> quit
```
