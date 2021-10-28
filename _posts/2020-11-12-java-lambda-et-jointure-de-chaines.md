---
layout: post
title: "java, lambda et jointure de chaines"
date: "2020-11-12 14:26:00"
tags: java jointure chaines
---
```
@Test
public void testFoo() throws Exception {
    List<String> l = Arrays.asList("a", "b", "c");
    assertEquals("[a],[b],[c]", l.stream().map(v->String.format("[%s]", v)).collect(Collectors.joining(",")));
}
```

