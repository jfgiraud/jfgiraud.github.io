---
layout: post
title: "bash, appel callback à la sortie..."
date: "2020-11-20 17:20:00"
---
Il est possible en bash d'appeler des méthodes lorsque de la fin du script est atteinte et ce même s'il y a une erreur. Ci-dessous, le script appellera cleanup_err puis cleanup_ok lorsque false sera atteint.  <br/><br/> <script src="https://pastebin.com/embed_js/ZmmmJC8S"></script><br/><br/> C'est bien pratique pour nettoyer les fichiers et répertoires temporaires :)  <div style="overflow:hidden; height:0;">trap</div>