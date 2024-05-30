---
title: "Comparaisons numériques avec sort"
date: 2008-03-17T10:35:00+01:00
tags: ["linux", "commande", "sort"]
description: "Comment trier numériquement avec sort"
---

```shell
$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -g
```
```console
1
5.0
2e1
21
```
```shell
$ printf "1 21 5.0 2e1" | tr " " "\n" | sort -n
```
```console
1
2e1
5.0
21
```
```shell
$ printf "1 21 5.0 2e1" | tr " " "\n" | sort
```
```console
1
21
2e1
5.0
```