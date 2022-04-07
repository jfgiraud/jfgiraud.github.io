---
layout: post
title: "java, tests unitaires en ligne de commande"
date: "2018-12-17 12:13:00"
---
Rappel:

```
$ mvn test
$ mvn -Dtest=TestClass test
$ mvn -Dtest=TestClass1,TestClass2 test
$ mvn -Dtest=TestClass#methodName test
$ mvn -Dtest=TestClass#methodPattern* test
$ mvn -Dtest=TestClass#methodPattern1*+methodPattern2* test
```
