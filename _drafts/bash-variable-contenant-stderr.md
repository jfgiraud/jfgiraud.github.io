---
layout: post
title: "bash, variable contenant stderr"
date: "2020-11-23 18:03:00"
---
inverser stdin, stderr    stderr=$(../bin/sql-connect.sh -e -k 'xxxxx' <<< 'select value from _migrate_db where name="version";' 3>&2 2>&1 1>&3-)   status=$?   assert "[[ \"$stderr\" == '*configuration not found*' ]]" "bad stderr (actual=$stderr)" 
