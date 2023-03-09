---
title: "Jetty 8 et paramètres d'initialisation"
date: 2012-07-17T17:14:00+01:00
---
La documentation sur le net est obscure quant à la manière d'initialiser les paramètres de contexte avec jetty (hors du web.xml dans le webdefault.xml (équivalent du host.xml de tomcat)). 

J'ai cherché, cherché et cherché...  

Et puis j'ai trouvé :)  Le nouveau code est le suivant :  <pre><code>
&lt;?xml version="1.0"  encoding="ISO-8859-1"?&gt;
&lt;!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" 
"http://www.eclipse.org/jetty/configure.dtd"&gt;

&lt;Configure class="org.eclipse.jetty.webapp.WebAppContext"&gt;

  &lt;Set name="sessionHandler"&gt;
    &lt;New class="org.eclipse.jetty.server.session.SessionHandler"&gt;
      &lt;Arg&gt;
        &lt;New class="org.eclipse.jetty.server.session.HashSessionManager"&gt;
          &lt;Set name="storeDirectory"&gt;jetty/sessions&lt;/Set&gt;
        &lt;/New&gt;
      &lt;/Arg&gt;
    &lt;/New&gt;
  &lt;/Set&gt;
  &lt;Get name="ServletContext"&gt;
    &lt;Call name="setInitParameter"&gt;
      &lt;Arg&gt;driverSQL&lt;/Arg&gt;
      &lt;Arg&gt;com.mysql.jdbc.Driver&lt;/Arg&gt;
    &lt;/Call&gt;
  &lt;/Get&gt;
&lt;/Configure&gt;
</code></pre> L'ancien code était le suivant :  <pre><code>
&lt;?xml version="1.0"  encoding="ISO-8859-1"?&gt;
&lt;!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" 
"http://www.eclipse.org/jetty/configure.dtd"&gt;

&lt;Configure class="org.eclipse.jetty.webapp.WebAppContext"&gt;
  &lt;Set name="sessionHandler"&gt;
    &lt;New class="org.eclipse.jetty.server.session.SessionHandler"&gt;
      &lt;Arg&gt;
 &lt;New class="org.eclipse.jetty.server.session.HashSessionManager"&gt;
   &lt;Set name="storeDirectory"&gt;jetty-sessions&lt;/Set&gt;
 &lt;/New&gt;
      &lt;/Arg&gt;
    &lt;/New&gt;
  &lt;/Set&gt;
  &lt;Set name="initParams"&gt;
    &lt;Map&gt;

      &lt;Entry&gt;
 &lt;Item&gt;driverSQL&lt;/Item&gt;
 &lt;Item&gt;com.mysql.jdbc.Driver&lt;/Item&gt;
      &lt;/Entry&gt;
&lt;/Map&gt;
  &lt;/Set&gt;
&lt;/Configure&gt;
</code></pre> Ce n'est pas très différent mais il fallait trouver, la documentation en ligne n'en parlant pas !  En espérant que ça vous fasse économiser de précieuses heures...  A vos servletContext.getInitParameter !!!
