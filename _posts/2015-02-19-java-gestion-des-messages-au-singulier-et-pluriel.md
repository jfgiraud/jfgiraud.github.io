---
layout: post
title: "java, gestion des messages au singulier et pluriel"
date: "2015-02-19 15:15:00"
---
Java propose depuis longtemps la possibilité de gérer les singuliers/pluriels via MessageFormat.

Vous trouverez ci-dessous un exemple au travers de tests unitaires.

Maintenant, fini les rustines dans le code pour les libellés !


```
import junit.framework.TestCase;

import java.text.MessageFormat;

public class FooTest extends TestCase {

    public void testPlural() {
        String formatPattern = "The directory {0} contains {1,choice,0#no file|1#one file|1<{1,number,integer} files}.";
        assertEquals("The directory XYZ contains no file.", MessageFormat.format(formatPattern, "XYZ", 0));
        assertEquals("The directory XYZ contains one file.", MessageFormat.format(formatPattern, "XYZ", 1));
        assertEquals("The directory XYZ contains 1 234 files.", MessageFormat.format(formatPattern, "XYZ", 1234));
    }
    
}
```

<div style="height: 0; overflow: hidden;">java, messageformat, singulier, pluriel
</div>
