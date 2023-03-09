---
title: "python, conversion d'un fichier d'iso8859 en utf8"
date: 2012-05-04T14:44:00+01:00
---
<code><pre>
#!/bin/python

import sys

if len(sys.argv) != 3:
    print 'usage: python iso8859toutf8.py [infile] [outfile]'
    sys.exit(0)

with open(sys.argv[2], 'w') as fout:
    with open(sys.argv[1], 'r') as fin:
        data = fin.read().decode('iso8859')
        while data:
            fout.write(data.encode('utf8'))
            data = fin.read().decode('iso8859')
</pre></code>
