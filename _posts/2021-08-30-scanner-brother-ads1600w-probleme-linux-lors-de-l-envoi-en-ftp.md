---
layout: post
title: "Scanner Brother ADS1600W, problème linux lors de l'envoi en FTP"
date: "2021-08-30 09:06:00"
---
L'envoi en FTP ne fonctionne pas avec le paquet vsftpd (bien que l'envoi d'une page de test depuis l'interface de gestion du scanner indique OK). <br/><br/><blockquote>sudo apt install vsftpd</blockquote><br/><br/>Lors du scan d'un document réel, le scanner indique "Sending error" sans plus d'information. <br/><br/>En changeant le serveur FTP, cela passe. Prendre  <br/><br/><blockquote>sudo apt install pure-ftpd-common</blockquote><br/><br/>  