---
layout: post
title: "Bash, pattern substitution"
date: "2012-08-08 16:21:00"
tags: bash regexp pattern
---

Le manuel bash présente les syntaxes suivantes ([voir](http://tldp.org/LDP/abs/html/string-manipulation.html))  

- `${parameter#word}` et `${parameter##word}` pour supprimer le plus court et le plus long préfix
- `${parameter%word}` et `${parameter%%word}` pour supprimer le plus court et le plus long suffixe
- `${parameter/pattern/string}` pour substituer une chaîne à un pattern. 

Il faut savoir que word peut être une regexp dans les 2 premiers cas.  Mais il faut surtout savoir que la syntaxe du pattern diffère de celles que l'on connaît généralement...  

Sur [wiki.bash-hackers.org](http://wiki.bash-hackers.org/syntax/pattern) :  

```
?(<PATTERN-LIST>) Matches zero or one occurrence of the given patterns
*(<PATTERN-LIST>) Matches zero or more occurrences of the given patterns
+(<PATTERN-LIST>) Matches one or more occurrences of the given patterns
@(<PATTERN-LIST>) Matches one of the given patterns
!(<PATTERN-LIST>) Matches anything except one of the given patterns
```  

D'où des choses zarbies du genre :  
```
$ shopt -s extglob
$ v="LE temps PASSE vite"
$ echo ${v//+([[:upper:]])} 
temps vite
$ echo ${v%%+([[:lower:]])} 
LE temps PASSE
```

```
$ for b in configb configb1 configb2 configb_test; 
do 
  echo $b $(DB_NAME=$b; echo '%%configcommon' | sed -e "s/%%configcommon/${DB_NAME/configb@(1|2|)/configcommon}/g" )
done
configb configcommon
configb1 configcommon
configb2 configcommon
configb_test configcommon_test
```


