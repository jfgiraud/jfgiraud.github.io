---
layout: post
title: "docker, tests karma dans un container docker"
date: "2020-06-22 16:13:00"
---
Je suis novice en docker / gitlab ci/cd mais je m'y mets depuis la semaine dernière. <br /><br />Mon ancienne machine de dév avait été transformée en jenkins. Elle a son disque qui a "cramé" et c'est donc  l'occasion de changer de technologie...<br /><br />Le projet supervisé a des tests karma.<br />Lors du portage sur git ci/cd, les tests étaient gelés jusqu'au claquage d'un timeout (cf traces ci-après). <br />Ca ne se passait que dans gitlab ci/cd. En local, hors du container docker tout était OK, dans le container, c'était KO<br /><br /><script src="https://pastebin.com/embed_js/pGAg05sY"></script><br /><br />Dans mon cas, il manquait simplement l'installation de firefox lors de la création de l'image docker...<br /><br /><script src="https://pastebin.com/embed_js/Ydsz9e3h"></script><br /><br />Après ajout, c'est bon (ouf de soulagement) <br />Il faut dire que l'erreur n'était pas très explicite. Beaucoups de fils de discussion parlent de problèmes de proxy...<br /><br /><br />
