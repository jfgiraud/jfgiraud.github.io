---
title: "SVN: ignorer un fichier lors du commit"
date: 2008-03-21T16:10:00+01:00
tags: ["svn", "propset", "ignore"]
description: "Comment faire pour que SVN ignore un fichier ?"
---

```bash
$ pwd
/home/myuser/appli
$ touch a_file
$ svn st
? a_file
$ svn propset svn:ignore a_file .
$ svn st
$
```
