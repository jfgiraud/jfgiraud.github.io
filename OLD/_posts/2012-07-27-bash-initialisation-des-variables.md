---
title: "bash, initialisation des variables"
date: "2012-07-27 14:42:00"
tags: bash expansion parameter
---

**Use a default value**

```
${PARAMETER:-WORD}
${PARAMETER-WORD}
```

If the parameter PARAMETER is unset (never was defined) or null (empty), this one expands to WORD, otherwise it expands to the value of PARAMETER, as if it just was ${PARAMETER}. If you omit the : (colon), like shown in the second form, the default value is only used when the parameter was unset, not when it was empty. 


**Assign a default value**

```
${PARAMETER:=WORD}
${PARAMETER=WORD}
```

This one works like the using default values, but the default text you give is not only expanded, but also assigned to the parameter, if it was unset or null. Equivalent to using a default value, when you omit the : (colon), as shown in the second form, the default value will only be assigned when the parameter was unset. 


Pour résumer : 

- Le `:` indique que l'on remplace par l'expansion de WORD même si PARAMETER est vide (positionné mais vide)
- Le `=` à la différence de `:` indique qu'en plus PARAMETER sera affecté par l'expansion de WORD si celle-ci est utilisée. 

 
```
${PARAMETER:-WORD} renvoie WORD si PARAMETER est non défini ou vide
${PARAMETER-WORD} renvoie WORD si PARAMETER est non défini
${PARAMETER:=WORD} renvoie WORD si PARAMETER est non défini ou vide et assigne PARAMETER à WORD
${PARAMETER=WORD} renvoie WORD si PARAMETER est non défini et assigne PARAMETER à WORD
```
