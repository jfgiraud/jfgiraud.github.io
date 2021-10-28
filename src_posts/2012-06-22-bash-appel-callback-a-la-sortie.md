---
layout: post
title: "bash, appel callback à la sortie..."
date: "2012-06-22 09:42:00"
---
Il est possible en bash d'appeler des méthodes lorsque de la fin du script est atteinte et ce même s'il y a une erreur.  Ci-dessous, le script appellera cleanup_err puis cleanup_ok lorsque false sera atteint.  <code><pre><br />#!/bin/bash<br />set -e<br /><br />function cleanup_err {<br />  echo cleanup_err<br />}<br /><br />function cleanup_ok {<br />  echo cleanup_ok<br />}<br />  <br />trap cleanup_ok EXIT<br />trap cleanup_err ERR<br />  <br />false<br /></pre></code> C'est bien pratique pour nettoyer les fichiers et répertoires temporaires :)
