---
title: "Java, retirer les accents d'une chaîne"
date: "2016-03-16 11:10:00"
tags: java accents
---
Voici le code qui permet de supprimer les accents d'une chaîne de caractères. 


```java
public String removeAccents(String text) {
    String libelle = Normalizer.normalize(text, Normalizer.Form.NFD);
    return libelle.replaceAll("\\p{Mn}+", "");
}

@Test
public void removeAccents() {
    String withAccents = "Portez ce vieux whisky au juge blond qui fume sur son île intérieure, à côté de l'alcôve ovoïde, où les bûches se consument dans l'âtre, ce qui lui permet de penser à la cænogénèse de l'être dont il est question dans la cause ambiguë entendue à Moÿ, dans un capharnaüm qui, pense-t-il, diminue çà et là la qualité de son œuvre.";
    String withoutAccents = "Portez ce vieux whisky au juge blond qui fume sur son ile interieure, a cote de l'alcove ovoide, ou les buches se consument dans l'atre, ce qui lui permet de penser a la cænogenese de l'etre dont il est question dans la cause ambigue entendue a Moy, dans un capharnaum qui, pense-t-il, diminue ca et la la qualite de son œuvre.";
    assertEquals(withoutAccents, removeAccents(withAccents));
}
```

Attention, il conserve les lettres ligaturées telles que œ et æ contrairement à la solution proposée sur [stackoverflow](http://stackoverflow.com/questions/8523631/remove-accents-from-string) où ce type de lettres sont tout simplement "supprimées".


