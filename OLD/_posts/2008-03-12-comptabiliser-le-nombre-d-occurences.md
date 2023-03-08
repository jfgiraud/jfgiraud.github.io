---
title: "Comptabiliser le nombre d'occurences"
date: "2008-03-12 11:52:00"
---
Utiliser la commande <span style="font-style: italic;">uniq </span>pour afficher ou omettre des lignes récupérées de l'entrée standard. L'option -c permet de comptabiliser les lignes (qui doivent être ordonnées)

Associer avec sort.

for A in 1 3 4 2 3 1 1 1 3; do echo $A; done | sort | uniq -c
