---
title: "bash, récupérer le code de sortie d'un sous-shell"
date: 2012-07-31T11:18:00+01:00
tags: ["bash", "pipe", "status"]
---
Ci-dessous on récupère le code de sortie d'un sous-shell afin d'effectuer un traitement particulier avec des pipes. 

 
```bash
MYSQL_CMD="mysql -P$DB_PORT -u$DB_USER -p$DB_PASSWD -h$DB_HOST $DB --connect-timeout=1"
VERSION=$(${MYSQL_CMD} -B -s -e 'select value from _cvf_metadatas where name="version"' 2>/dev/null | tail -n 1 ; exit $PIPESTATUS)
if [ $? -ne 0 ]; then 
    VERSION="*can't connect*"
elif [ -z "$VERSION" ]; then
    VERSION="*not found*"
fi
```
