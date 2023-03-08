---
title: "Java, convertir un fichier alaw en pcm"
date: "2017-11-24 15:09:00"
tags: java conversion wav
---
Dans un billet précédent, je parlais d'un petit player en html5 qui devait jouer des wav. Je convertissais les wav en mp3 pour la compatibilité des navigateurs.

Lors de l'intégration de celui-ci dans l'IHM d'administration du serveur vocal, j'ai eu quelques soucis de conversion...

La conversion en mp3 ne fonctionnait pas car les fichiers en entrée n'étaient pas des vrais "wav"... C'étaient des fichiers A-law ! 

```
ACCUEIL_CHOIX_TARIFS.wav:        RIFF (little-endian) data, WAVE audio, ITU G.711 A-law, mono 8000 Hz
```

Pour que la conversion en mp3 avec jump3r fonctionne, le format d'entrée doit être dans mon cas

```
RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
```

Avec sox, la conversion est simple :


```bash 
sox -t AL ATACMOB_Message_3.alaw -r 8000 -e signed-integer -b 16 ATACMOB_Message_3.wav
```

Mais c'est en java que cette conversion doit être faite car embarquée dans tomcat !

Le code suivant permet de convertir en java un fichier ITU G.711 A-law en Microsoft PCM


```java
protected boolean g711ToWav(File g711_wav, File pcm_wav) throws IOException, UnsupportedAudioFileException {
	AudioInputStream inputStream = AudioSystem.getAudioInputStream(g711_wav);
	try {
		AudioFormat format = inputStream.getFormat();
		AudioInputStream convertedInputStream;
		if ((format.getEncoding() == AudioFormat.Encoding.ULAW) || (format.getEncoding() == AudioFormat.Encoding.ALAW)) {
			AudioFormat tmp = new AudioFormat(
					AudioFormat.Encoding.PCM_SIGNED,
					format.getSampleRate(),
					format.getSampleSizeInBits() * 2,
					format.getChannels(),
					format.getFrameSize() * 2,
					format.getFrameRate(), true);
			convertedInputStream = AudioSystem.getAudioInputStream(tmp, inputStream);
			AudioSystem.write(convertedInputStream, AudioFileFormat.Type.WAVE, pcm_wav);
			return true;
		}
		return false;
	} finally {
		inputStream.close();
	}
}
```

Référence: 
- [https://stackoverflow.com/a/12862290/3550759](https://stackoverflow.com/a/12862290/3550759)
