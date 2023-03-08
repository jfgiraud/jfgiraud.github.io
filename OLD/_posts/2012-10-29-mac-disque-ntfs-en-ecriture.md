---
title: "mac, disque ntfs en écriture"
date: "2012-10-29 22:42:00"
---
Grrr, apple bloque tout. Le disque Western Digital que je viens d'acheter se monte directement mais n'est visible du finder qu'en lecture seulement !

C'est rageant.

Il y a des solutions tierces telles que paragon-software.com et tuxera.com mais c'est payant :(

J'ai quand même fait quelques explorations et il s'avère qu'on peut bien monter le disque en lecture/écriture sans passer par la caisse :


```
$ sudo umount /Volumes/WD1TO
$ mkdir /Volumes/WD1TO
$ sudo mount -t ntfs -o nodev,nosuid,noowners,rw /dev/disk2s1 /Volumes/WD1TO
$ echo hello the world > /Volumes/WD1TO/example
$ cat /Volumes/WD1TO/example
hello the world
```

J'ai lancé une copie de 200Go de données, je verai bien si tout passe.

Note: ça passe sur mon mac mini avec Mac OS 10.6.8 :) 

<div style="height: 0; overflow: hidden;">sudo, mount, ntfs, rw</div>
