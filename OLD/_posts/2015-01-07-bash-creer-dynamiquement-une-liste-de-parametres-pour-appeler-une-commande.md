---
title: "bash, créer dynamiquement une liste de paramètres pour appeler une commande"
date: "2015-01-07 15:17:00"
tags: bash whiptail
---
Voici comment créer dynamiquement une liste de paramètres et l'utiliser dans des appels de commande.
Le cas des espaces dans les options est bien géré.

Dans le cas présent, cela sert à afficher une boite de dialogue (utilitaire whiptail livré d'office sous debian) pour que l'utilisateur puisse choisir les actions à effectuer


```
$ opts=("Redémarrer fitnesse" "" off)
$ [[ $available -eq 1 ]] && opts+=("Redémarrer tomcat" "" off)
$ retour=$(whiptail --title "Fitnesse" --checklist "Sélectionner les options" 15 60 8 "${opts[@]}" 3>&1 1>&2 2>&3)
$ echo $retour
"Redémarrer fitnesse" "Redémarrer tomcat"
```

<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/-yH5VoeAU5ao/VK1AKg6J0lI/AAAAAAAADzA/M2iI0dOv0m8/s1600/Capture%2Bdu%2B2015-01-07%2B15%3A17%3A54.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/-yH5VoeAU5ao/VK1AKg6J0lI/AAAAAAAADzA/M2iI0dOv0m8/s320/Capture%2Bdu%2B2015-01-07%2B15%3A17%3A54.png" /></a></div>  Pour des radioboutons, remplacer `--selectbox` par `--radiobox`
