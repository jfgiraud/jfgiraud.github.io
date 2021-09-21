---
layout: post
title: "python, conversion d'un fichier d'iso8859 en utf8"
date: "2012-05-04 14:44:00"
---
<code><pre><br />#!/bin/python<br /><br />import sys<br /><br />if len(sys.argv) != 3:<br />    print 'usage: python iso8859toutf8.py [infile] [outfile]'<br />    sys.exit(0)<br /><br />with open(sys.argv[2], 'w') as fout:<br />    with open(sys.argv[1], 'r') as fin:<br />        data = fin.read().decode('iso8859')<br />        while data:<br />            fout.write(data.encode('utf8'))<br />            data = fin.read().decode('iso8859')<br /></pre></code>