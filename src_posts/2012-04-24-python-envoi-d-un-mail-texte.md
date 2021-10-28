---
layout: post
title: "python, envoi d'un mail texte"
date: "2012-04-24 11:18:00"
---
<pre><code><span style="font-family: &quot;Courier New&quot;,Courier,monospace;font-size: small;"><br />import smtplib<br />from email.MIMEText import MIMEText<br /><br />msg = MIMEText('le texte du message')<br />msg['From']='crontab-do-not-reply@example.com'<br />msg['To']='destinataire1@example.com,destinataire2@example.com'<br />msg['Subject']='le titre du message'<br /><br />smtp = smtplib.SMTP(mailhost)<br />smtp.sendmail('crontab-do-not-reply@example.com', ['destinataire1@example.com', <br />                'destinataire2@example.com'], msg.as_string())<br />smtp.quit()<br /></code></span></pre>
