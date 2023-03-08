---
title: "bash, presse-papier"
date: "2012-05-24 11:17:00"
---
Il est possible de copier un fichier ou la sortie standard dans le presse papier...  Il suffit d'utiliser la commande <pre>xsel</pre>Exemple : 
<pre><code>
$ cat /etc/fstab | xsel -b
</code></pre>
La commande xclip un peu similaire permet la même chose...
<pre><code>
$ sudo apt-get install xclip# Downloads and installs xclip
$ xclip -sel clip < ~/.ssh/id_rsa.pub
</code></pre>
