---
layout: post
title: "jar, github, repo : transfert des anciens jars vers le repo définitif"
date: "2020-06-13 11:27:00"
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
  mvn deploy:deploy-file -DgroupId=com.github.jfgiraud -DartifactId=temmental -Dpackaging=jar -Durl=https://maven.pkg.github.com/jfgiraud/temmental -Dversion=$v -Dfile=temmental-$v.jar -DrepositoryId=jfgiraud-repo; done
```


<div class="separator" style="clear: both; text-align: center;"><a href="https://4.bp.blogspot.com/-5szNPMxC4B8/XuScB7yMzzI/AAAAAAAAEUE/0d1ys854-2ALbmP30vOKBEHoyfVXIKkHwCNcBGAsYHQ/s1600/settings.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-5szNPMxC4B8/XuScB7yMzzI/AAAAAAAAEUE/0d1ys854-2ALbmP30vOKBEHoyfVXIKkHwCNcBGAsYHQ/s320/settings.png" width="320" height="167" data-original-width="612" data-original-height="319" /></a></div> EDIT: le système nécessite visiblement le paramétrage d'un token dans le settings.xml même pour télécharger le war. Ce cas d'usage me déçoit :(
