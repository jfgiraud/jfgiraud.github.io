---
layout: post
title: "docker, alpine, mariadb: ce qui m'a été nécessaire..."
date: "2020-12-02 10:16:00"
tags: docker alpine mariadb
---

Voici ce qui m'a été nécessaire :

```text
#!/bin/bash

apk add openrc

# Avoid Service `hwdrivers' needs non existent service `dev'
#/ # rc-status
# * Caching service dependencies ...
#Service `hwdrivers' needs non existent service `dev' [ ok ]
#Runlevel: sysinit
apk add udev-init-scripts-openrc

apk add mariadb mariadb-client mariadb-server-utils pwgen
mysql_install_db --user=mysql --ldata=/var/lib/mysql

# com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure
# due to : skip-networking
# https://stackoverflow.com/a/2985169/3550759
#
# Specified key was too long; max key length is 767 bytes
# due to : innodb-default-row-format && (maybe) innodb_strict_mode
sed -e '/^\\[mysqld\\]/a innodb_strict_mode=0' \\
-e '/^\\[mysqld\\]/a innodb-default-row-format=dynamic' \\
-e '/^\\[mysqld\\]/a sql-mode="ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"' \\
-e '/^skip-networking/c #skip-networking' \\
-i /etc/my.cnf.d/mariadb-server.cnf
rc-update add mariadb && mkdir -p /run/openrc/ && touch /run/openrc/softlevel
```

Attention, ça ne démarre pas étrangement si on ne fait pas le `rc-status` auparavent...

```text
rc-status
rc-service mariadb start
``` 
