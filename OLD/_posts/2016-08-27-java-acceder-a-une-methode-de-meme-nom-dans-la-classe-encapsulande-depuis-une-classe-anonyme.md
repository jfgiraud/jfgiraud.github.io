---
title: "java, accéder à une méthode de même nom dans la classe encapsulande depuis une classe anonyme"
date: 2016-08-27T06:18:00+01:00
tags: ["java", "compilation"]
---

Pour ce faire, il faut utiliser ParamTransform.this pour que la compilation n'échoue pas.

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

