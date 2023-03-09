---
title: "Simuler un lien WAN sous Linux"
date: 2020-10-07T23:02:00+01:00
tags: ["simuler", "wan"]
---
Voici un script qui m'a bien été utile il y a 3-4 ans.

Le déploiement d'un livrable échouait lorsque je le lançais depuis chez moi via le VPN de la société.

En simulant une connexion comme chez moi mais depuis mon bureau, j'ai pu détecter qu'il y avait un timeout
qui se produisait.

J'ai alors pu corriger un plugin maven afin d'augmenter ce timeout pour faire en sorte que sur une connexion lente, le déploiement se passe bien.<br /><br />  

Source: [https://github.com/nicolargo/simulwan](https://github.com/nicolargo/simulwan)
