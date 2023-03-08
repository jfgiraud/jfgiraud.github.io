---
layout: post
title: "Jetty, démarrer sur un port déterminé"
date: "2013-04-19 11:42:00"
---
Cela se passe dans le build.xml


```
<typedef name="selectChannelConnector" classname="org.eclipse.jetty.server.nio.SelectChannelConnector"
                            classpathref="jetty.plugin.classpath" loaderref="jetty.loader" />

<target name="webapp-run" depends="create-manifest,build" description="Run website in local">
	<jetty tempDirectory="jetty-temp">
		<connectors>
			<selectChannelConnector port="8090" />
		</connectors>
		<webApp name="webapp" contextpath="/" warfile="target" webXmlFile="src/main/webapp/WEB-INF/web.xml" scanIntervalSeconds="5" jettyEnvXml="src/main/webapp/conf/dev/jetty-env.xml">
			<lib dir="src/main/webapp/WEB-INF/lib/" includes="*.jar" />
				<classes dir="${classes.dir}" />
					<scanTargets dir="src/main">
						<include name="webapp/html/*.tpl" />
						<include name="webapp/html/*.properties" />
						<include name="webapp/css/*.css" />
						<include name="webapp/js/*.js" />
					</scanTargets>
		</webApp>
	</jetty>
</target>
```

<div style="height: 0; overflow: hidden;">port jetty ant webapp connector</div>
