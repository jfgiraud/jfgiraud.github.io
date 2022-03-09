---
layout: post
title: "java, accéder à une méthode de même nom dans la classe encapsulande depuis une classe anonyme"
date: "2016-08-27 06:18:00"
tags: java compilation
---

```java
public abstract class ParamTransform<Init,In,Out> implements Transform<Init,Transform<In,Out>> {

    public abstract Out apply(Init values, In value);

    public final Transform<In, Out> apply(final Init values) {
        return  new Transform<In, Out>() {
            public Out apply(In value) {
                return ParamTransform.this.apply(values, value);
            }
        };
    }

}
```

Pour ce faire, il faut utiliser ParamTransform.this pour que la compilation n'échoue pas.
