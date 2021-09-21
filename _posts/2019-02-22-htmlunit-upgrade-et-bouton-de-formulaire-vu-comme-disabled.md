---
layout: post
title: "htmlunit, upgrade et bouton de formulaire vu comme disabled"
date: "2019-02-22 11:53:00"
---
Sur le projet, l'upgrade de la version de htmlunit de 2.21 à 2.33 a provoqué une régression.<br /><br />Le bouton de validation des formulaires est vu comme <tt>disabled</tt>.<br /><br />Sur la version 2.21, le code pour saisir le texte dans les <tt>HtmlTextInput</tt> utilise la méthode <tt>setValueAttribute</tt>.<br /><br />Entre la version 2.24 et 2.25, <tt>setValueAttribute</tt> n'émet plus l'événement qui permet au formulaire de se valider et activer/désactiver le bouton de soumission.<br /><br />A partir de la version 2.25, il faut utiliser la méthode <tt>type</tt> pour "saisir" le texte dans la zone texte.<br /><br />
