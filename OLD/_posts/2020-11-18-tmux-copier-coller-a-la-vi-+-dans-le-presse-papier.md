---
title: "tmux, copier/coller à la vi + dans le presse-papier"
date: "2020-11-18 17:56:00"
tags: presse-papier tmux xclip commande bash
---
Commandes à ajouter au `~/.tmux.conf`

Dans mon cas, il s'agit d'un tmux 1.8 :

```bash
bind-key P run-shell "xclip -o | tmux load-buffer - ; tmux paste-buffer"
bind-key -t vi-copy 'v' begin-selection
bind-key -t vi-copy 'y' copy-pipe "tmux save-buffer - | xclip -sel clip -i"
bind-key -t vi-copy 'r' rectangle-toggle
```

Cela nécessite d'ajouter la commande `xclip`

Attention, l'exécution est très très lente...
