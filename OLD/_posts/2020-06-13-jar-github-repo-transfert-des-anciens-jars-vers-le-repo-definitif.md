---
title: "jar, github, repo : transfert des anciens jars vers le repo définitif"
date: 2020-06-13T11:27:00+01:00
tags: ["git", "repo", "jar"]
---
Manipulations pour les envoyer vers maven.pkg.github.com en ligne de commande

```
~/.m2/settings.xml
<server>
      <id>jfgiraud-repo</id>
      <username>jfgiraud</username>
      <password>{{{votre token : https://github.com/settings/tokens}}}</password>
</server>

Envoi des fichiers récupérés de l'ancien repo vers le nouveau

for v in 1.5.3 2.0.0 2.0.1 2.0.2 2.0.3 2.0.4 2.0.5 2.0.6 2.0.7; do  
  mvn deploy:deploy-file -DgroupId=com.github.jfgiraud -DartifactId=temmental -Dpackaging=jar -Durl=https://maven.pkg.github.com/jfgiraud/temmental -Dversion=$v -Dfile=temmental-$v.jar -DrepositoryId=jfgiraud-repo
done
```

![2020-06-13-jar-github-repo-transfert-des-anciens-jars-vers-le-repo-definitif.png](assets/images/2020-06-13-jar-github-repo-transfert-des-anciens-jars-vers-le-repo-definitif.png) 

**EDIT**: le système nécessite visiblement le paramétrage d'un token dans le settings.xml même pour télécharger le war. Ce cas d'usage me déçoit :(
