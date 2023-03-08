---
title: "bash, génerer des mots de passe"
date: "2012-07-26 17:23:00"
---
Vous n'avez pas envie de réfléchir pour générer un mot de passe ?  Voici une petite méthode à mettre dans votre bashrc qui vous facilitera le choix ;)  <code><pre>
function genpass() {
    LENGTH=${1:-10}
    if [ "$2" == "0" ]; then
      CHAR="[:alnum:]"
    elif [ "$2" == "1" ]; then
      CHAR="[:graph:]"
    elif [ "${2:0:1}" != "+" ]; then
      echo "Erreur: vous devez spécifier les caractères acceptés"
      echo "Exemple: $ genpass 32 '+[:alnum:]_'"
      echo "2na2lku4FBqM7eNPC_aooahXV0c8GxI7"
      return
    else
      CHAR="${2:1}"
    fi
    cat /dev/urandom | tr -cd "$CHAR" | head -c $LENGTH
    echo
}

$ # génère un mot de passe de 10 caractères avec lettres et chiffres
$ genpass 10 0
toSGXjycaa
$ # génère un mot de passe de 10 caractères avec lettres, chiffres et symboles
$ genpass 10 1
^:5-LONhtn
$ # génère un mot de passe de 10 caractères avec ce que vous spécifiez après le +
$ genpass 10 "+abc[:digit:]"
b5836a29a2
</pre></code>
