---
title: "docker, alpine, mariadb: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: Communications link failure"
date: "2020-12-02 10:09:00"
tags: docker alpine mariadb
---
La connexion se fait en ligne de commande mais pas depuis les tests unitaires lancés par maven.  

```text
sed -e '/^skip-networking/c #skip-networking' -i /etc/my.cnf.d/mariadb-server.cnf 
```

Source: [https://stackoverflow.com/a/2985169/3550759](https://stackoverflow.com/a/2985169/3550759)
