---
title: "changer d'ordinateur, calculer son amortissement..."
date: 2012-08-06T14:38:00+01:00
---
Dernièrement, je voulais acheter un ordinateur portable mais je n'arrivais pas à passer le cap...

J'ai eu un macbook blanc que j'ai donné à ma mère... 

Le matériel était excellent... 

Depuis, il y a eu le passage aux macbook pro au prix de 1250€ (250€ de plus que le macbook que j'avais acheté à l'époque).

Et là, je me dis que c'est trop cher...

Normalement, plus le temps passe plus le prix du matériel technologique baisse (TV, ordis...).

Chez Apple, c'est l'inverse :(

J'ai hésité, hésité... Envie d'un mac mais le cerveau qui dit non...

Et puis... un petit tour sur la page wiki de l'amortissement et la lecture de la méthode softy.

Dans mon cas, si je garde l'ordi (sans pépin 4 ans) :
 <code><pre>
$ python
>>> prix=1250
>>> nb_annees=4
>>> [prix*x/365 for x in [a * 2.0 / (nb_annees * (nb_annees + 1)) for a in range(nb_annees, 0, -1)]]
[1.36986301369863, 1.0273972602739727, 0.684931506849315, 0.3424657534246575]
>>> prix=850
>>> [prix*x/365 for x in [a * 2.0 / (nb_annees * (nb_annees + 1)) for a in range(nb_annees, 0, -1)]]
[0.9315068493150684, 0.6986301369863014, 0.4657534246575342, 0.2328767123287671]
</pre></code> Soit .44€ de moins par jour pour un PC la première année... Ce qui équivaut tout de même à 160€ la première année. C'est énorme.

Finalement, je repasse aux PC...

... et j'attends avec impatience mon Sony VAIO

bye apple...

