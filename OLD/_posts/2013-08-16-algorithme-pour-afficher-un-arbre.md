---
title: "Algorithme pour afficher un arbre"
date: "2013-08-16 08:58:00"
---
Voici un algorithme pour afficher un joli arbre à la manière de la commande tree.


```
    private void print(Writer out, String prefix, List<Object> items) throws IOException {
        int j;
        for (j=items.size()-1; j>=0; j--) {
            Object o = items.get(j);
            if (! (o instanceof List))
                break;
        }
        for (int i=0; i<items.size(); i++) {
            Object o = items.get(i);
            boolean isTail = (i >= j) || (i == items.size() - 1);
            if (! (o instanceof List)) {
                out.write(prefix + (isTail ? "└── " : "├── ") + String.valueOf(o) + "\n");
            } else {
                print(out, prefix + (isTail ? "    " : "│   "), (List<Object>) o);
            }
        }
    }

    @Test
    public void testFoo() throws IOException {
        PrintWriter pw = new PrintWriter(System.out);
        print(pw, "", Arrays.asList("a", "b", Arrays.asList("c", "d", Arrays.asList("e", "g")), "h"));
        pw.flush();
        fail();
    }
```

Ce qui donne :


```
├── a
├── b
│   ├── c
│   └── d
│       ├── e
│       └── g
└── h
```
