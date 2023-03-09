---
title: "Droits sql..."
date: 2011-12-01T11:39:00+01:00
tags: ["grant", "insert", "select", "on", "mysql", "user", "privileges", "flush"]
---
Pour générer les commandes SQL adéquates pour 3 types d'utilisateurs de la BD avec les grant mysql qui vont bien.
 
```
function echo_grant_privileges() {
  local db=$1
  local db_user=$2
  local pswd_ro=${db_user}ro
  local pswd_rw=${db_user}rw
  local pswd_adm=${db_user}adm
  echo "GRANT SELECT ON $db.* TO ${db_user}ro identified by '${pswd_ro}';"
  echo "GRANT SELECT,INSERT,UPDATE,DELETE ON $db.* TO ${db_user}rw identified by '${pswd_rw}';"
  echo "GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES, CREATE VIEW, SHOW VIEW ON $db.* TO ${db_user}adm identified by '${pswd_adm}';"
  echo "flush privileges;"
}


$ echo_grant_privileges db toto
GRANT SELECT ON db.* TO totoro identified by 'totoro';
GRANT SELECT,INSERT,UPDATE,DELETE ON db.* TO totorw identified by 'totorw';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,INDEX,ALTER,CREATE TEMPORARY TABLES,LOCK TABLES, CREATE VIEW, SHOW VIEW ON db.* TO totoadm identified by 'totoadm';
```

