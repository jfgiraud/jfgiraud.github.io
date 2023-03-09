---
title: "Linux, niveau de la baterie"
date: 2012-09-23T15:46:00+01:00
tags: ["acpi"]
---
Une petite commande pour connaitre le niveau de la baterie...


```
$ acpi -V
Battery 0: Charging, 25%, 01:59:29 until charged
Battery 0: design capacity 4390 mAh, last full capacity 4390 mAh = 100%
Adapter 0: on-line
Thermal 0: ok, 37.0 degrees C
Thermal 0: trip point 0 switches to mode critical at temperature 96.0 degrees C
Thermal 0: trip point 1 switches to mode passive at temperature 106.0 degrees C
Cooling 0: LCD 0 of 15
Cooling 1: Processor 0 of 10
Cooling 2: Processor 0 of 10
Cooling 3: Processor 0 of 10
Cooling 4: Processor 0 of 10
```

Cela peut être utile lorsque l'on est en mode console sur son portable...

