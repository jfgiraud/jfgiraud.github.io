---
layout: post
title: "Linux Mint Cinnamon & wifi"
date: "2012-08-28 08:18:00"
---
Hier soir j'ai désactivé le Wifi dans la widget près de l'heure. Impossible de le réactiver, même un redémarrage ne fonctionne pas !  La fenêtre "Réseau" dans les préférences montrait un bouton où le mode avion était activé et rien n'y faisait, impossible de rétablir le wifi !!  En attendant la réparation du bug...  <code><pre><br />$ rfkill list<br />0: hci0: Bluetooth<br /> Soft blocked: no<br /> Hard blocked: no<br />1: sony-wifi: Wireless LAN<br /> Soft blocked: yes<br /> Hard blocked: no<br />2: sony-bluetooth: Bluetooth<br /> Soft blocked: no<br /> Hard blocked: no<br />3: phy0: Wireless LAN<br /> Soft blocked: yes<br /> Hard blocked: yes<br />$ rfkill unblock 1<br />$ rfkill unblock 3<br /></pre></code>
