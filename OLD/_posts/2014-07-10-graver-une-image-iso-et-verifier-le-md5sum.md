---
title: "Graver une image iso et vérifier le md5sum"
date: "2014-07-10 20:39:00"
---

```
isofile=/home/jfgiraud/linuxmint-17-cinnamon-64bit-v2.iso
growisofs -dvd-compat -Z /dev/sr0=$isofile 
blocks=$(expr $(du -b $isofile | awk '{print $1}') / 2048)
dd if=/dev/sr0 bs=2048 count=$blocks | md5sum
md5sum $isofile
```

<div style="height: 0; overflow: hidden;">iso growisofs dvd compat sr0 dd if bs count
</div>
