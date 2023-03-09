---
title: "C, compiler un projet avec autoconf, automake & consors"
date: 2012-11-07T22:49:00+01:00
---
Si le projet met à disposition un fichier autogen.sh, utilisez-le.

Sinon, exécutez les commandes suivantes pour reconfigurer et recompiler le projet :



- <b>autoreconf --force --install</b> - lance aclocal, autoconf, autoheader et automake dans le bon ordre pour créer config.h.in, Makefile.in, configure et un certain nombre de fichiers auxiliaires
- <b>./configure</b> - crée le fichier Makefile à partir du fichier Makefile.in et config.h à partir du fichier config.h.in - <b>make</b>





