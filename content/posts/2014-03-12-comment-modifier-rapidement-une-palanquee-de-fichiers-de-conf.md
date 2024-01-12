---
title: "Comment modifier rapidement une palanquée de fichiers de conf..."
date: 2014-03-12T17:42:00+01:00
tags: ["bash"]
---

```
#!/bin/bash

cat <<EOF > container.tpl
	<Resource auth="Container"
           name="jdbc/configb"
           type="javax.sql.DataSource"
           factory="org.apache.tomcat.dbcp.dbcp.BasicDataSourceFactory"
           driverClassName="com.mysql.jdbc.Driver"
           url="jdbc:mysql://%s/%s"
           username="%s"
           password="%s"
           initialSize="0"
           maxActive="30"
           maxIdle="4"
           minIdle="0"
           maxWait="10000"
           poolPreparedStatements="true"
           testOnBorrow="true"
           timeBetweenEvictionRunsMillis="60000"
           numTestsPerEvictionRun="30"
           minEvictableIdleTimeMillis="180000"
           removeAbandoned="true"
           removeAbandonedTimeout = "60"
           logAbandoned="true"
           />
EOF

#\$0 pour ne pas interpreter...
cat <<EOF > container.awk
/name="jdbc\/3900"/ { gsub("jdbc/3900", "jdbc/data", \$0); }
match(\$0, /<Parameter name="mysql.host" value="(.+)" override="true"\/>/, m) { host=m[1]; next }
match(\$0, /<Parameter name="mysql.database" value="(.+)" override="true"\/>/, m) { database=m[1]; next }
match(\$0, /<Parameter name="mysql.username" value="(.+)" override="true"\/>/, m) { username=m[1]; next }
match(\$0, /<Parameter name="mysql.password" value="(.+)" override="true"\/>/, m) { password=m[1]; next }
/<\/Context>/ { 
	printf fmt, host, database, username, password;
	printf "\n";
}
1
EOF

for file in $*
do
    tofile=$(mktemp)
    awk -v fmt="$(cat container.tpl)" -f container.awk $file | xmllint --format --dropdtd - | grep -v '<?xml version="1.0"?>' > $tofile
    cat $tofile > $file
    rm -f $tofile
done

rm -f container.tpl container.awk
```

<div style="height: 0; overflow: hidden;">Resource dbcp BasicDataSourceFactory jdbc mysql awk match container format indent xmllint</div>
