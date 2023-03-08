---
title: "stat, différence entre modify et change"
date: "2013-01-31 12:11:00"
---
Quelle est la différence entre modify et change dans le retour de la commande stat ?


```
$ svn st | awk '/^M/ && /.java$/ {print $2}' | xargs stat
  File: «VxmlStatistiquesServletService.java»
  Size: 10248     	Blocks: 24         IO Block: 4096   fichier
Device: 807h/2055d	Inode: 5770813     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/mee)   Gid: ( 1000/mee)
Access: 2013-01-30 16:58:57.208953609 +0100
Modify: 2013-01-30 16:58:57.198953609 +0100
Change: 2013-01-30 16:58:57.198953609 +0100
  File: «VxmlGlobalServletService.java»
  Size: 64632     	Blocks: 128        IO Block: 4096   fichier
Device: 807h/2055d	Inode: 5774444     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/mee)   Gid: ( 1000/mee)
Access: 2013-01-30 16:54:35.098953459 +0100
Modify: 2013-01-30 16:54:35.078953459 +0100
Change: 2013-01-30 16:54:35.078953459 +0100
```



- Modify - indique quand le fichier a été modifié la dernière fois (le contenu a été modifié)
- Change - indique la dernière fois que les meta données du fichier ont été changées (exemple permissions)



