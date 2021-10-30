---
layout: post
title: "Linux Mint Cinnamon, positionner la luminosité en ligne de commande"
date: "2012-09-07 12:26:00"
---
Il est possible d'utiliser les fichiers 


- `/sys/class/backlight/acpi_video0/max_brightness`

- `/sys/class/backlight/acpi_video0/brightness` 

afin de modifier la luminosité.  Le script suivant prend un numérique (pourcentage entre 0 et 100) et modifie le fichier `/sys/class/backlight/acpi_video0/brightness` en conséquent.  


<script src="http://pastebin.com/embed_js.php?i=xbUAWiTh"></script>   Toutefois, pour exécuter ce fichier, il faudra être root (sudo ou SUID bit positionné sur l'exécutable une fois compilé).   

Note: après rédaction de ce post, j'ai découvert que le paquet `xbacklight` met à disposition un utilitaire du même genre.  <script src="http://pastebin.com/embed_js.php?i=XKGfrx0H"></script>
Il permet la même chose sauf en mode console...
