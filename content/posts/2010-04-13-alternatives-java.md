---
title: "Alternatives java"
date: 2010-04-13T10:14:00+01:00
tags: [ "alternatives", "linux", "java" ]
description: "Lister et positionner une alternative java"
---

On peut utiliser `update-alternatives` ou bien ceci pour : 

- Lister les alternatives java

    ```
    sudo update-java-alternatives -l
    ```

- Positionner l' alternative java

    ```
    sudo update-java-alternatives -s java-6-sun
    ```
