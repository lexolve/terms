---
description: Kontroller lovkrav og konsistens i dokumentene, og vurder om endringene krever varsel
argument-hint: "[commit å sammenligne med, valgfritt]"
---

# Kryssjekk av dokumentene

Du skal kontrollere at dokumentene oppfyller lovkravene, at de stemmer med hverandre og med `data/`, og om endringene krever varsel.
Kjør kryssjekken før en endring publiseres.
Du skal ikke endre noen dokumenter, datafiler eller skript.
Rapporten legges i mappen `verification/`, som ikke er med i git.

Les `AGENTS.md` før du begynner.
Dokumentene ligger i `src/`.

## Regler

- Skriv på norsk bokmål.
- Vis alltid til nøyaktig sted, for eksempel `2-databehandleravtale.md#subprocessors` eller raden `forskning` i `data/processing.yaml`.
- Gjett ikke. Er du usikker, merk det som et spørsmål.
- Ta utgangspunkt i at faktaene om tjenestene er riktige: leverandører, lokasjoner, lagringstider og sikkerhetstiltak. Spør bare hvis to steder sier ulike ting.
- Ikke foreslå nye bestemmelser bare fordi mange vilkår har dem. Se «Ikke reguler i tilfelle» i `AGENTS.md`.
- Lexolve OS skal fases ut. Funn som bare gjelder Lexolve OS, er mindre funn, med mindre et lovkrav mangler eller dokumentene motsier hverandre.

## Steg

### 1. Kjør kontrollen

Kjør `python scripts/gendoc.py check` og noter resultatet.
Kontrollen skal gi 0 feil. List opp merknadene om TODO.

### 2. Konsistens

Kontroller og rapporter:

- Alle frister og tall i alle dokumentene, i én tabell, med sted. Finn tall som er ulike for det samme.
- At lagringstider, roller og mottakere i teksten stemmer med `data/`.
- At samme forhold ikke er beskrevet ulikt i to dokumenter.
- At begreper fra `data/glossary.yaml` brukes med samme betydning overalt.
- At henvisninger peker på et punkt som faktisk handler om det henvisningen sier.

### 3. Lovkrav

Lag en sjekkliste for hvert av disse kravene, med sted i dokumentene, eller «mangler»:

- GDPR art. 28 nr. 3 i `2-databehandleravtale.md`: gjenstand, varighet, art, formål, typer opplysninger, kategorier av registrerte, og bokstav a til h.
- GDPR art. 13 nr. 1 og 2 i hvert personverndokument, og art. 14 for personer som omtales i innholdet.
- Opplysninger om angrerett og klageadgang i `2-vilkar-privat.md`. Angreretten står i punktet om oppsigelse, angrerett og sletting, med angreskjemaet.
- Opplysninger om tjenesteyteren etter ehandelsloven § 8 i `1-overordnede-vilkar.md`.

### 4. Varsel

Finn endringene som skal vurderes:

- Hvis du har fått en commit som argument, er det endringene fra den: `git diff $ARGUMENTS -- src data`.
- Ellers er det endringene som ikke er publisert: `git diff origin/main -- src data`, også endringer som ikke er committet.

Vurder hver endring etter «Endringer som utløser varsel» i `AGENTS.md`.
Oppgi for hver endring som krever varsel: hva som er endret, hvem som skal varsles, fristen, og om `effective_from` må endres.
Vær pragmatisk, slik AGENTS.md sier.

### 5. Rapport

Lag `verification/rapport.md` med:

- Resultatet av kontrollen fra steg 1.
- Funn sortert etter alvorlighet:
  - **Kritisk:** lovkrav som mangler, eller motstrid mellom dokumentene.
  - **Viktig:** uklarheter som kan gi tvist eller feil forståelse av rettigheter og plikter.
  - **Mindre:** språk, konsistens og formatering.
- Hvert funn med sted og et konkret forslag til løsning.
- Vurderingen av varsel fra steg 4.
- En liste over spørsmål som bare et menneske kan avgjøre.

Flytt en eldre rapport til `verification/archive/` med dagens dato før du skriver den nye.

## Ferdig når

- Sjekklistene for lovkrav er fylt ut.
- Endringene er vurdert for varsel.
- Rapporten er skrevet.
- Ingen filer utenfor `verification/` er endret. Kontroller det med `git status`.
