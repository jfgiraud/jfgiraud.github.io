---
layout: post
title: "C, compiler un projet avec autoconf, automake & consors"
date: "2012-11-07 22:49:00"
---
Si le projet met à disposition un fichier autogen.sh, utilisez-le.<br /><br />Sinon, exécutez les commandes suivantes pour reconfigurer et recompiler le projet :<br /><br /><ul><li><b>autoreconf --force --install</b></li> - lance aclocal, autoconf, autoheader et automake dans le bon ordre pour créer config.h.in, Makefile.in, configure et un certain nombre de fichiers auxiliaires</li><li><b>./configure</b></li> - crée le fichier Makefile à partir du fichier Makefile.in et config.h à partir du fichier config.h.in <li><b>make</b></li></ul><br /><br /><br />
