---
title: "bash, timeout"
date: 2012-07-31T12:30:00+01:00
---
L'astuce du jour !

Si un script appelle une commande qui peut ou non rendre la main (chemin réseau) et que l'on souhaite toujours la récupérer, on peut faire appel à la commande timeout.  <code><pre>
$ timeout 3 ssh user@host.example.com:~/ ls
</pre></code> Cela est très pratique lorsque la commande utilisée n'a pas prévu de rendre la main suite à un timeout spécifié en paramètre.
