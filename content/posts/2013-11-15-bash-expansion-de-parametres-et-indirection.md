---
title: "bash, expansion de paramètres et indirection "
date: 2013-11-15T09:40:00+01:00
---
Aujourd'hui, je viens de découvrir l'indirection de paramètres en bash.

La syntaxe est la suivante : ${!PARAMETER}

L'expansion ne donne pas la valeur du paramètre lui même mais la valeur du paramètre dont le nom est contenu dans PARAMETER.


```
$ TEMP="hello world"
$ TEXT=TEMP
$ echo ${!TEXT}
hello world
```

Cela permet de faire de jolies choses comme ceci en s'abstrayant d'eval...


```
XXX_user=rootX
XXX_password=rootX123
XXX_host=sqlserver01.example.com

YYY_user=rootY
YYY_password=rootY123
YYY_host=sqlserver02.example.com

ZZZ_user=rootZ
ZZZ_password=rootZ123
ZZZ_host=sqlserver03.example.com

connect_to() {
    local database="$1"
    user_key="${database}_user"
    password_key="${database}_password"
    host_key="${database}_host"
    mysql -h "${!host_key}" -u "${!user_key}" -p"${!password_key}" "$database"
}

connect_to ZZZ
```

Ci-dessous une documentation bien claire sur l'expansion des paramètres en bash

[http://wiki.bash-hackers.org/syntax/pe](http://wiki.bash-hackers.org/syntax/pe)


