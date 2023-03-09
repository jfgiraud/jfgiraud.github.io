---
title: "emacs, afficher le nom de fichier complet dans la modeline"
date: 2012-06-15T15:48:00+01:00
---
<pre>
<code>
; show the full path and filename in the message area

(defun path ()
  (interactive "*")
  (message "%s" buffer-file-name)
  )

; set filename only in the Modeline display
(defun short-file-name ()
  "Display the full file path and name in the modeline"
  (interactive "*")
  (setq-default mode-line-buffer-identification '("%12b"))
  )

; set the full path and filename only in the Modeline display
(defun long-file-name ()
  "Display the full file path and name in the modeline"
  (interactive "*")
  (setq-default mode-line-buffer-identification
    '("%S:"(buffer-file-name "%f")))
  )

(long-file-name)
</code>
</pre>
