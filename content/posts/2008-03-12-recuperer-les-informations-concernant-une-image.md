---
title: "Récupérer les informations concernant une image"
date: 2008-03-12T11:47:00+01:00
tags: [ "bash", "image", "information", "commande", "imagemagick" ]
description: "Gagnez en productivité !"
---

La commande est `imagemagick`. 

```shell
$ sudo apt-get install imagemagick
```
```shell
$ identify original.jpg
```
```console
original.jpg JPEG 460x460 460x460+0+0 8-bit sRGB 33596B 0.000u 0:00.000
```
```shell
$ identify -verbose original.jpg
```
```console
Image:
  Filename: original.jpg
  Format: JPEG (Joint Photographic Experts Group JFIF format)
  Mime type: image/jpeg
  Class: DirectClass
  Geometry: 460x460+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 211600
    Red:
      min: 0  (0)
      max: 247 (0.968627)
      mean: 62.3865 (0.244653)
      standard deviation: 70.4595 (0.276312)
      kurtosis: -0.426495
      skewness: 0.956078
      entropy: 0.869357
    Green:
      min: 0  (0)
      max: 241 (0.945098)
      mean: 81.3109 (0.318866)
      standard deviation: 60.0806 (0.23561)
      kurtosis: -0.484856
      skewness: 0.878619
      entropy: 0.93076
    Blue:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 94.9396 (0.372312)
      standard deviation: 50.3896 (0.197606)
      kurtosis: -0.134958
      skewness: 0.938605
      entropy: 0.904229
  Image statistics:
    Overall:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 79.5456 (0.311944)
      standard deviation: 60.3099 (0.236509)
      kurtosis: -0.500266
      skewness: 0.722652
      entropy: 0.901449
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33)
    green primary: (0.3,0.6)
    blue primary: (0.15,0.06)
    white point: (0.3127,0.329)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 460x460+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: JPEG
  Quality: 75
  Orientation: Undefined
  Properties:
    date:create: 2023-03-11T09:55:14+00:00
    date:modify: 2023-03-11T09:55:14+00:00
    jpeg:colorspace: 2
    jpeg:sampling-factor: 2x2,1x1,1x1
    signature: 5b6ab8339689d544c345577984dc4f199b684e41e1bf0153ba2391987a0e941c
  Artifacts:
    filename: IdeaProjects/jfgiraud.github.io/static/original.jpg
    verbose: true
  Tainted: False
  Filesize: 33596B
  Number pixels: 211600
  Pixels per second: 31.4273MB
  User time: 0.010u
  Elapsed time: 0:01.006
  Version: ImageMagick 6.9.11-60 Q16 x86_64 2021-01-25 https://imagemagick.org
```
