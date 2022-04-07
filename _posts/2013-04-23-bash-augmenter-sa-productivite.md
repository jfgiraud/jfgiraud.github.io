---
layout: post
title: "bash, augmenter sa productivité"
date: "2013-04-23 11:19:00"
---

```
Bash Bang (!) Commands

Bash also has some handy features that use the ! (bang) to allow you to do some funky stuff with bash commands.

    !! - run last command
    !blah – run the most recent command that starts with ‘blah’ (e.g. !ls)
    !blah:p – print out the command that !blah would run (also adds it as the latest command in the command history)
    !$ – the last word of the previous command (same as Alt + .)
    !$:p – print out the word that !$ would substitute
    !* – the previous command except for the last word (e.g. if you type ‘find some_file.txt /‘, then !* would give you ‘find some_file.txt‘)
    !*:p – print out what !* would substitute
```

Trouvé [ici](http://www.skorks.com/2009/09/bash-shortcuts-for-maximum-productivity/)
