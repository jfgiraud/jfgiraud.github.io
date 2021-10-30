---
layout: post
title: "Bash, templating..."
date: "2012-08-08 14:37:00"
---
Pour faire un système de templating en bash (par exemple pour du mailing) on peut faire ainsi si l'on souhaite que le modèle soit dans un fichier à part :  <code><pre>
$ cat template.txt 
&lt;b&gt;Hello '"${firstname}"'&lt;/b&gt;
Bye '"${firstname}"'

$ for firstname in luc jeff gwen
&gt; do 
&gt;   while read line 
&gt;   do 
&gt;      eval echo "'$line'"
&gt;   done &lt;template.txt
&gt; done
&lt;b&gt;Hello luc&lt;/b&gt;
Bye luc
&lt;b&gt;Hello jeff&lt;/b&gt;
Bye jeff
&lt;b&gt;Hello gwen&lt;/b&gt;
Bye gwen
</pre></code> Avec les Here Documents, cela aurait été plus simple...
