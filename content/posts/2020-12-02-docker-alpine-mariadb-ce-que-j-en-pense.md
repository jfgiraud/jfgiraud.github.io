---
title: "docker / alpine / mariadb : ce que j'en pense...."
date: "2020-12-02 11:02:00"
tags: ["docker", "alpine", "mariadb"]
---
J'ai voulu passer à alpine à cause de la taille de l'image produite et parce qu'elle boote vite.

Je voulais améliorer les performances du pipeline de mon projet.

J'ai eu beaucoup de déboires pour :

* comprendre et réussir à faire tourner le service MariaDB dans docker (je voulais une image généraliste qui ne fasse pas que MariaDB mais aussi du java/maven & du python2.7)    
* contourner des problèmes pour réussir à configurer mariadb convenablement (actuellement les postes de dévs et le gitlab sont en mysql alors que nos serveurs d'intégration/préproduction/production sont passés en MariaDB). Les sysadmins m'ont aiguillé.     
* corriger des pbs d'appels depuis les tests java ou python
  

Hier, soir, j'arrive enfin à faire tourner les tests... et désenchantement ! 

Les tests sont extrèmement lents sous alpine ! Trop c'est trop... 

```text
(alpine)
Ran 110 tests in 379.308s
OK

 __    _____
\\ \\ / /__|
 \\ V /\\__\\
  \\_/ |___/

(ubuntu)
Ran 110 tests in 178.103s
OK
```

Apparemment c'est connu... Je vais en rester là, peut-être aller voir du côté de `debian:buster-slim`

 Références additionnelles 


- [https://andygrove.io/2020/05/why-musl-extremely-slow/](https://andygrove.io/2020/05/why-musl-extremely-slow/)
- [https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d](https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d)


