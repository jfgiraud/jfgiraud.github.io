---
title: "Java, convertir des wav en mp3"
date: "2017-09-27 16:49:00"
tags: java conversion wav mp3
---
Je maintiens une IHM d'administration dans laquelle un petit player flash permet d'écouter des fichiers wav.

Le passage au player html5 a été laborieux.

Le player devait s'afficher dans une popup (on utilisait auparavant qtip mais le passage à html5 faisait planter le rendu aléatoirement) et un problème d'affichage du temps total du morceau était présent de temps à autre (cf solution dans billet précédent).

Une fois la popup affichée et le problème de temps résolu, je me suis heurté à un autre problème de taille... 

En effet, IE11 (un des navigateurs à supporter) ne lit pas les fichiers wav !!!

J'ai donc cherché à convertir les fichiers wav en mp3.

La plupart des solutions sont à base de ffmepg encapsulé (comme JAVE) mais je n'ai pas réussi à les intégrer pour les faire fonctionner dans Tomcat.
Cela était certainement dû au Security Manager...

Puis par chance, j'ai trouvé un convertisseur 100% java : Jump3r

La bibliothèque est disponible sur le repository maven ([https://mvnrepository.com/artifact/de.sciss/jump3r/1.0.4](https://mvnrepository.com/artifact/de.sciss/jump3r/1.0.4)) et les sources sur [https://github.com/Sciss/jump3r](https://github.com/Sciss/jump3r)

L'utilisation est simple pour convertir un fichier wav en mp3. Voici ci-dessous un exemple :


```java
import de.sciss.jump3r.Main;

public void convertWavFileToMp3File(File source, File target) throws IOException {
    String[] mp3Args = { "--preset","standard",
        "-q","0",
        "-m","s",
        source.getAbsolutePath(),
        target.getAbsolutePath()
    };
    (new Main()).run(mp3Args);
}
```

Dans celui-ci, la fonction *main* a été *inlinée* pour permettre d'attraper/relancer une éventuelle *IOException*.

Jump3r m'a sauvé la vie : il a permis de modifier la servlet qui délivrait le wav pour lui faire délivrer un mp3 compatible avec tous les players HTML 5 des navigateurs.

Liens utiles :
- [http://textopia.org/androidsoundformats.html](http://textopia.org/androidsoundformats.html)
- [http://dinbror.dk/blog/how-to-preload-entire-html5-video-before-play-solved/](http://dinbror.dk/blog/how-to-preload-entire-html5-video-before-play-solved/)
