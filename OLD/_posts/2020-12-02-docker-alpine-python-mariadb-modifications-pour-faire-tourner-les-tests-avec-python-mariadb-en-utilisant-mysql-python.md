---
layout: post
title: "docker, alpine, python, mariadb : Modifications pour faire tourner les tests avec python / mariadb en utilisant MySQL-python"
date: "2020-12-02 11:11:00"
tags: docker alpine mariadb
---

Erreurs vues et paquets installés : 

```bash
apk add python3 python3-dev py3-virtualenv
apk add python2 python2-dev
apk add mariadb-dev

#error: command 'gcc' failed with exit status 1
#  ----------------------------------------
#  ERROR: Failed building wheel for MySQL-python
apk add gcc

#19 | #include <limits.h>
#   |          ^~~~~~~~~~
#    compilation terminated.
#    error: command 'gcc' failed with exit status 1
apk add libc-dev

#_mysql.c: In function '_mysql_ConnectionObject_ping':
#_mysql.c:1804:41: error: 'MYSQL' {aka 'struct st_mysql'} has no member named 'reconnect'
#1804 |  if ( reconnect != -1 ) self->connection.reconnect = reconnect;
#     |                                         ^
#error: command 'gcc' failed with exit status 1
#https://github.com/DefectDojo/django-DefectDojo/issues/407#issuecomment-415862064
sed '/st_mysql_options options;/a unsigned int reconnect;' /usr/include/mysql/mysql.h -i.bkp
```