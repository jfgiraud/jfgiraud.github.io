---
title: "docker, formater la sortie ls"
date: 2023-01-12T07:10:00+01:00
tags: [ "docker", "ls", "format" ]
description: "Voici comment formater la sortie de docker ls"
---

```
docker container ls -a --format 'table {{.ID}}\t{{.Image}}\t{{.Command}}\t{{.Status}}'

docker container ls -a --format 'table {{.ID}}\t{{.Image}}\t{{.Command}}\t{{.Status}}\t{{.Names}}' 
```

La commande suivante peut aider à déterminer les noms à mettre dans les `{{}}`

```
docker container ls -a --format '{{json .}}'
```

Source: [https://docs.docker.com/engine/reference/commandline/ps/](https://docs.docker.com/engine/reference/commandline/ps/)