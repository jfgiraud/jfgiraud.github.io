---
layout: post
title: "intellij, page vide sans menu au démarrage"
date: "2020-05-15 14:26:00"
---
Suite à la mise à jour d'un plugin (python), mon intellij 2020.1 ne démarrait plus correctement. Les versions antérieures oui, mais j'ai eu des difficultés pour rétablir un démarrage correct.

Voici les commandes que j'ai effectuées pour nettoyer et permettre le redémarrage correct avec ouverture des projets.

Attention, vous pouvez perdre d'autres configurations mais pour moi c'était acceptable.

```
  457  | 14/05 16:38 |  rm -rf .config/JetBrains/ .java/ .local/share/JetBrains/ .cache/JetBrains/
```

![2020-05-15-intellij-page-vide-sans-menu-au-demarrage.png](assets/images/2020-05-15-intellij-page-vide-sans-menu-au-demarrage.png)
