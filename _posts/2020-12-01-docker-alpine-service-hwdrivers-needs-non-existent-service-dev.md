---
layout: post
title: "docker, alpine, Service `hwdrivers' needs non existent service `dev'"
date: "2020-12-01 09:44:00"
tags: docker alpine mariadb
---

```text
# Avoid Service `hwdrivers' needs non existent service `dev'
#/ # rc-status
# * Caching service dependencies ...
#Service `hwdrivers' needs non existent service `dev' [ ok ]
#Runlevel: sysinit

RUN apk add udev-init-scripts-openrc
```