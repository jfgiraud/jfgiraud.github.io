---
title: "ssh, accéder à un site derrière un VPN via une VM"
date: 2021-03-31T17:16:00+01:00
tags: ["ssh", "vpn", "vm"]
---

Un petit schéma pour expliquer comment j'accède à fitnesse depuis mon poste linux.

Le VPN est monté dans la VM, un local port forwarding permet d'accéder à fitnesse dans la VM.

Un remote port forwarding permet d'écouter et répondre aux interrogations faites depuis le poste linux.

![Montage](https://1.bp.blogspot.com/-fZ_c1F8yGvI/YGSSUWB8UPI/AAAAAAAAEdg/cTe1UzKIpNEWkuQQuTJMLYeWTbmVM7RVACNcBGAsYHQ/s1400/Capture%2Bdu%2B2021-03-31%2B17-11-05.png)

