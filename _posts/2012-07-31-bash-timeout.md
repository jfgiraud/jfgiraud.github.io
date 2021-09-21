---
layout: post
title: "bash, timeout"
date: "2012-07-31 12:30:00"
---
L'astuce du jour !<br/><br/>Si un script appelle une commande qui peut ou non rendre la main (chemin réseau) et que l'on souhaite toujours la récupérer, on peut faire appel à la commande timeout.  <code><pre><br />$ timeout 3 ssh user@host.example.com:~/ ls<br /></pre></code> Cela est très pratique lorsque la commande utilisée n'a pas prévu de rendre la main suite à un timeout spécifié en paramètre.
