---
layout: post
title: "“docker pull” certificate signed by unknown authority"
date: "2021-02-10 11:31:00"
---
  For my case, the error was on "docker login" command.  The solution I found for my ubuntu:  I downloaded the crt file via firefox (lock icon in the url adress bar) and save it : ~/mydomain:1234.crt  After that :  <script src="https://pastebin.com/embed_js/iZiCMxcJ"></script>  Source: https://stackoverflow.com/a/62404469/3550759