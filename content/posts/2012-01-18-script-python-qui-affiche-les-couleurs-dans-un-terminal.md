---
title: "Script python qui affiche les couleurs dans un terminal"
date: 2012-01-18T10:28:00+01:00
tags: ["colors"]
---

```
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

print '===> ' +  bcolors.OKGREEN + where + bcolors.ENDC + " " + href
```
