---
title: "ssh, exécuter un sudo par ssh sans saisir son mot de passe (pour sudo)..."
date: 2016-02-12T10:57:00+01:00
tags: ["ssh", "password"]
---
Dans le cadre de mon projet, on souhaitait pouvoir exécuter des redémarrages de services depuis son poste local sur des machines accessibles par ssh mais dont on n'avait pas accès au compte root.

Le service est cependant redémmarrable via sudo mais un mot de passe était demandé.

Nous avons mis en place un script qui lit dans un fichier de conf le mot de passe et exécute le sudo (et remplis le mot de passe du sudo) par ssh.

Cela donne un code comme ceci :


```bash
ssh user@host.example.com "sudo -S service sonar restart <<< '$passwd'"
```
