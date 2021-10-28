---
layout: post
title: "Manipulation de dates"
date: "2008-03-17 10:20:00"
---
Date::Manip n'est pas installé par défaut avec perl. C'est embêtant car il faut installer un paquet sur chaque environnement utilisé.<br /><br />En outre, dans la perldoc, voici la réponse à la question <span style="font-weight:bold;">SHOULD I USE DATE::MANIP</span><br /><br /><span style="font-style:italic;">Date::Manip is written entirely in perl.  It’s the most powerful of the<br />       date modules.  It’s also the biggest and slowest.<br /></span><br /><br />Bref, pourquoi ne pas utiliser directement la commande date ?!<br /><br />* avec perl :<br /><br /><pre><br />  use Date::Manip;<br />  my $nextDate = DateCalc("$year-$month-$day 07:00:00", "+ 1 day");<br />  $validity_start = UnixDate($nextDate, "%Y-%m-%d 07:00:00");<br /></pre><br /><br />* en bash<br /><br /><pre><br />  date -d '2007-03-12 11:23:59 1 day ago' +'%Y-%m-%d %H:%M:%S'<br /></pre>
