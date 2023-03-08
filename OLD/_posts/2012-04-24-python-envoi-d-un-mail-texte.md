---
title: "python, envoi d'un mail texte"
date: "2012-04-24 11:18:00"
---
<pre><code><span style="font-family: &quot;Courier New&quot;,Courier,monospace;font-size: small;">
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
</code></span></pre>
