---
layout: post
title: "url et mot de passe"
date: "2012-07-03 18:24:00"
---
Pour réduire mes logs, je viens d'utiliser la syntaxe suivante :  <code><pre><br />http://user:password@host:port...<br /></pre></code> Ici, le mot de passe doit être encodé lorsque des caractères non alphanumériques sont utilisés (comprenez 0-9a-zA-Z).  Chaque caractère non alphanumérique doit être encodé avec le format "%xx" où xx sera remplacé par le code hexadécimal du caractère.  <code><pre><br />Exemple: <br /><br />def conv(pw):<br />    r = ''<br />    for c in pw:<br /> if not c.isalpha():<br />     r += '%' + '%X' % ord(c)<br /> else:<br />     r += c<br />    return r <br /><br />>>> conv(u'tuéàtu')<br />u'tu\xe9\xe0tu'<br /><br /></pre></code>
