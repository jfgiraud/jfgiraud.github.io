---
title: "Linux Mint Cinnamon & Samsung ML-1865"
date: "2012-08-27 23:13:00"
---
Impossible de faire fonctionner mon imprimante (une Samsung ML-1865) sur mon Sony SVS-1311 où j'ai installé un Linux Mint 13 Cinnamon.

L'imprimante était détectée&nbsp; sur le réseau mais le modèle indiqué dans le panneau Imprimantes était Samsung ML-1750 

Les impressions partaient mais les feuilles sortaient... <code><pre>INTERNAL ERROR - Please use the proper driver
POSITION : 0x0 (0)
SYSTEM : h6fw_5.49/xl_op
LINE : 180
VERSION : SPL 5.49 10-20-2010 
</pre></code> Je suis allé sur le site de samsung pour télécharger le driver et l'ai installé... Même problème bien que le modèle indiqué dans le panneau soit mieux : Samsung ML-1860

Au final, après recherche sur google, je suis tombé sur la page suivante : [http://forums.linuxmint.com/viewtopic.php?f=51&amp;t=107026](http://forums.linuxmint.com/viewtopic.php?f=51&amp;t=107026)

J'ai ajouté  <tt>deb <a class="postlink" href="http://www.bchemnet.com/suldr/">http://www.bchemnet.com/suldr/</a> debian extra</tt> dans la liste des dépôts (menu configuration du gestionnaire de paquets Synaptic) et hop !

Un coup de :

<code><pre>$ su
$ wget -O - http://www.bchemnet.com/suldr/suldr.gpg | apt-key add -- - 
$ apt-get install samsungmfp-data samsungmfp-configurator-qt4 
  samsungmfp-configurator-data samsungmfp-driver 
  printer-driver-splix
</pre></code> 

On réinstalle l'imprimante et fini les  <code><pre>INTERNAL ERROR - Please use the proper driver
POSITION : 0x0 (0)
SYSTEM : h6fw_5.49/xl_op
LINE : 180
VERSION : SPL 5.49 10-20-2010 
</pre></code>  Ouf!


EDIT : 7 Septembre 2016 les paquets samsungmfp-* ont été remplacés par suld-*
