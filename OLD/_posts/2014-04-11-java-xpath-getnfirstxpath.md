---
title: "java & xpath : getNFirstXpath"
date: "2014-04-11 06:24:00"
---

```
private Object getNFirstXpath(HtmlPage page, String fmt, Object ... args) {
        String request;
        if (args.length == 0) {
            request = fmt;
        } else {
            request = String.format(fmt, args);
        }
        List inputs = page.getByXPath(request);
        if (inputs == null || inputs.size() == 0) {
            resultat = String.format("L'\u00e9lement '%s' n'a pas \u00e9t\u00e9 trouv\u00e9 dans la page", request);
            return null;
        }
        return inputs.get(0);
    }
```


```
HtmlCheckBoxInput o = (HtmlCheckBoxInput) getNFirstXpath(page, String.format("//input[@type='checkbox'][@id='id_%s_activation']", champ, valeur));

HtmlTextInput o = (HtmlTextInput) getNFirstXpath(page, String.format("//input[@name='%s']", champ));

HtmlOption o = (HtmlOption) getNFirstXpath(page, String.format("//select[@name='%s']//option[text()='%s']", champ, valeur));

HtmlOption o = (HtmlOption) getNFirstXpath(page, String.format("//select[@name='%s']//option[text()='%s'][@selected='']", champ, valeur));

List<HtmlTableRow> trs = (List<HtmlTableRow>) page.getByXPath("//table[@class='rules']/tbody/tr[starts-with(@id,'rule_')]");

String valeur = ((HtmlAnchor) getNFirstXpath(page, String.format("//tr[starts-with(@id, 'rule_')]/td[@name='ID'][text()='%s']/preceding-sibling::td/a[@class='on' or @class='off']", numero))).getAttribute("class");

HtmlTableCell td = (HtmlTableCell) getNFirstXpath(page, "//tr[starts-with(@id,'rule_')]/td[@name='ID'][text()=%d]", numero);

List<HtmlTableRow> trs = (List<HtmlTableRow>) page.getByXPath("//table[@class='rules']/tbody/tr");

Object o = getNFirstXpath(page, "//span[@class='section'][contains(text(),'Vous \u00e9ditez une nouvelle r\u00e8gle')]");

Object o = getNFirstXpath(page, "//span[@class='section'][contains(text(),'Vous \u00e9ditez la r\u00e8gle %s')]", numero);

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//a[@class='button'][span='Cr\u00e9er une nouvelle r\u00e8gle']");

xpath = "//*[@id='formulaire']/div[1]/label[@title='%s']";
xpath = "//td[text()='%s']";

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//a[@class='button'][span='Cr\u00e9er une nouvelle r\u00e8gle']");

HtmlSubmitInput button = (HtmlSubmitInput) getNFirstXpath(page, "//input[@type='submit'][@value='%s']", nom);

HtmlHiddenInput actionButton = (HtmlHiddenInput) getNFirstXpath(page, "//input[@type='hidden'][@id='action']");

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//table[@class='rules']/tbody/tr/td[@name='ID'][text()='%d']/../td[@name='COMMANDES']/a[@class='edition']", numero);

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//table[@class='rules']/tbody/tr/td[@name='ID'][text()='%d']/../td[@name='COMMANDES']/a[@class='off']", numero);

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//table[@class='rules']/tbody/tr/td[@name='ID'][text()='%d']/../td[@name='COMMANDES']/a[@class='on']", numero);

HtmlElement href = (HtmlAnchor) getNFirstXpath(page, "//td[@name='NOM_REGLE'][text()='%s']/preceding-sibling::td/a[@class='delete']", nomRegle);

HtmlElement href = (HtmlElement) getNFirstXpath(page, "//tr[starts-with(@id, 'rule_')][%s]/td[@name='ID'][text()=%d]", position, numero);

HtmlAnchor href = (HtmlAnchor) getNFirstXpath(page, "//a[@href='/logout']");

HtmlTextInput username = (HtmlTextInput) getNFirstXpath(page, "//input[@id='username']");

HtmlPasswordInput password = (HtmlPasswordInput) getNFirstXpath(page, "//input[@id='password']");

HtmlButton button = (HtmlButton) getNFirstXpath(page, "//button[@type='submit']");
```
