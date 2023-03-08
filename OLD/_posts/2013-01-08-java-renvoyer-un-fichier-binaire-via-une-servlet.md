---
title: "Java, renvoyer un fichier binaire via une servlet"
date: "2013-01-08 17:22:00"
tags: java, setContentType, addHeader, HttpServletRequest req, HttpServletResponse resp,Pragma,msword, getServletContext, getRealPath, FileInputStream, ServletOutputStream, IOUtils, copy
---

```java
package xxxx;

import java.io.FileInputStream;
import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.io.IOUtils;


public class GetManualServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("application/msword");
        resp.addHeader( "Content-Transfer-Encoding", "binary" );
        resp.addHeader("Pragma", "no-cache");
        resp.addHeader("Cache-Control", "no-cache, max-age=0, must-revalidate");
        resp.addHeader("Content-Disposition", "attachment; fileName=\"ManuelUtilisateur.docx\";");
        
        String path = getServletContext().getRealPath("doc/ManuelUtilisateur.docx");
        
        FileInputStream in = new FileInputStream(path);
        try {
            ServletOutputStream out = resp.getOutputStream();
            IOUtils.copy(in, out);
            out.flush();
        } finally {
            in.close();
        }
        
    }

}
```

