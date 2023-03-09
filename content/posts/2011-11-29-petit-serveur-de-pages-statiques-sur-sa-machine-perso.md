---
title: "Petit serveur de pages statiques sur sa machine perso..."
date: 2011-11-29T11:04:00+01:00
---
Installation d'apache :

<pre><code><small>
  $ apt-get install apache2
  $ cd /etc/apache2/mods-enabled/
  $ sudo ln -s ../mods-available/userdir.conf .
  $ sudo ln -s ../mods-available/userdir.load .
  $ sudo /etc/init.d/apache2 reload
</small></code></pre>  

Pages statiques :

<pre><code><small>
  $ mkdir ~/public_html
  $ echo '<html><body>hello</body></html>' > ~/public_html/hello.html
</small></code></pre>  

Ouvrir le browser 

[http://127.0.0.1/~me/hello.html](http://127.0.0.1/~me/hello.html)

:)
