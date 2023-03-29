---
title: "java, exclure une dépendance dans le pom"
date: 2021-12-21T07:10:00+01:00
tags: [ "java", "pom", "dependency" ]
description: "Supprimer une lib modifiée maison et la remplacer par l'officielle"
---

Dans le `pom.xml` :

```
<dependency>
    <groupId>genesys</groupId>
    <artifactId>api-genesys</artifactId>
    <version>1.1</version>
    <exclusions>
        <exclusion>
            <groupId>cvf</groupId>
            <artifactId>log4j</artifactId>
        </exclusion>
    </exclusions>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-1.2-api</artifactId>
    <version>2.17.0</version>
</dependency>
```
