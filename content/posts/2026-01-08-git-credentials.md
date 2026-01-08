---
title: "Git demande le login/mdp (token)"
date: 2026-01-08T17:52:00+01:00
tags: ["git", "token"]
description: "Solution pour avoir le personal token access stoqué sur sa homedir"
---


```shell
# git pull
Username for 'https://githostname.example.com': gitlogin
Password for 'https://gitlogin@githostname.example.com':
```

Dans le `~/.gitconfig`
```
[credential "https://githostname.example.com"]
        username = gitlogin
        helper = "!f() { test \"$1\" = get && echo \"password=$(cat $HOME/.secret)\"; }; f"
```

Dans le `~/.secret` (en rw-------),
```
Copier le token en clair
```
