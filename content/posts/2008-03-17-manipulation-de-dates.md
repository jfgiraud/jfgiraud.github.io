---
title: "Manipulation de dates"
date: 2008-03-17T10:20:00+01:00
tags: ["linux", "perl", "date"]
description: "Faut-il utiliser date::manip ?"
---

`Date::Manip` n'est pas installé par défaut avec perl. C'est embêtant car il faut installer un paquet sur chaque environnement utilisé.

En outre, dans la perldoc, voici la réponse à la question **SHOULD I USE DATE::MANIP**

>    Date::Manip is written entirely in perl.  It’s the most powerful of the
>    date modules.  It’s also the biggest and slowest.

Bref, pourquoi ne pas utiliser directement la commande date ?!

* avec perl :

    use Date::Manip;
    my $nextDate = DateCalc("$year-$month-$day 07:00:00", "+ 1 day");
    $validity_start = UnixDate($nextDate, "%Y-%m-%d 07:00:00");

* en bash

    date -d '2007-03-12 11:23:59 1 day ago' +'%Y-%m-%d %H:%M:%S'
