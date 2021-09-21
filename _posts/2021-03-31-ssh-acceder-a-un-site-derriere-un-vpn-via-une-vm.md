---
layout: post
title: "ssh, accéder à un site derrière un VPN via une VM"
date: "2021-03-31 17:16:00"
---
Un petit schéma pour expliquer comment j'accède à fitnesse depuis mon poste linux.<br/><br/> Le VPN est monté dans la VM, un local port forwarding permet d'accéder à fitnesse dans la VM.<br/><br/> Un remote port forwarding permet d'écouter et répondre aux interrogations faites depuis le poste linux.<br/><br/> <div class="separator" style="clear: both;"><a href="https://1.bp.blogspot.com/-fZ_c1F8yGvI/YGSSUWB8UPI/AAAAAAAAEdg/cTe1UzKIpNEWkuQQuTJMLYeWTbmVM7RVACNcBGAsYHQ/s1400/Capture%2Bdu%2B2021-03-31%2B17-11-05.png" style="display: block; padding: 1em 0; text-align: center; "><img alt="" border="0" width="600" data-original-height="851" data-original-width="1400" src="https://1.bp.blogspot.com/-fZ_c1F8yGvI/YGSSUWB8UPI/AAAAAAAAEdg/cTe1UzKIpNEWkuQQuTJMLYeWTbmVM7RVACNcBGAsYHQ/s600/Capture%2Bdu%2B2021-03-31%2B17-11-05.png"/></a></div>
