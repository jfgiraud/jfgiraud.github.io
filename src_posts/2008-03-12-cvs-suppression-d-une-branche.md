---
layout: post
title: "CVS: suppression d'une branche"
date: "2008-03-12 11:07:00"
---
Ce matin, j'ai crée une branche à la place d'un tag. La correction n'est pas évidente pour nettoyer :<br /><br /><pre># renommage du tag en branche<br />cvs rtag -b -r &lt;version&gt;_TAG &lt;version&gt;_BRANCH &lt;application&gt;<br /># suppression de la branche<br />cvs rtag -d -B &lt;version&gt;_TAG &lt;application&gt;<br /></pre><br /><br />Lien externe : <a href="http://www.delorie.com/gnu/docs/cvs/cvs_51.html">http://www.delorie.com/gnu/docs/cvs/cvs_51.html</a>
