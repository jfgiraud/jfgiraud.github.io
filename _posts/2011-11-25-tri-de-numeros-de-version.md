---
layout: post
title: "Tri de numéros de version"
date: "2011-11-25 14:20:00"
---
<pre><code><small><br />$ cat ~/a <br />9.1.1<br />9.4.14<br />9.4.6<br />$ export LC_ALL=C ; cat ~/a | sort -t. -n -k1 -k2 -k3<br />9.1.1<br />9.4.14<br />9.4.6<br />=> pas bon<br />$ export LC_ALL=fr_FR.UTF-8 ; cat ~/a | sort -t. -n -k1 -k2 -k3<br />9.1.1<br />9.4.6<br />9.4.14<br />=> bon<br />$ export LC_ALL=C ; cat ~/a | sort -t. -k1,1n -k2,2n -k3,3n<br />9.1.1<br />9.4.6<br />9.4.14<br />=> bon<br /></small></code></pre><br /><br />Sinon si l'option est disponible (version récente de la commande)<br /><br /><pre><code><small><br />cat ~a | sort --version<br /></small></code></pre>
