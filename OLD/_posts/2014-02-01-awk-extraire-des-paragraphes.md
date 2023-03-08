---
title: "awk, extraire des paragraphes"
date: "2014-02-01 08:07:00"
---
Avec awk, il est possible d'extraire des paragraphes spécifiques par leur ordre d'apparence.

Il faut positionner le séparateur d'enregistrements RS et donner les numéros de paragraphe que
l'on souhaite extraire via un if comme dans l'exemple ci-dessous.


```
$ cat a
NODE-ID> command1

Lorem ipsum dolor 
sit amet, consectetuer adipiscing 
elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.


NODE-ID> command2


Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.

NODE-ID> command3

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.


$ cat a |  awk 'BEGIN { RS=""; i=0; } { ++i; if (i==2 || i==6) print $0; }'
Lorem ipsum dolor 
sit amet, consectetuer adipiscing 
elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.
```
