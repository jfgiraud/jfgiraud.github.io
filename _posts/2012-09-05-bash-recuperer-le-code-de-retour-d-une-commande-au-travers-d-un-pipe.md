---
layout: post
title: "bash, récupérer le code de retour d'une commande au travers d'un pipe"
date: "2012-09-05 17:20:00"
---
L'exemple se passe de commentaires !  <code><pre>$ ls toto | head -n 1<br />ls: impossible d'accéder à toto: Aucun fichier ou dossier de ce type<br />$ echo $?<br />0<br />$ set -o pipefail 1<br />$ ls toto | head -n 1<br />ls: impossible d'accéder à toto: Aucun fichier ou dossier de ce type<br />$ echo $?<br />2<br /></pre></code>  Pratique dans le cas d'un "curl $url | sed ... > $output" pour savoir si une erreur est remontée.  