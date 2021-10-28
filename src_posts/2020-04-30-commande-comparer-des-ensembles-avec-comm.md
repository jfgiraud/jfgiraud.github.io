---
layout: post
title: "commande, comparer des ensembles avec comm"
date: "2020-04-30 15:54:00"
---
Parfois, on a besoin de comparer des ensembles. La commande <kbd>comm</kbd> permet de faire ressortir :<br /><br /><ul><li>les valeurs qui n'appartiennent qu'au fichier f1 (colonne 1)<br /></li><li>les valeurs qui n'appartiennent qu'au fichier f2 (colonne 2)<br /></li><li>les valeurs qui appartiennent aux fichiers f1 et f2 (colonne 3)<br /></li></ul><div class="separator" style="clear: both; text-align: center;"><a href="https://3.bp.blogspot.com/-vg7Zva_Vs00/XqrXy6g4dAI/AAAAAAAAEQ4/D3E_dujxKNYiC4_z-CtMraGKzxn9bjKGwCNcBGAsYHQ/s1600/comm.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="172" data-original-width="341" height="202" src="https://3.bp.blogspot.com/-vg7Zva_Vs00/XqrXy6g4dAI/AAAAAAAAEQ4/D3E_dujxKNYiC4_z-CtMraGKzxn9bjKGwCNcBGAsYHQ/s400/comm.png" width="400" /></a></div>En jouant sur les options, on peut faire disparaître les valeurs d'une ou plusieurs colonnes   <br /><ul><li>-1 pour faire disparaître la colonne 1<br /></li><li>-2 pour faire disparaître la colonne 2<br /></li><li>-3 pour faire disparaître la colonne 3<br /></li></ul>Attention, les fichiers doivent être au préalable triés. <br /><br /><br />Exemple :  ```
$ cat f1 | sort | sponge f1
$ cat f2 | sort | sponge f2
$ cat f1
a
b
c
d
e
f
g
h
i
$ cat f2
d
e
f
k
l
m
n
o
p
$ comm f1 f2
a
b
c
		d
		e
		f
g
h
i
	k
	l
	m
	n
	o
	p
$ comm -1 f1 f2
	d
	e
	f
k
l
m
n
o
p
$ comm -13 f1 f2
k
l
m
n
o
p
```
  
