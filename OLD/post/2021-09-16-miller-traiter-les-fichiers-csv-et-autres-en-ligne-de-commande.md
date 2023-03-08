---
layout: post
title: "miller, traiter les fichiers CSV (et autres) en ligne de commande"
date: "2021-09-16 10:07:00"
tags: csv commande miller
---

Hier, j'ai découvert le programme `mlr` ([https://github.com/johnkerl/miller](https://github.com/johnkerl/miller))

Il est installable par apt sous ubuntu.

Il permet d'effectuer des traitements sur les fichiers dont les données sont indexées par nom 

```name-indexed data such as CSV, TSV, and tabular JSON``` 

La documentation semble bien étoffée: [https://miller.readthedocs.io/en/latest/index.html](https://miller.readthedocs.io/en/latest/index.html)

```text
$ wget https://www.data.gouv.fr/fr/datasets/r/de7d0863-13e8-4010-9c75-487269f5d7ac -O depts.csv
...
depts.csv                                            100%[=====================================================================================================================>]   3,25K  --.-KB/s    ds 0,01s   
...

$ cat depts.csv | head -n 2
code_departement,nom_departement,code_region,nom_region
1,Ain,84,Auvergne-Rhône-Alpes

$ cat depts.csv | tail -n 2
974,La Réunion,4,La Réunion
976,Mayotte,6,Mayotte

$ mlr --icsv --from depts.csv --opprint cat|head
code_departement nom_departement         code_region nom_region
1                Ain                     84          Auvergne-Rhône-Alpes
2                Aisne                   32          Hauts-de-France
3                Allier                  84          Auvergne-Rhône-Alpes
4                Alpes-de-Haute-Provence 93          Provence-Alpes-Côte d'Azur
5                Hautes-Alpes            93          Provence-Alpes-Côte d'Azur
6                Alpes-Maritimes         93          Provence-Alpes-Côte d'Azur
7                Ardèche                 84          Auvergne-Rhône-Alpes
8                Ardennes                44          Grand Est
9                Ariège                  76          Occitanie

$ mlr --icsv --from depts.csv --opprint filter '$nom_departement =~ "^G"'
code_departement nom_departement code_region nom_region
30               Gard            76          Occitanie
32               Gers            76          Occitanie
33               Gironde         75          Nouvelle-Aquitaine
971              Guadeloupe      1           Guadeloupe
973              Guyane          3           Guyane
```

Exemple pour retrouver les communes de Dordogne qui ont un code postal girondin (et oui, cela existe !) : 

```text
$ mlr --icsv --from ~/Téléchargements/communes-departement-region.csv filter -S '$code_commune_INSEE=~"^24" && $code_postal=~"^33"'
code_commune_INSEE=24189,nom_commune_postal=FOUGUEYROLLES,code_postal=33220,libelle_acheminement=FOUGUEYROLLES,ligne_5=,latitude=44.8684209151,longitude=0.188754198495,code_commune=189,article=,nom_commune=Fougueyrolles,nom_commune_complet=Fougueyrolles,code_departement=24,nom_departement=Dordogne,code_region=75,nom_region=Nouvelle-Aquitaine
code_commune_INSEE=24335,nom_commune_postal=PORT STE FOY ET PONCHAPT,code_postal=33220,libelle_acheminement=PORT STE FOY ET PONCHAPT,ligne_5=,latitude=44.8622535573,longitude=0.208854675888,code_commune=335,article=,nom_commune=Port-Sainte-Foy-et-Ponchapt,nom_commune_complet=Port-Sainte-Foy-et-Ponchapt,code_departement=24,nom_departement=Dordogne,code_region=75,nom_region=Nouvelle-Aquitaine
```
