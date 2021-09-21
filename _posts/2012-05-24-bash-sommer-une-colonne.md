---
layout: post
title: "bash, sommer une colonne...."
date: "2012-05-24 16:11:00"
---
Comment sommer des valeurs provenant d'un fichier ou de la sortie standard.  Voici plusieurs solutions...<br /><br /><br />A la <tt>awk</tt> : <code></code><br /><pre><code>printf "1\n2\n3\n" | awk '{s+=$1} END {print s}'<br /></code></pre><br />A la <tt>tr</tt> : <code></code><br /><pre><code>printf "1\n2\n3\n"| tr '\n' '+' | sed -e 's/+$/\n/' | bc<br /></code></pre><br />A la <tt>paste</tt> : <code></code><br /><pre><code>printf "1\n2\n3\n" | paste -sd+ | bc<br /></code></pre><br />Moi je choisis la troisième solution. Elle est plus courte, simple et efficace !!<br />