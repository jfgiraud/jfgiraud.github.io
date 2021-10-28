---
layout: post
title: "ssh, exécuter un sudo par ssh sans saisir son mot de passe (pour sudo)..."
date: "2016-02-12 10:57:00"
---
Dans le cadre de mon projet, on souhaitait pouvoir exécuter des redémarrages de services depuis son poste local sur des machines accessibles par ssh mais dont on n'avait pas accès au compte root.<br /><br />Le service est cependant redémmarrable via sudo mais un mot de passe était demandé.<br /><br />Nous avons mis en place un script qui lit dans un fichier de conf le mot de passe et exécute le sudo (et remplis le mot de passe du sudo) par ssh.<br /><br />Cela donne un code comme ceci :<br /><br /><script src="//pastebin.com/embed_js/mLRT0FFd"></script>
