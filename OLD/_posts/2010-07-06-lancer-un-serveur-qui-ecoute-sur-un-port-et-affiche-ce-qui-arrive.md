---
layout: post
title: "lancer un serveur qui écoute sur un port et affiche ce qui arrive"
date: "2010-07-06 11:27:00"
---
socat TCP4-LISTEN:7533,reuseaddr STDOUT
