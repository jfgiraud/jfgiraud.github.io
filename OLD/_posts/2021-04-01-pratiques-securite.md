---
title: "pratiques sécurité"
date: 2021-04-01T10:36:00+01:00
tags: ["sécurité"]
---

## Headers Http sur toutes les pages délivrées

```text
resp.addHeader("X-Frame-Options", "DENY");
resp.addHeader("X-XSS-Protection", "1; mode=block");
resp.addHeader("X-Content-Type-Options", "nosniff");
```
 
 
## Header Http positionné lors de la création d'un HttpSession

```text
response.setHeader("Set-Cookie", "JSESSIONID=" + session.getId() + "; Path=/; HttpOnly");
``` 
 
 
 
## Injection SQL
 
Ne pas créer les requêtes SQL par concaténation / formatage de chaîne (%s)
 
=> N'utiliser que des PreparedStatement (les paramètres sont échappés automatiquement)
 
 
 
 
## Sortie page HTML
 
Ne pas renvoyer de code HTML : si une donnée de la BDD contient un code JS injecté, il peut se retrouver exécuté lors de l'affichage
 
Remplacer les caractères < > & ' par leur entités html en sortie
 
 
 
## Entrée formulaire HTML
 
Vérifier les paramètres, formats... côté serveur (en plus du côté client)
 
Un Filtre (implements javax.servlet.Filter) peut être mis en place par exemple pour vérifier si les paramètres contiennent du code HTML, etc.
=> permet de centraliser les vérifications, mais peut-être complexe (exemple : post avec body en json contenant une valeur avec du code html)
Si stocké en BDD, le code peut-être joué (si pas échappé en sortie)
 
 
## Jeton Anti CSRF
 
Ajouter dans les formulaires du site A un jeton (champ caché) qui sera vérifié lors de la soumission.
Ca permet d'éviter qu'un site tiers B formate une url (incluse dans sa page) qui sera jouée par le navigateur de l'utilisateur sur le site A.
 
 
## Exceptions
 
Rattraper les exceptions et ne pas afficher la stack (pourrait indiquer une ip, nom de machine, chemin disque...)
 
Mettre dans la page HTML un UUID et dans le local7 l'UUID avec la pile d'exception.
 
Utiliser une page d'erreur spécifique (il me semble que de base, la page d'exception affiche la version tomcat)
 
 
## Côté système : 
 
Ne pas donner les versions Apache / Tomcat dans les headers de réponse.
