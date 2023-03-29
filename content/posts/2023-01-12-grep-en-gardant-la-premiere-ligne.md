---
title: "sed, filtrer comme grep en gardant la première ligne"
date: 2023-01-12T07:10:00+01:00
tags: [ "sed", "grep" ]
description: "Astuce pour filter tout en gardant la première ligne du flux"
---

Astuce pour filter tout en gardant la première ligne du flux. 

Cela peut être utile par exemple pour conserver les titres d'un tableau.

```
$ docker container ls -a | sed '1p;/xxx:/!d'
CONTAINER ID   IMAGE                                                              COMMAND                  CREATED          STATUS                       PORTS     NAMES
faca9b07e90c   multirepo.example:5002/xxx/xxx:latest          "bash"                   10 minutes ago   Up 10 minutes                          monsvi-latest
```

Source: [https://youtrack.jetbrains.com/issue/IDEA-214308#focus=Comments-27-4177127.0-0](https://youtrack.jetbrains.com/issue/IDEA-214308#focus=Comments-27-4177127.0-0)