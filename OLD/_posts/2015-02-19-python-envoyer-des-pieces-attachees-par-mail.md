---
title: "Python, envoyer des pièces attachées par mail"
date: 2015-02-19T14:23:00+01:00
tags: ["python", "mail"]
---

```
#!/usr/bin/python3

import smtplib
import os
import mimetypes

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders
from email.Utils import COMMASPACE, formatdate


def send_mail(send_from, send_to, subject, text, files=[], smtp_server='smtp.example.com'):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )
    
    for f in files:
        (mimetype, encoding) = mimetypes.guess_type(f)
        if mimetype is not None:
            part = MIMEBase(*mimetype.split('/',2))
        else:
            part = MIMEBase('application', "octet-stream")
        part.set_payload( ''.join(open(f,'rb').readlines()) )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(smtp_server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

me = 'me@example.com'
to = [ 'you@example.com' ]
smtp_server = 'smtp.example.com'
files = [ '/path/to/the/file.ext', '/path/to/the/other/file.ext' ]
message = 'Veuillez trouver les documents ci-joints'

send_mail(me, to, 'Titre', message, files, smtp_server)
```
