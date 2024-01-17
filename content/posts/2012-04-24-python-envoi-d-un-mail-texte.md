---
title: "python, envoi d'un mail texte"
date: 2012-04-24T11:18:00+01:00
tags: ["python", "mail"]
description: "code pour envoyer un mail"
---

```
import smtplib
from email.MIMEText import MIMEText

msg = MIMEText('le texte du message')
msg['From']='crontab-do-not-reply@example.com'
msg['To']='destinataire1@example.com,destinataire2@example.com'
msg['Subject']='le titre du message'

smtp = smtplib.SMTP(mailhost)
smtp.sendmail('crontab-do-not-reply@example.com', ['destinataire1@example.com', 
                'destinataire2@example.com'], msg.as_string())
smtp.quit()
```
