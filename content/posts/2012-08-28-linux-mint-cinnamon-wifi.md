---
title: "Linux Mint Cinnamon & wifi"
date: 2012-08-28T08:18:00+01:00
tags: ["wifi"]
---
Hier soir j'ai désactivé le Wifi dans la widget près de l'heure. Impossible de le réactiver, même un redémarrage ne fonctionne pas !  La fenêtre "Réseau" dans les préférences montrait un bouton où le mode avion était activé et rien n'y faisait, impossible de rétablir le wifi !!  En attendant la réparation du bug...  

```bash
$ rfkill list
0: hci0: Bluetooth
 Soft blocked: no
 Hard blocked: no
1: sony-wifi: Wireless LAN
 Soft blocked: yes
 Hard blocked: no
2: sony-bluetooth: Bluetooth
 Soft blocked: no
 Hard blocked: no
3: phy0: Wireless LAN
 Soft blocked: yes
 Hard blocked: yes
$ rfkill unblock 1
$ rfkill unblock 3
```
