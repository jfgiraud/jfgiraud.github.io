---
layout: post
title: "bash, génerer des mots de passe"
date: "2012-07-26 17:23:00"
---
Vous n'avez pas envie de réfléchir pour générer un mot de passe ?  Voici une petite méthode à mettre dans votre bashrc qui vous facilitera le choix ;)  <code><pre><br />function genpass() {<br />    LENGTH=${1:-10}<br />    if [ "$2" == "0" ]; then<br />      CHAR="[:alnum:]"<br />    elif [ "$2" == "1" ]; then<br />      CHAR="[:graph:]"<br />    elif [ "${2:0:1}" != "+" ]; then<br />      echo "Erreur: vous devez spécifier les caractères acceptés"<br />      echo "Exemple: $ genpass 32 '+[:alnum:]_'"<br />      echo "2na2lku4FBqM7eNPC_aooahXV0c8GxI7"<br />      return<br />    else<br />      CHAR="${2:1}"<br />    fi<br />    cat /dev/urandom | tr -cd "$CHAR" | head -c $LENGTH<br />    echo<br />}<br /><br />$ # génère un mot de passe de 10 caractères avec lettres et chiffres<br />$ genpass 10 0<br />toSGXjycaa<br />$ # génère un mot de passe de 10 caractères avec lettres, chiffres et symboles<br />$ genpass 10 1<br />^:5-LONhtn<br />$ # génère un mot de passe de 10 caractères avec ce que vous spécifiez après le +<br />$ genpass 10 "+abc[:digit:]"<br />b5836a29a2<br /></pre></code>
