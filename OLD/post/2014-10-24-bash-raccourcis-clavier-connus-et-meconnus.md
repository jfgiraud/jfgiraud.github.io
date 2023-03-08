---
layout: post
title: "Bash, raccourcis clavier connus et méconnus..."
date: "2014-10-24 11:57:00"
---
Un petit post pour rappeler les raccourcis clavier dans les terminaux.

Certains sont bien utiles comme le Esc + . que j'utilise constamment ;)


```
1. Déplacement

    Ctrl + a               Déplace votre curseur en début de ligne
    Ctrl + e               Déplace votre curseur en fin de ligne
    Ctrl + b               Déplace le curseur d'un caractère vers la gauche
    Ctrl + f               Déplace le curseur d'un caractère vers la droite
    Alt + b ou Esc + b     Déplace le curseur de mot en mot vers la gauche
    Alt + f ou Esc + f     Déplace le curseur de mot en mot vers la droite
    Ctrl + x Ctrl + x      Alterne le curseur avec son ancienne position (car x est en forme de croisement)


2. Couper / Coller

    Ctrl + u               Efface tous les caractères à gauche du curseur
    Ctrl + k               Efface tous les caractères à droite du curseur
    Ctrl + y               Colle la précédente saisie
    Ctrl + w               Efface le mot précédent
    Alt + BS ou Esc + BS   Coupe le texte jusqu'au début de mot précédent le curseur.

3. Modification

    Ctrl + t               Permet d'inverser la lettre courante avec la précédente
    Alt  + t               Inverse le mot courant et le mot précédent
    Ctrl + d               Efface le caractère courant ou sinon déconnecte (équivalent de logout) si la ligne est vide
    Alt + d ou Esc + d     Efface le mot suivant
    Alt + c ou Esc + c     Met la lettre sous le curseur en majuscule et les suivantes en minuscules (c pour capitalize)
    Alt + l ou Esc + l     Met un mot en en minuscule (l pour lowercase)
    Alt + u ou Esc + u     Met un mot en majuscule (u pour uppercase)
    Alt + .                Réécrit le dernier paramètre de la dernière commande
    Ctrl + x Ctrl + e      Edite la ligne courante dans votre éditeur de texte (editor car reprend la variable $EDITOR du shell)
    Esc<nombre><caractère> Répète le caractère autant de fois que le chiffre.

    Ctrl + _               Annule la dernière modification
    Alt + r ou Esc + r     Annule les changements et remet la ligne telle qu'elle était dans l'historique.

4. Autre

    Alt + . ou Esc + .     Réécrit le dernier paramètre de la dernière commande
    !!                     Réexécute la dernière commande
    !x                     Réexécute la dernière commande commencant par x
    !x:p                   Affiche la dernière commande commencant par x
    !$                     Récupere le dernier paramètre de la commande précédente

    Ctrl + r               Permet de rechercher dans l'historique des commandes précédemment saisies
    Ctrl + l               Efface le contenu de l'écran
    Ctrl + c               Arrêter la commande en court
    Ctrl + d               Quitter le shell en court
```
