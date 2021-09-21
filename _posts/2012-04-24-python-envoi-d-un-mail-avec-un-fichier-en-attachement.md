---
layout: post
title: "python, envoi d'un mail avec un fichier en attachement"
date: "2012-04-24 12:53:00"
---
<pre><code><span style="font-family: &quot;Courier New&quot;,Courier,monospace;font-size: small;"><br />import smtplib<br />from email.MIMEText import MIMEText<br />from email.MIMEMultipart import MIMEMultipart<br />from email import Encoders<br /><br />msg = MIMEText('le texte du message')<br />msg['From']='crontab-do-not-reply@example.com'<br />msg['To']='destinataire1@example.com,destinataire2@example.com'<br />msg['Subject']='le titre du message'<br /><br />texte = MIMEText(u'Le \xe9but du message', 'plain', 'utf-8')<br />msg.attach(texte)<br /><br />content = MIMEBase('text', 'csv')<br />content.set_payload(csvbuffer)<br />Encoders.encode_base64(content)<br />content.add_header('Content-Disposition', 'attachment', filename='fichier.csv')<br />msg.attach(content)<br /><br />smtp = smtplib.SMTP(mailhost)<br />smtp.sendmail('crontab-do-not-reply@example.com', ['destinataire1@example.com', <br />                'destinataire2@example.com'], msg.as_string())<br />smtp.quit()<br /></code></span></pre>