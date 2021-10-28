---
layout: post
title: "Bash, templating..."
date: "2012-08-08 14:37:00"
---
Pour faire un système de templating en bash (par exemple pour du mailing) on peut faire ainsi si l'on souhaite que le modèle soit dans un fichier à part :  <code><pre><br />$ cat template.txt <br />&lt;b&gt;Hello '"${firstname}"'&lt;/b&gt;<br />Bye '"${firstname}"'<br /><br />$ for firstname in luc jeff gwen<br />&gt; do <br />&gt;   while read line <br />&gt;   do <br />&gt;      eval echo "'$line'"<br />&gt;   done &lt;template.txt<br />&gt; done<br />&lt;b&gt;Hello luc&lt;/b&gt;<br />Bye luc<br />&lt;b&gt;Hello jeff&lt;/b&gt;<br />Bye jeff<br />&lt;b&gt;Hello gwen&lt;/b&gt;<br />Bye gwen<br /></pre></code> Avec les Here Documents, cela aurait été plus simple...
