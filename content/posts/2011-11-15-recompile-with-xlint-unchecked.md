---
title: "Recompile with -Xlint:unchecked"
date: 2011-11-15T10:31:00+01:00
tags: [ "Xlint" ]
description: "Désactiver Xlint"
---

```
   [javac] Note: src/main/java/com/orange/mbs/aiguilleur/ws/WsConfiguration.java 
uses unchecked or unsafe operations.
   [javac] Note: Recompile with -Xlint:unchecked for details.
```
La solution...

```
   <target name="compile" description="Compilation of the overall project>

       &lt;mkdir dir="${classes.dir}"&gt;
       &lt;javac srcdir="${src.dir}" destdir="${classes.dir}" debug="on" optimize="off" 
deprecation="on" source="1.5" target="1.5"&gt;
           &lt;classpath refid="classpath"&gt;
           &lt;compilerarg value="-Xlint:unchecked"&gt;
       &lt;/compilerarg>&lt;/classpath&gt;&lt;/javac&gt;
   &lt;/mkdir&gt;&lt;/target&gt;
```