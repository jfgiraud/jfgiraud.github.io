---
title: "Manipulation de dates"
date: "2008-03-17 10:20:00"
---
Date::Manip n'est pas installé par défaut avec perl. C'est embêtant car il faut installer un paquet sur chaque environnement utilisé.

En outre, dans la perldoc, voici la réponse à la question <span style="font-weight:bold;">SHOULD I USE DATE::MANIP</span>

<span style="font-style:italic;">Date::Manip is written entirely in perl.  It’s the most powerful of the
       date modules.  It’s also the biggest and slowest.
</span>

Bref, pourquoi ne pas utiliser directement la commande date ?!

* avec perl :

<pre>
  use Date::Manip;
  my $nextDate = DateCalc("$year-$month-$day 07:00:00", "+ 1 day");
  $validity_start = UnixDate($nextDate, "%Y-%m-%d 07:00:00");
</pre>

* en bash

<pre>
  date -d '2007-03-12 11:23:59 1 day ago' +'%Y-%m-%d %H:%M:%S'
</pre>
