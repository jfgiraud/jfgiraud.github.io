---
layout: post
title: "Placements"
date: "2012-02-17 14:50:00"
---
Tu as de l'argent et tu comptes le placer à un meilleur taux... Combien de temps faudra-t-il bloquer cet argent à ce meilleur taux pour qu'il rapporte à nouveau (c'est à dire que la quinzaine perdue soit amortie...)<br /><br /><pre><code><br />>>> Tde=2.25<br />>>> Tvers=2.8<br />>>> import math<br />>>> rattrappeEn=int(math.ceil(Tde/(Tvers-Tde)))<br />>>> rattrappeEn<br />5<br />>>> Tde*(rattrappeEn+2)>Tvers*rattrappeEn<br />True<br />>>> Tde*(rattrappeEn+1)>Tvers*rattrappeEn<br />False<br /></code></pre>La somme doit rester pendant 5 quinzaines pleines (sans compter la quinzaine de reception de la somme) pour qu'elle commence à rapporter à nouveau.
