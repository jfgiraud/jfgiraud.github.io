---
title: "bash, afficher en gras"
date: 2012-11-30T11:35:00+01:00
---
On peut utiliser la commande tput de la manière suivante :


```
echo "$(tput bold)Mise à jour du modèle '$modele' sur 'itg$environnement' de '$fromversion' vers '$toversion'$(tput sgr0)"
```

<div style="height: 0; overflow: hidden;">gras, bold, tput, echo
</div>
