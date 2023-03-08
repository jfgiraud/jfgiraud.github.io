---
title: "java, regexp nommées"
date: "2020-10-07 22:50:00"
tags: java regexp
---

Nommer un groupe et l'utiliser :

```java
    @Test
    public void testFoo() {
        Pattern p = Pattern.compile("Voici le nombre : (?<nombre>\\d+)");
        Matcher m = p.matcher("Voici le nombre : 123");
        assertTrue(m.matches());
        assertEquals("123", m.group("nombre"));
    }

```

