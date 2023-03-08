---
title: "Linux Mint Cinamon, touchpad et défilement à 2 doigts"
date: "2012-09-20 23:09:00"
---
Le défilement à 2 doigts sur le touchpad ne fonctionnait pas.

J'ai cherché dans les menus et je n'ai rien vu.

Sur internet, des pages parlent de synclient.

Effectivement, la ligne suivante
<code><pre>$ synclient VertTwoFingerScroll=1</pre></code>
permet de faire fonctionner le défilement à 2 doigts. Mais malheureusement, la modification n'est pas persistente après un redémarrage...

Pour la rendre persistente j'ai vu plein de docs ainsi que la page 

[http://mixeduperic.com/ubuntu/ubuntu-1004-how-to-setup-two-finger-scroll-on-laptop-touch-pad.html](http://mixeduperic.com/ubuntu/ubuntu-1004-how-to-setup-two-finger-scroll-on-laptop-touch-pad.html)

Cette page peut donner des idées si des choses sont à effectuer lors de l'ouverture de la session X.

Je n'en ai pas eu besoin car j'ai trouvé bizarre de faire tout cela.

Alors en recherchant encore dans les menus, j'ai vu :

<div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-b4G7Jskkbbk/UFuGr3YN-TI/AAAAAAAADn8/p5PI66Mn8cM/s1600/S%25C3%25A9lection_002.png" imageanchor="1" style="margin-left:1em; margin-right:1em"><img border="0" height="261" width="400" src="http://2.bp.blogspot.com/-b4G7Jskkbbk/UFuGr3YN-TI/AAAAAAAADn8/p5PI66Mn8cM/s400/S%25C3%25A9lection_002.png" /></a></div>
Sauvé, tout marche de manière simple :)
