---
title: "Placements"
date: 2012-02-17T14:50:00+01:00
tags: ["finances"]
---

Tu as de l'argent et tu comptes le placer à un meilleur taux... Combien de temps faudra-t-il bloquer cet argent à ce meilleur taux pour qu'il rapporte à nouveau (c'est à dire que la quinzaine perdue soit amortie...)

```
>>> Tde=2.25
>>> Tvers=2.8
>>> import math
>>> rattrappeEn=int(math.ceil(Tde/(Tvers-Tde)))
>>> rattrappeEn
5
>>> Tde*(rattrappeEn+2)>Tvers*rattrappeEn
True
>>> Tde*(rattrappeEn+1)>Tvers*rattrappeEn
False
```

La somme doit rester pendant 5 quinzaines pleines (sans compter la quinzaine de reception de la somme) pour qu'elle commence à rapporter à nouveau.
