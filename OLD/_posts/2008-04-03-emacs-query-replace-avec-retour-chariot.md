---
title: "emacs : query replace avec retour chariot !"
date: 2008-04-03T11:05:00+01:00
---
Ayant un document xml avec plein de données, je souhaite séparer les blocs "&lt;Event&gt;<event>" pour mieux distinguer. Voici comment faire...

</event>
<pre>M-%
&lt;Event&gt;
<event>C-q C-j C-q C-j </event>&lt;Event&gt;


</pre>
