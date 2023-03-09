---
title: "“docker pull” certificate signed by unknown authority"
date: 2021-02-10T11:31:00+01:00
tags: ["docker", "certificat"]
---

For my case, the error was on "docker login" command.  

The solution I found for my ubuntu:  I downloaded the crt file via firefox (lock icon in the url adress bar) and save it : 

~/mydomain:1234.crt  

After that : 

```text  
cp ~/mydomain:1234.crt /usr/local/share/ca-certificates/
update-ca-certificates
service docker restart
```

Source: [https://stackoverflow.com/a/62404469/3550759](https://stackoverflow.com/a/62404469/3550759)
