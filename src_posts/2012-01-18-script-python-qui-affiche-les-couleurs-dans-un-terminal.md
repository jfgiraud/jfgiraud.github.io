---
layout: post
title: "Script python qui affiche les couleurs dans un terminal"
date: "2012-01-18 10:28:00"
---
<pre>class bcolors:<br />    HEADER = '\033[95m'<br />    OKBLUE = '\033[94m'<br />    OKGREEN = '\033[92m'<br />    WARNING = '\033[93m'<br />    FAIL = '\033[91m'<br />    ENDC = '\033[0m'<br /><br />    def disable(self):<br />        self.HEADER = ''<br />        self.OKBLUE = ''<br />        self.OKGREEN = ''<br />        self.WARNING = ''<br />        self.FAIL = ''<br />        self.ENDC = ''<br /><br />print '===> ' +  bcolors.OKGREEN + where + bcolors.ENDC + " " + href<br /></pre>
