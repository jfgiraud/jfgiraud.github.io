---
title: "bash, fautes sur commande cd..."
date: "2012-07-02 12:06:00"
tags: bash, cdspell
---

Si l'option cdspell est positionnée, les fautes de frappe dans la commande cd seront corrigées. Les erreurs prises en compte seront les caractères transposés, les caractères manquants et les caractères trop nombreux. Si un correctif est trouvé, le chemin utilisé pour le cd sera affiché et la commande exécutée. L'option n'est utilisée que dans le cas des shells intéractifs.  

```bash
$ shopt -s cdspell
$ cd /ec
/etc
$ shopt -u cdspell
```
