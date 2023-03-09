---
title: "python, envoi d'un mail avec un fichier en attachement"
date: 2012-04-24T12:53:00+01:00
---
<pre><code><span style="font-family: &quot;Courier New&quot;,Courier,monospace;font-size: small;">
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email import Encoders

msg = MIMEText('le texte du message')
msg['From']='crontab-do-not-reply@example.com'
msg['To']='destinataire1@example.com,destinataire2@example.com'
msg['Subject']='le titre du message'

texte = MIMEText(u'Le \xe9but du message', 'plain', 'utf-8')
msg.attach(texte)

content = MIMEBase('text', 'csv')
content.set_payload(csvbuffer)
Encoders.encode_base64(content)
content.add_header('Content-Disposition', 'attachment', filename='fichier.csv')
msg.attach(content)

smtp = smtplib.SMTP(mailhost)
smtp.sendmail('crontab-do-not-reply@example.com', ['destinataire1@example.com', 
                'destinataire2@example.com'], msg.as_string())
smtp.quit()
</code></span></pre>
