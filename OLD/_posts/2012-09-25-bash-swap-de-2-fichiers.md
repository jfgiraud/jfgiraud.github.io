---
title: "bash, swap de 2 fichiers"
date: 2012-09-25T13:50:00+01:00
tags: ["bash", "commande", "mv", "tempfile"]
---
Le code suivant à ajouter au bashrc permet de swapper ou plutôt échanger 2 fichiers rapidement.


```
function swap() { 
    if [[ -e "$1" && -e "$2" ]]      # if files exist
    then
	    local TMPFILE=$(tempfile)
	    mv "$1" $TMPFILE
	    mv "$2" "$1"
	    mv $TMPFILE "$2"
    else
	    echo "Error: Make sure the files exist."
    fi
}
```

Et son exemple :


```
$ echo x>x
$ echo y>y
$ swap x e
Error: Make sure the files exist.
$ swap x y
$ cat x
y
$ cat y
x
```


