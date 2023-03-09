---
title: "docker, alpine, Service hwdrivers needs non existent service dev"
date: 2020-12-01T09:44:00+01:00
tags: ["docker", "alpine", "mariadb"]
---

Voici comment résoudre `Avoid Service hwdrivers needs non existent service dev`

```
# Avoid Service `hwdrivers' needs non existent service `dev'
#/ # rc-status
# * Caching service dependencies ...
#Service `hwdrivers' needs non existent service `dev'               [ ok ]
#Runlevel: sysinit

RUN apk add udev-init-scripts-openrc
```