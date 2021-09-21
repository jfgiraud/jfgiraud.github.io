---
layout: post
title: "emacs, afficher le nom de fichier complet dans la modeline"
date: "2012-06-15 15:48:00"
---
<pre><br /><code><br />; show the full path and filename in the message area<br /><br />(defun path ()<br />  (interactive "*")<br />  (message "%s" buffer-file-name)<br />  )<br /><br />; set filename only in the Modeline display<br />(defun short-file-name ()<br />  "Display the full file path and name in the modeline"<br />  (interactive "*")<br />  (setq-default mode-line-buffer-identification '("%12b"))<br />  )<br /><br />; set the full path and filename only in the Modeline display<br />(defun long-file-name ()<br />  "Display the full file path and name in the modeline"<br />  (interactive "*")<br />  (setq-default mode-line-buffer-identification<br />    '("%S:"(buffer-file-name "%f")))<br />  )<br /><br />(long-file-name)<br /></code><br /></pre>
