---
title: "maven, jar en repo local"
date: "2014-11-19 13:50:00"
---

```
mvn deploy:deploy-file -Durl=file:///home/jfgiraud/IdeaProjects/temmental-example/repo/ -Dfile=./target/temmental-2.0.0-SNAPSHOT.jar -DgroupId=temmental -DartifactId=temmental -Dpackaging=jar -Dversion=2.0-SNAPSHOT
```
