---
layout: post
title: "mysql, supprimer les mysql: [Warning] Using a password on the command line interface can be insecure."
date: "2020-04-25 17:44:00"
---
```
$ mysql -u test -ptest -h localhost MYdatabase
mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.

# Solution 1 : utilise une variable d'environnement
$ MYSQL_PWD=test mysql -u test -h localhost MYdatabase

# Solution 2 : utilise sshpass
$ sshpass -ptest mysql -u test -p -h localhost MYdatabase

# Solution 3 : ne modifie pas les fd
$ (((((mysql -u test -ptest -h localhost MYdatabase) 1>&9) 2>&1)|grep -vF 'mysql: [Warning] Using a password on the command line interface can be insecure.') 1>&2 ) 9>&1

# Solution 4 : passer par expect
$ expect -c 'spawn mysql -u test -p -h localhost MYdatabase ; expect "Enter password:" ; send "test\n" ; interact'
```


En bash une solution plus simple existe équivalente à la solution 3 :

```
# Solution 3 : ne modifie pas les fd (plus simple en bash)
$ mysql -u test -ptest -h localhost MYdatabase 2> >(grep -vF 'mysql: [Warning] Using a password on the command line interface can be insecure.' 1>&2 )
```

