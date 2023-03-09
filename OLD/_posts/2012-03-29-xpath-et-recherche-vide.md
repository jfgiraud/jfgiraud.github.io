---
title: "XPath et recherche vide..."
date: 2012-03-29T09:48:00+01:00
---
Recherche des lignes d'un tableau ayant dans la 3e colonne une valeur à XXX :

Si XXX est vide :
<br style="font-family: &quot;Courier New&quot;,Courier,monospace;" /><span style="font-family: &quot;Courier New&quot;,Courier,monospace; font-size: small;">//table/tr/td[3][not(text())]/..</span>

Sinon
<br style="font-family: &quot;Courier New&quot;,Courier,monospace;" /><span style="font-family: &quot;Courier New&quot;,Courier,monospace;">//table/tr/td[3][text() = '" + XXX + "']/..</span>
