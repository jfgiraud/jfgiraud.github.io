---
title: "Scanner Brother ADS1600W, problème linux lors de l'envoi en FTP"
date: 2021-08-30T09:06:00+01:00
tags: ["scanner", "ftp"]
---

L'envoi en FTP ne fonctionne pas avec le paquet `vsftpd` (bien que l'envoi d'une page de test depuis l'interface 
de gestion du scanner indique OK). 

```text
sudo apt install vsftpd
```

Lors du scan d'un document réel, le scanner indique "Sending error" sans plus d'information. 

En changeant le serveur FTP, cela passe. 

Prendre  

```text
sudo apt install pure-ftpd-common
```  
