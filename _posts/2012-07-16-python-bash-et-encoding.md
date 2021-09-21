---
layout: post
title: "python, bash et encoding..."
date: "2012-07-16 12:31:00"
---
En python, lorsque la sortie n'est pas de type tty, l'encoding est "ascii" ce qui provoque des erreurs sur les caractères accentués. La solution est d'exporter la variable PYTHONIOENCODING qui définit l'encoding à utiliser.  <code><pre><br />$ python a.py <br />é<br />$ python a.py | cat<br />Traceback (most recent call last):<br />  File "a.py", line 3, in <module><br />    print u"\xe9";<br />UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 0: <br />ordinal not in range(128)<br />$ export PYTHONIOENCODING=utf-8 <br />$ python a.py | cat<br />é<br />$<br /></pre></code> Une autre solution est de changer l'encoding de stdout...  <code><pre><br />#!/usr/bin/python<br /># -*- coding: utf-8 -*-<br /><br />import sys<br />import codecs<br />import locale<br /><br />sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)<br /><br />print u"é"<br /></pre></code>