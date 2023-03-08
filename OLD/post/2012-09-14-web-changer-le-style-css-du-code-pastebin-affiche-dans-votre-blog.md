---
layout: post
title: "web, changer le style css du code pastebin affiché dans votre blog"
date: "2012-09-14 13:44:00"
---
Si vous affichez du code déposé sur pastebin et que les couleurs ne conviennent pas car elles ne sont pas en accord avec les couleurs de votre blog, il est possible de les personnaliser...

Dans mon cas, j'ai ajouté le code suivant 


```javascript
<script src="http://code.jquery.com/jquery-1.8.1.min.js"></script>
<script language="javascript">
  (function () {
     $(".embedFooter").css("background", "#666666");
     $(".embedFooter a").css({"color": "#ffffff"});
     $(".embedPastebin").css("background", "#eeeeee");
     $(".de1").css("background", "#eeeeee");
     $(".de2").css("background", "#eeeeee");
   })();
</script>
```

dans un gadget du blog que vous consultez actuellement (cf Conception>Mise en page).

Cela a pour effet de changer le css des éléments trouvés au chargement de la page.
