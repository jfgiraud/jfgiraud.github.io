---
layout: post
title: "java, déboires d'encoding..."
date: "2012-09-25 12:47:00"
tags: java, encoding, charset, utf-8, iso-8859
---
Il y a quelques temps, j'ai eu de petits problèmes d'affichage d'accents sur une IHM d'un fichier qui était fourni par une autre appplication.

Le charset n'était pas le bon.

Il a fallu que je force l'écriture du charset et sa lecture. 

Pour l'écriture :


```java
package a.b.c;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Writer;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.io.IOUtils;

public class GetFileServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        
        String path = req.getParameter("path");
        
	path = getServletContext().getRealPath("/") + path;
        path = path.replaceAll("//", "/");
        
        resp.setContentType("text/plain");
        resp.setCharacterEncoding("UTF-8");
        resp.addHeader("Pragma", "no-cache");
        resp.addHeader("Cache-Control", "no-cache, max-age=0, must-revalidate");

        InputStream in = new FileInputStream(path);
        Writer out = resp.getWriter();
        try {
            IOUtils.copy(in, out, "UTF-8");
        } finally {
            in.close();
        }
    }

}
```

Pour la lecture : 


```java
package x.y.z;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.Writer;
import java.net.URL;
import java.net.URLConnection;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.io.IOUtils;

public class GetFileServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("text/plain");
        resp.setCharacterEncoding("UTF-8");
        resp.addHeader("Pragma", "no-cache");
        resp.addHeader("Cache-Control", "no-cache, max-age=0, must-revalidate");

        String sviUrl = getServletContext().getInitParameter("sviUrl");
        if (! sviUrl.endsWith("/"))
            sviUrl += "/";
        
        String file = req.getParameter("file");
        
        sviUrl += "get-file?file=" + file;
        
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
        
    }

}
```


