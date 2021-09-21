---
layout: post
title: "Recompile with -Xlint:unchecked"
date: "2011-11-15 10:31:00"
---
<pre><code><small><br />   [javac] Note: src/main/java/com/orange/mbs/aiguilleur/ws/WsConfiguration.java <br />uses unchecked or unsafe operations.<br />   [javac] Note: Recompile with -Xlint:unchecked for details.<br /></small></code><br /></pre><br /><br />La solution...<br /><br /><pre><code><small><br />   &lt;target name="compile" description="Compilation of the overall project"&gt;<br /><br />       &lt;mkdir dir="${classes.dir}"&gt;<br />       &lt;javac srcdir="${src.dir}" destdir="${classes.dir}" debug="on" optimize="off" <br />deprecation="on" source="1.5" target="1.5"&gt;<br />           &lt;classpath refid="classpath"&gt;<br />           &lt;compilerarg value="-Xlint:unchecked"&gt;<br />       &lt;/compilerarg>&lt;/classpath&gt;&lt;/javac&gt;<br />   &lt;/mkdir&gt;&lt;/target&gt;<br /></small><br /></code><br /></pre>