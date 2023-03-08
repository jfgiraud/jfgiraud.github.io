---
layout: post
title: "bash et les tableaux..."
date: "2012-11-05 22:35:00"
---
Voici comment faire des tableaux et les utiliser en bash.


```
$ cat script.bash 
#!/bin/bash
tableau=("un élément" "et puis un deuxième" "et pourquoi pas un dernier" "pour finir")
for elem in "${tableau[@]}"; do
    echo $elem
done
echo et si je ne veux que le 3e...
echo "${tableau[@]:2:1}"
$ ./script.bash
un élément
et puis un deuxième
et pourquoi pas un dernier
pour finir
et si je ne veux que le 2e...
et pourquoi pas un dernier
```

Je suis tombé dessus en regardant les PKGBUILD de dwm comme ([celui-ci](https://github.com/w0ng/jokerboy-dwm/blob/master/PKGBUILD))
