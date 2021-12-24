---
layout: post
title: "docker, alpine, mariadb: Specified key was too long; max key length is 767 bytes"
date: "2020-12-02 10:10:00"
tags: docker alpine mariadb
---

Contourner l'erreur `Specified key was too long; max key length is 767 bytes` :

```bash
sed -e '/^\\[mysqld\\]/a innodb_strict_mode=0' \\
-e '/^\\[mysqld\\]/a innodb-default-row-format=dynamic' \\
-i /etc/my.cnf.d/mariadb-server.cnf
```
