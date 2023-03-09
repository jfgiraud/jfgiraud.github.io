---
title: "java, lambda et jointure de chaines"
date: 2020-11-12T14:26:00+01:00
tags: ["java", "jointure", "chaines"]
---

Faire une concaténation de chaînes avec les lambdas :

```java
@Test
public void testFoo() throws Exception {
    List<String> l = Arrays.asList("a", "b", "c");
    assertEquals("[a],[b],[c]", l.stream().map(v->String.format("[%s]", v)).collect(Collectors.joining(",")));
}
```

