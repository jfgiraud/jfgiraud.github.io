---
title: "SVN, ignorer des fichiers"
date: "2013-03-06 12:38:00"
---
Pour ignorer plusieurs fichiers lors des commits SVN


```
#!/bin/bash

cd $(dirname $(readlink -f $0))/..

svnignorefile=$(mktemp)

cat >> $svnignorefile <<EOF
.classpath
.project
bin
target
*.tgz
EOF

svn propset svn:ignore -F $svnignorefile .

rm -f $svnignorefile

svn commit -m 'svn ignore'
```

Une page qui explique bien&nbsp;[http://www.math-linux.com/spip.php?article111](http://www.math-linux.com/spip.php?article111) 

<div style="height: 0; overflow: hidden;"><span class="kw2">svn propset</span> svn:ignore <span class="re5">-F mktemp</span> temp fichier temporaire</div>
