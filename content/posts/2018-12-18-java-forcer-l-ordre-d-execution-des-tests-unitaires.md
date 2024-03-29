---
title: "java, forcer l'ordre d'exécution des tests unitaires"
date: 2018-12-18T11:59:00+01:00
tags: ["java", "test", "tu"]
---
Parfois, des tests unitaires plantent lorsqu'ils sont exécutés dans un certain ordre.

Aujourd'hui, c'est le cas et pour reproduire le problème, j'ai utilisé cette annotation qui permet de spécifier l'ordre que l'on souhaite utiliser lors de l'exécution de tous les tests de la classe.


```
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class TestMethodOrder {

    @Test
    public void testA() {
        System.out.println("first");
    }
    @Test
    public void testB() {
        System.out.println("second");
    }
    @Test
    public void testC() {
        System.out.println("third");
    }
}
```

Source : [https://github.com/junit-team/junit4/wiki/Test-execution-order](https://github.com/junit-team/junit4/wiki/Test-execution-order)
