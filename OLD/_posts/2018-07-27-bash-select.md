---
title: "bash, select"
date: "2018-07-27 11:47:00"
tags: bash commande select
---
Je viens de m'apercevoir que je n'ai jamais parlé de la commande select sous bash. Celle-ci est très pratique car elle permet de faire un choix en précisant un numéro et non sa valeur.

Exemple d'utilisation ci-dessous :


```bash
$ select n in item1 item2 item3 item4 item5; do if [[ -n "$n" ]]; then echo "You choose: $n"; break; else echo "Invalid choice"; fi; done
1) item1
2) item2
3) item3
4) item4
5) item5
#? 6
Invalid choice
#? z
Invalid choice
#? 2
You choose: item2
```
