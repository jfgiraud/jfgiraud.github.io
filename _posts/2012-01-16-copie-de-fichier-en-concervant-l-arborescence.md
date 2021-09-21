---
layout: post
title: "Copie de fichier en concervant l'arborescence"
date: "2012-01-16 10:32:00"
---
$ mkdir toto/tutu/titi/<br />$ touch toto/tutu/titi/grosminet.txt<br />$ mkdir tata<br />$ cp --parents toto/tutu/titi/grosminet.txt tata<br />$ tree <br /><pre>.<br />├── tata<br />│   └── toto<br />│       └── tutu<br />│           └── titi<br />│               └── grosminet.txt<br />└── toto<br />    └── tutu<br />        └── titi<br />            └── grosminet.txt<br /></pre>