---
layout: post
title: "bash, lecture ligne à ligne et initialisation variables..."
date: "2012-08-07 14:55:00"
---
Dans la lignée du post précédent, il est possible de lire ligne à ligne et d'initialiser des variables directement pour des fichiers bien structurés.<br/><br/>Dans le cas d' /etc/password : <code><pre><br />$ while IFS=: read user pass uid gid full home shell        <br />> do        <br />>   printf "$full -- Pseudo : $user UID : $uid GID : $gid Home : $home Shell : $shell\n"        <br />> done < /etc/passwd<br />root -- Pseudo : root UID : 0 GID : 0 Home : /root Shell : /bin/bash<br />daemon -- Pseudo : daemon UID : 1 GID : 1 Home : /usr/sbin Shell : /bin/sh<br />bin -- Pseudo : bin UID : 2 GID : 2 Home : /bin Shell : /bin/sh<br />sys -- Pseudo : sys UID : 3 GID : 3 Home : /dev Shell : /bin/sh<br /></pre></code>
