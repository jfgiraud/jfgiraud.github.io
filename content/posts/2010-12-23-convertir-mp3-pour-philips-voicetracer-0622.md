---
title: "Convertir Mp3 pour philips voicetracer 0622"
date: 2010-12-23T05:59:00+01:00
tags: [ "conversion", "mp3", "lame" ]
description: "Convertir un fichier dans un format compatible avec le dictaphone voicetracer 0622"
---

    $ file DVT_A001.MP3 
    DVT_A001.MP3: MPEG ADTS, layer III, v2,  64 kbps, 22.05 kHz, Monaural

    $ lame --mp3input -b 64 -m m --resample 22.05 lsdlrm.MP3 DVT_B002.MP3
    
    $ ls /mnt/PHILIPS/VOICE/B/
    DVT_B001.MP3

    $ cp DVT_B002.MP3 /mnt/PHILIPS/VOICE/B/
