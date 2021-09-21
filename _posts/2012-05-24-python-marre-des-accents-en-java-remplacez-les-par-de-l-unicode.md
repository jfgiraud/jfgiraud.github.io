---
layout: post
title: "python, marre des accents en java : remplacez les par de l'unicode !"
date: "2012-05-24 11:13:00"
---
<code><pre><br /><br />$ cat tounicode.py<br />#!/usr/bin/python<br /><br />import re<br />import sys<br /><br />s = sys.argv[1].decode('utf8')<br /><br />print re.sub('\\\\x', '\\u00', re.sub('\'$', '', re.sub('^u\'', '', repr(s))))<br /><br />$ python tounicode.py "salut beaut&eacute;"<br />salut beaut\u00e9<br /></pre></code>
