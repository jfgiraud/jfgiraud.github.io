---
layout: post
title: "bash, presse-papier"
date: "2012-05-24 11:17:00"
---
Il est possible de copier un fichier ou la sortie standard dans le presse papier...  Il suffit d'utiliser la commande <pre>xsel</pre>Exemple : <br /><pre><code><br />$ cat /etc/fstab | xsel -b<br /></code></pre><br />La commande xclip un peu similaire permet la même chose...<br /><pre><code><br />$ sudo apt-get install xclip# Downloads and installs xclip<br />$ xclip -sel clip < ~/.ssh/id_rsa.pub<br /></code></pre>
