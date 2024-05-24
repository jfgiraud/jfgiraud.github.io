---
title: "Jetty 8 et paramètres d'initialisation"
date: 2012-07-17T17:14:00+01:00
tags: ["bash", "python", "encoding"]
---
La documentation sur le net est obscure quant à la manière d'initialiser les paramètres de contexte avec jetty (hors du web.xml dans le webdefault.xml (équivalent du host.xml de tomcat)). 

J'ai cherché, cherché et cherché...  

Et puis j'ai trouvé :)  Le nouveau code est le suivant :  

```
<?xml version="1.0"  encoding="ISO-8859-1"?>
<!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" 
"http://www.eclipse.org/jetty/configure.dtd">

<Configure class="org.eclipse.jetty.webapp.WebAppContext">

  <Set name="sessionHandler">
    <New class="org.eclipse.jetty.server.session.SessionHandler">
      <Arg>
        <New class="org.eclipse.jetty.server.session.HashSessionManager">
          <Set name="storeDirectory">jetty/sessions</Set>
        </New>
      </Arg>
    </New>
  </Set>
  <Get name="ServletContext">
    <Call name="setInitParameter">
      <Arg>driverSQL</Arg>
      <Arg>com.mysql.jdbc.Driver</Arg>
    </Call>
  </Get>
</Configure>
```

L'ancien code était le suivant : 

```
<?xml version="1.0"  encoding="ISO-8859-1"?>
<!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" 
"http://www.eclipse.org/jetty/configure.dtd">

<Configure class="org.eclipse.jetty.webapp.WebAppContext">
  <Set name="sessionHandler">
    <New class="org.eclipse.jetty.server.session.SessionHandler">
      <Arg>
 <New class="org.eclipse.jetty.server.session.HashSessionManager">
   <Set name="storeDirectory">jetty-sessions</Set>
 </New>
      </Arg>
    </New>
  </Set>
  <Set name="initParams">
    <Map>

      <Entry>
 <Item>driverSQL</Item>
 <Item>com.mysql.jdbc.Driver</Item>
      </Entry>
</Map>
  </Set>
</Configure>
``` 

Ce n'est pas très différent mais il fallait trouver, la documentation en ligne n'en parlant pas !  En espérant que ça vous fasse économiser de précieuses heures...  A vos servletContext.getInitParameter !!!
