---
layout: post
title: "Bash, pattern substitution"
date: "2012-08-08 16:21:00"
---
Le manuel bash présente les syntaxes suivantes ([voir](http://tldp.org/LDP/abs/html/string-manipulation.html))  

- ${parameter#word} et ${parameter##word} pour supprimer le plus court et le plus long préfix
- ${parameter%word} et ${parameter%%word} pour supprimer le plus court et le plus long suffixe
- ${parameter/pattern/string} pour substituer une chaîne à un pattern. 

Il faut savoir que word peut être une regexp dans les 2 premiers cas.  Mais il faut surtout savoir que la syntaxe du pattern diffère de celles que l'on connaît généralement...  Sur [wiki.bash-hackers.org](http://wiki.bash-hackers.org/syntax/pattern) :  <code><pre>?(&lt;PATTERN-LIST&gt;) Matches zero or one occurrence of the given patterns
*(&lt;PATTERN-LIST&gt;) Matches zero or more occurrences of the given patterns
+(&lt;PATTERN-LIST&gt;) Matches one or more occurrences of the given patterns
@(&lt;PATTERN-LIST&gt;) Matches one of the given patterns
!(&lt;PATTERN-LIST&gt;) Matches anything except one of the given patterns
</pre></code>  D'où des choses zarbies du genre :  <code><pre>$ shopt -s extglob
$ v="LE temps PASSE vite"
$ echo ${v//+([[:upper:]])} 
temps vite
$ echo ${v%%+([[:lower:]])} 
LE temps PASSE
</pre></code> <script src="http://pastebin.com/embed_js.php?i=KJjpzEHF"></script><div style="height: 0; overflow: hidden;">pattern</div>
