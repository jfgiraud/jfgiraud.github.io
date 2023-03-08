---
layout: post
title: "Linux, optimiser le poids des enregistrements MP3 en ligne de commande"
date: "2013-03-11 08:48:00"
---
Voici comment optimiser le poids de vos enregistrements en ligne de commande.

Pour cela vous pouvez utiliser le logiciel lame


```
$ lame --mp3input -b 128 infile.mp3 outfile.mp3
LAME 3.99.5 64bits (http://lame.sf.net)
Using polyphase lowpass filter, transition band: 16538 Hz - 17071 Hz
Encoding infile.mp3 to outfile.mp3
Encoding as 44.1 kHz j-stereo MPEG-1 Layer III (11x) 128 kbps qval=3
    Frame          |  CPU time/estim | REAL time/estim | play/CPU |    ETA 
  9492/9492  (100%)|    0:05/    0:05|    0:05/    0:05|   42.098x|    0:00 
-------------------------------------------------------------------------------
   kbps        LR    MS  %     long switch short %
  128.0        4.9  95.1        95.6   2.6   1.8
Writing LAME Tag...done
ReplayGain: -7.6dB
```

<div style="height: 0; overflow: hidden;">lame 128 encodage mp3 poids réduire réduction</div>
