---
layout: post
title: "Perl, retirer les accents d'une chaine"
date: "2014-07-01 07:43:00"
tags: perl accent accents retirer supprimer unicode unicodedata
---

Code pour retirer les accents d'une chaîne de caractères :

```perl
#!/usr/bin/perl -CS -w

use strict;
use warnings;
use utf8;
use Unicode::Normalize;

my $test = "Portez ce vieux whisky au juge blond qui fume sur son île intérieure, à côté de l'alcôve ovoïde, où les bûches se consument dans l'âtre, ce qui lui permet de penser à la cænogénèse de l'être dont il est question dans la cause ambiguë entendue à Moÿ, dans un capharnaüm qui, pense-t-il, diminue çà et là la qualité de son œuvre.";

my $decomposed = NFD($test);
$decomposed =~ s/\p{Mn}//g;
print "$decomposed\n";
```

```bash
$ chmod +x t.pl
$ ./t.pl 
Portez ce vieux whisky au juge blond qui fume sur son ile interieure, a cote de l'alcove ovoide, ou les buches se consument dans l'atre, ce qui lui permet de penser a la cænogenese de l'etre dont il est question dans la cause ambigue entendue a Moy, dans un capharnaum qui, pense-t-il, diminue ca et la la qualite de son œuvre.
```

