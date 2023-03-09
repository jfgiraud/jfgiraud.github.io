---
title: "archlinux, problème de clé sur mise à jour beautiful-soup4"
date: 2015-10-24T11:34:00+01:00
tags: ["archlinux", "gpg", "clés", "key"]
---

```
erreur: python-beautifulsoup4: key "Daniel Wallace <danielwallace@gtmanfred.com>" is disabled
:: Le fichier /var/cache/pacman/pkg/python-beautifulsoup4-4.4.1-1-any.pkg.tar.xz est corrompu (paquet invalide ou corrompu (signature PGP)).
```


```
# pacman-key --edit-key 'danielwallace@gtmanfred.com'

pub  rsa2048/4F010D48
     créé: 2012-03-02  expire: jamais      utilisation: SC  
     confiance: inconnu       validité: totale
*** Cette clef a été désactivée
sub  rsa2048/182ADEA0
     créé: 2012-03-02  expire: jamais      utilisation: E   
[  totale ] (1). Daniel Wallace <danielwallace@gtmanfred.com>
[  totale ] (2)  Daniel Wallace <daniel.wallace12@gmail.com>
[  totale ] (3)  Daniel Wallace (gtmanfred) <daniel.wallace@gatech.edu>
[ révoquée] (4)  Daniel Wallace (gmail account) <daniel.wallace12@gmail.com>

gpg> enable
```
