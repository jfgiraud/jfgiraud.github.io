---
layout: post
title: "bash, boucles for"
date: "2012-08-07 12:24:00"
---
En bash, on aurait tendance à penser que "for line in $(cat fichier)" renvoie les lignes mais c'est faux car les séparateurs par défaut sont les espaces, tabulations... On itère donc sur la liste des mots...

Pour palier à ce soucis, on peut jouer en modifiant la variable IFS et en la restaurant ensuite.

Cela donne :  <code><pre>old_IFS=$IFS     
IFS=$'\n'      
for line in $(cat fichier)        
do        
   echo "La ligne est : $line"
done        
IFS=$old_IFS    
</pre></code>  Une méthode plus subtile mais tout aussi jolie est d'utiliser read et while...  Cela donne maintenant :  <code><pre>cat fichier | while read line || [[ $line ]]
do        
   echo "La ligne est : $line"
done        
</pre></code>

C'est quand même moins tordu ;)

A noter, le [[ $line ]] permet de prendre en compte la dernière ligne s'il n'y a pas de retour chariot.
