---
title: "python, distance de levenshtein"
date: "2020-11-13 12:24:00"
tags: distance levenshtein
---

La distance de Levenshtein est une distance, au sens mathématique du terme, donnant une mesure de la différence 
entre deux chaînes de caractères. Elle est égale au nombre minimal de caractères qu'il faut supprimer, insérer ou 
remplacer pour passer d'une chaîne à l'autre.

```python
def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]
```

Exemple:

```python
>>> levenshtein('toto', 'toto')
0
>>> levenshtein('toto', 'totos')
1
>>> levenshtein('toto', 'tata')
2
>>> levenshtein('toto', 'toto')
0
>>> 
>>> levenshtein('toto', 'too')
1
```

Source: [https://fr.wikipedia.org/wiki/Distance_de_Levenshtein](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein)
