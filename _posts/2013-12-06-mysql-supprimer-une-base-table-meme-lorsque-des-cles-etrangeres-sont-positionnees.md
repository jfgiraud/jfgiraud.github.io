---
layout: post
title: "mysql, supprimer une base/table même lorsque des clés étrangères sont positionnées"
date: "2013-12-06 14:23:00"
---
Pour ignorer la vérification de la présence de clés étrangères lors de la suppression d'une table ou base, on peut utiliser "SET foreign_key_checks = 0" avec mysql comme dans l'exemple ci-dessous :

<script src="https://pastebin.com/embed_js/hyjiLiVT"></script>
