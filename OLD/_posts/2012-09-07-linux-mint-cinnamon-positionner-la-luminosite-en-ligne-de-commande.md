---
title: "Linux Mint Cinnamon, positionner la luminosité en ligne de commande"
date: 2012-09-07T12:26:00+01:00
---
Il est possible d'utiliser les fichiers : 
- `/sys/class/backlight/acpi_video0/max_brightness`
- `/sys/class/backlight/acpi_video0/brightness` 
afin de modifier la luminosité.  Le script suivant prend un numérique (pourcentage entre 0 et 100) et modifie le fichier `/sys/class/backlight/acpi_video0/brightness` en conséquent.  

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int is_numeric(const char *p) {
  if (*p) {
    char c;
    while ((c=*p++)) {
      if (!isdigit(c)) return 0;
    }
    return 1;
  }
  return 0;
}

int
main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s <brightness>\n\nwhere brightness is an integer between 0 and 100\n", argv[0]);
    exit(1);
  }
  if (! is_numeric(argv[1])) {
    fprintf(stderr, "The given parameter '%s' is not an integer between 0 and 100.\n", argv[1]);
    exit(1);
  }
  int percent = atoi(argv[1]);
  if (percent < 0 || percent > 100) {
    fprintf(stderr, "The given parameter '%s' is not an integer between 0 and 100.\n", argv[1]);
    exit(1);
  }


  char *path = "/sys/class/backlight/acpi_video0/max_brightness";
  FILE *fp = fopen(path, "r");
  if (fp == NULL) {
    char buf[512];
    snprintf(buf, sizeof(buf), "The following error occurred while opening '%s'", path);
    perror (buf);
    exit(1);
  }
  char line[256];
  if (fgets(line, sizeof(line), fp) == NULL) {
    fprintf(stderr, "Can not read maximal brightness in file '%s'\n", path);
    exit(1);
  }
  int maxbrightness = atoi(line);
  fclose(fp);
  int newbrightness = maxbrightness * percent / 100;
  printf("Set brightness to %d/%d (%d%%)\n", newbrightness, maxbrightness, percent);
  path = "/sys/class/backlight/acpi_video0/brightness";
  fp = fopen(path, "w");
  if (fp == NULL) {
    char buf[512];
    snprintf(buf, sizeof(buf), "The following error occurred while opening '%s'", path);
    perror (buf);
    exit(1);
  }
  fprintf(fp, "%d\n", newbrightness);
  fclose(fp);
}
```   Toutefois, pour exécuter ce fichier, il faudra être root (sudo ou SUID bit positionné sur l'exécutable une fois compilé).   

Note: après rédaction de ce post, j'ai découvert que le paquet `xbacklight` met à disposition un utilitaire du même genre.  

```bash
$ xbacklight -set 0
```

Il permet la même chose sauf en mode console...
