---
title: "tmux, Copier/coller"
date: 2021-12-07T10:07:00+01:00
tags: [ "tmux" ]
description: "Copier/coller avec la souris"
---

Sélectionnez avec la souris.

Utilisez `ctrl` `shift` `v` pour coller la sélection.

```
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'

set -g mouse on
set -g @yank_selection 'clipboard'
set -g @yank_selection_mouse 'clipboard'

run -b '/usr/share/tmux-plugin-manager/tpm'

bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-selection
bind-key -T copy-mode-vi r send-keys -X rectangle-toggle
```
