---
layout: post
title: "bash, appel callback à la sortie..."
date: "2012-06-22 09:42:00"
---
Il est possible en bash d'appeler des méthodes lorsque de la fin du script est atteinte et ce même s'il y a une erreur.  Ci-dessous, le script appellera cleanup_err puis cleanup_ok lorsque false sera atteint.  <code><pre>
#!/bin/bash
set -e

function cleanup_err {
  echo cleanup_err
}

function cleanup_ok {
  echo cleanup_ok
}
  
trap cleanup_ok EXIT
trap cleanup_err ERR
  
false
</pre></code> C'est bien pratique pour nettoyer les fichiers et répertoires temporaires :)
