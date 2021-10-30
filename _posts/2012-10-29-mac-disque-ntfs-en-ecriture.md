---
layout: post
title: "mac, disque ntfs en écriture"
date: "2012-10-29 22:42:00"
---
Grrr, apple bloque tout. Le disque Western Digital que je viens d'acheter se monte directement mais n'est visible du finder qu'en lecture seulement !

C'est rageant.

Il y a des solutions tierces telles que paragon-software.com et tuxera.com mais c'est payant :(

J'ai quand même fait quelques explorations et il s'avère qu'on peut bien monter le disque en lecture/écriture sans passer par la caisse :

<script src="http://pastebin.com/embed_js.php?i=bp9HPBpY"></script>

J'ai lancé une copie de 200Go de données, je verai bien si tout passe.

Note: ça passe sur mon mac mini avec Mac OS 10.6.8 :) 

<div style="height: 0; overflow: hidden;">sudo, mount, ntfs, rw</div>
