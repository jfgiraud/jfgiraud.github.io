---
layout: post
title: "mysql, données binaires"
date: "2020-11-12 15:47:00"
tags: hexa binary binaire mysql
---
Dans certains cas, la commande `LOAD_FILE` n'est pas utilisable (problèmes de droits, etc..) pour alimenter 
un blob.

Dans ce cas, il peut être intéressant de convertir un fichier binaire (ici un fichier texte) en séquence 
hexadécimale...

```text
$ cat lorem.txt 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at lorem pharetra, pulvinar quam nec, efficitur ligula. Donec imperdiet aliquam rutrum. Aenean metus est, cursus eget auctor sit amet, vehicula id lorem. Vivamus mollis sollicitudin mattis. Aenean volutpat velit tellus, et ullamcorper nisi aliquam ut. Nunc efficitur est ac tincidunt ultrices. Morbi ac quam magna. Vivamus egestas elit in bibendum fermentum. Nulla nunc felis, aliquet a lorem eleifend, mollis laoreet libero. Etiam sit amet justo bibendum, cursus lectus in, blandit ex. Nulla dolor est, pharetra eget nulla et, sodales dapibus diam.

Fusce et mauris quis sem tincidunt eleifend. In felis ipsum, vehicula sit amet sapien a, vulputate euismod lacus. Proin condimentum ante ex, et viverra eros tristique eu. Quisque consectetur, lectus ut tempus aliquet, lorem urna venenatis dolor, id venenatis ante tortor quis odio. Fusce consectetur nisi id massa efficitur, et condimentum enim sagittis. Donec volutpat leo in nisl vestibulum tempor. Aliquam erat volutpat. Praesent egestas lectus nibh, vel porta lorem pharetra a. Pellentesque nec bibendum metus. Nulla a felis hendrerit, pulvinar est ac, ullamcorper ipsum. Donec tempus porta lectus a laoreet. Aenean eget tortor at mi aliquet sodales.
```

et utiliser cette séquence hexadécimale pour faire sa requête mysql.

On utilisera alors la commande UNHEX pour décoder la séquence hexadécimale et la remettre en binaire dans la requête SQL.

```text
$ xxd -p lorem.txt | tr -d '\n' | xargs printf 'select unhex("%s");' | mysql -u root -ptest -s 2> /dev/null | xargs -0 printf $'%b'
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer at lorem pharetra, pulvinar quam nec, efficitur ligula. Donec imperdiet aliquam rutrum. Aenean metus est, cursus eget auctor sit amet, vehicula id lorem. Vivamus mollis sollicitudin mattis. Aenean volutpat velit tellus, et ullamcorper nisi aliquam ut. Nunc efficitur est ac tincidunt ultrices. Morbi ac quam magna. Vivamus egestas elit in bibendum fermentum. Nulla nunc felis, aliquet a lorem eleifend, mollis laoreet libero. Etiam sit amet justo bibendum, cursus lectus in, blandit ex. Nulla dolor est, pharetra eget nulla et, sodales dapibus diam.

Fusce et mauris quis sem tincidunt eleifend. In felis ipsum, vehicula sit amet sapien a, vulputate euismod lacus. Proin condimentum ante ex, et viverra eros tristique eu. Quisque consectetur, lectus ut tempus aliquet, lorem urna venenatis dolor, id venenatis ante tortor quis odio. Fusce consectetur nisi id massa efficitur, et condimentum enim sagittis. Donec volutpat leo in nisl vestibulum tempor. Aliquam erat volutpat. Praesent egestas lectus nibh, vel porta lorem pharetra a. Pellentesque nec bibendum metus. Nulla a felis hendrerit, pulvinar est ac, ullamcorper ipsum. Donec tempus porta lectus a laoreet. Aenean eget tortor at mi aliquet sodales.
```

Le `xxd -p` permet de ne sortir que l'hexa sur la sortie standard tandis que le `tr -d '\n'` concatène les lignes.
