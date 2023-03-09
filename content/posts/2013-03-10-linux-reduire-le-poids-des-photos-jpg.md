---
title: "Linux, réduire le poids des photos jpg"
date: 2013-03-10T18:59:00+01:00
---
Je viens de découvrir un petit logiciel sympa réduire le poids des photos jpg et ce, en ligne de commandes.

Il s'agit du logiciel jpegoptim.

C'est très pratique pour réduire le poids de scans afin de les envoyer par emails :)


```
$ sudo apt-get install jpegoptim
$ jpegoptim -m70 DemandeRemboursementRadioThorax-*
DemandeRemboursementRadioThorax-1.jpg 2552x3508 24bit JFIF  [OK] 1021137 --> 363084 bytes (64.44%), optimized.
DemandeRemboursementRadioThorax-2.jpg 2552x3508 24bit JFIF  [OK] 940214 --> 321868 bytes (65.77%), optimized.
```
