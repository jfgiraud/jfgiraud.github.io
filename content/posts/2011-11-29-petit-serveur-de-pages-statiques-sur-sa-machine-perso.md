---
title: "Petit serveur de pages statiques sur sa machine perso..."
date: 2011-11-29T11:04:00+01:00
tags: [ "apache", "server", "static" ]
description: "Installer un serveur apache2 et lui dire de délivrer les répertoires ~/public_html des utilisateurs du système"
---

Installation d'apache :

  $ apt-get install apache2
  $ cd /etc/apache2/mods-enabled/
  $ sudo ln -s ../mods-available/userdir.conf .
  $ sudo ln -s ../mods-available/userdir.load .
  $ sudo /etc/init.d/apache2 reload

Pages statiques :

  $ mkdir ~/public_html
  $ echo '<html><body>hello</body></html>' > ~/public_html/hello.html

Ouvrir le browser 

    [http://127.0.0.1/~me/hello.html](http://127.0.0.1/~me/hello.html)

:)
