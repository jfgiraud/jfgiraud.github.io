---
layout: post
title: "Petit serveur de pages statiques sur sa machine perso..."
date: "2011-11-29 11:04:00"
---
Installation d'apache :<br /><br /><pre><code><small><br />  $ apt-get install apache2<br />  $ cd /etc/apache2/mods-enabled/<br />  $ sudo ln -s ../mods-available/userdir.conf .<br />  $ sudo ln -s ../mods-available/userdir.load .<br />  $ sudo /etc/init.d/apache2 reload<br /></small></code></pre>  <br /><br />Pages statiques :<br /><br /><pre><code><small><br />  $ mkdir ~/public_html<br />  $ echo '<html><body>hello</body></html>' > ~/public_html/hello.html<br /></small></code></pre>  <br /><br />Ouvrir le browser <br /><br /><a href="http://127.0.0.1/~me/hello.html">http://127.0.0.1/~me/hello.html</a><br /><br />:)