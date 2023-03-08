---
title: "docker, tests karma dans un container docker"
date: "2020-06-22 16:13:00"
tags: docker karma container
---
Je suis novice en docker / gitlab ci/cd mais je m'y mets depuis la semaine dernière. 

Mon ancienne machine de dév avait été transformée en jenkins. Elle a son disque qui a "cramé" et c'est donc  l'occasion de changer de technologie...

Le projet supervisé a des tests karma.
Lors du portage sur git ci/cd, les tests étaient gelés jusqu'au claquage d'un timeout (cf traces ci-après). 
Ca ne se passait que dans gitlab ci/cd. En local, hors du container docker tout était OK, dans le container, c'était KO



```text
karma start /root/xxxx/xxxxx-webapp/karma.unit.conf.js --single-run
22 06 2020 12:40:44.815:WARN [config]: "/" is proxied, you should probably change urlRoot to avoid conflicts 
22 06 2020 12:40:44.940:INFO [karma]: Front-end scripts not present. Compiling... 
22 06 2020 12:40:45.416:INFO [karma]: Karma v2.0.0 server started at http://0.0.0.0:9876/ 
22 06 2020 12:40:45.416:INFO [launcher]: Launching browser firefox_headless with unlimited concurrency 
22 06 2020 12:40:45.423:INFO [launcher]: Starting browser Firefox 
22 06 2020 12:41:45.484:WARN [launcher]: Firefox have not captured in 60000 ms, killing. 
22 06 2020 12:41:47.487:WARN [launcher]: Firefox was not killed in 2000 ms, sending SIGKILL. 
22 06 2020 12:41:49.489:WARN [launcher]: Firefox was not killed by SIGKILL in 2000 ms, continuing. 
 
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
```


Dans mon cas, il manquait simplement l'installation de firefox lors de la création de l'image docker...

```bash
apt-get install -y firefox
```


Après ajout, c'est bon (ouf de soulagement) 
Il faut dire que l'erreur n'était pas très explicite. Beaucoups de fils de discussion parlent de problèmes de proxy...



