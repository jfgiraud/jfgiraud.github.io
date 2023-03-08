---
layout: post
title: "htmlunit, upgrade et bouton de formulaire vu comme disabled"
date: "2019-02-22 11:53:00"
tags: htmlunit
---
Sur le projet, l'upgrade de la version de htmlunit de 2.21 à 2.33 a provoqué une régression.

Le bouton de validation des formulaires est vu comme `disabled`.

Sur la version 2.21, le code pour saisir le texte dans les `HtmlTextInput` utilise la méthode `setValueAttribute`.

Entre la version 2.24 et 2.25, `setValueAttribute` n'émet plus l'événement qui permet au formulaire de se valider et activer/désactiver le bouton de soumission.

A partir de la version 2.25, il faut utiliser la méthode `type` pour "saisir" le texte dans la zone texte.


