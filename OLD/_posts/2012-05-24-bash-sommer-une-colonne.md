---
title: "bash, sommer une colonne...."
date: "2012-05-24 16:11:00"
---
Comment sommer des valeurs provenant d'un fichier ou de la sortie standard.  Voici plusieurs solutions...


A la `awk` : <code></code>
<pre><code>printf "1\n2\n3\n" | awk '{s+=$1} END {print s}'
</code></pre>
A la `tr` : <code></code>
<pre><code>printf "1\n2\n3\n"| tr '\n' '+' | sed -e 's/+$/\n/' | bc
</code></pre>
A la `paste` : <code></code>
<pre><code>printf "1\n2\n3\n" | paste -sd+ | bc
</code></pre>
Moi je choisis la troisième solution. Elle est plus courte, simple et efficace !!

