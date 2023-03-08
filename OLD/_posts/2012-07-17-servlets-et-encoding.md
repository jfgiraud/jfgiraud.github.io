---
layout: post
title: "Servlets et encoding..."
date: "2012-07-17 12:42:00"
---
J'ai eu des petit soucis avec le charset...

 Un svi envoyait bien "text/csv; charset=utf-8" (curl) mais pour une raison x ou y, mon ihm qui l'appelait voyait "text/plain;charset=ISO-8859-1" ce qui faisait que le fichier était mal affiché.

 Dans le code ci-dessous, j'ouvre une connection et récupère le charset afin d'initialiser l'InputStreamReader et commencer les lectures...  <code><pre>
        URL url = new URL(sviUrl);
        URLConnection conn = url.openConnection();  
        conn.connect();
        InputStream in = null;
        try {
            String charset = "ISO-8859-1";
            String contentType = conn.getContentType(); 
            if (contentType != null && contentType.indexOf(";charset=") >= 0) {
                contentType = contentType.substring(contentType.indexOf(";charset=")+9);
                charset = contentType.trim();
            }
            in = conn.getInputStream();
            InputStreamReader inr = new InputStreamReader(url.openStream(), charset);
            Writer out = resp.getWriter();
            try {
                IOUtils.copy(inr, out);
            } finally {
                inr.close();
            }
        } finally {
            if (in != null) {
                in.close();
            }
        }
</pre></code>
