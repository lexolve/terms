---
title: Sikkerhet
level: 2
anchored_in: 1-overordnede-vilkar
service: null
effective_from: 2026-11-11
---

# Sikkerhet

Dokumentet beskriver tiltakene Låvli bruker for å sikre tjenestene og opplysningene i dem.
Låvli velger og videreutvikler de tekniske løsningene selv, og kan endre dem så lenge sikkerhetsnivået holdes eller blir bedre.

## 1 Tilgang og innlogging {#access}

- Engangskoder for innlogging har kort gyldighet og kan bare brukes én gang.
- Gjentatte feilforsøk på innlogging blir begrenset.
- Økter er tidsbegrensede.
- Tilgang gis etter rolle og prinsippet om minste privilegium.
- Ansatte logger inn med flerfaktorautentisering eller single sign-on.

## 2 Kryptering {#encryption}

- Opplysningene er kryptert når de lagres.
- Trafikk krypteres med en sikker versjon av TLS.
- Databasen er ikke tilgjengelig fra internett.
- Nøkler håndteres i en egen nøkkelhåndteringstjeneste.
- Opplastede dokumenter har ikke offentlig tilgang.

## 3 Isolasjon mellom kunder og brukere {#isolation}

- Hver kunde er skilt fra andre kunder i datalaget.
- I Låvli Privat, Låvli Bedrift og Låvli Plattform er samtaler og opplastede dokumenter isolert mellom brukerne.
- I Lexolve OS kan brukerne i samme selskapskonto se hverandres dokumenter.

## 4 KI-modeller og eksterne kilder {#ai}

- KI-modellene kjøres hos leverandører i EU/EØS.
- Tekst fra åpne kilder kontrolleres for forsøk på å manipulere KI-modellene.
- I Låvli Privat, Låvli Bedrift og Låvli Plattform renses søk mot eksterne kilder for personopplysninger før de sendes.
- KI-funksjoner kan slås av umiddelbart.
- Hver samtale har grenser for lengde og ressursbruk.

## 5 Logging og overvåking {#logging}

- Driftslogger inneholder ikke meldingsinnhold.
- Tekniske spor av agentkjøringer kan inneholde spørsmål og svar, lagres i EU/EØS og slettes etter kort tid.
- Bare noen få navngitte driftsansatte har lesetilgang til loggene, og bare når det trengs.
- Tilgang til innhold registreres i en revisjonslogg.
- Tjenestene overvåkes.

## 6 Utvikling og drift {#operations}

- Kode gjennomgås, og det kjøres automatiske sikkerhetskontroller.
- Utvikling, test og produksjon er adskilte miljøer.
- Infrastrukturen styres som kode.
- Ansatte får opplæring og har signert konfidensialitetsavtaler.
- Sikkerheten vurderes uavhengig med jevne mellomrom.

## 7 Sikkerhetskopier og gjenoppretting {#backups}

- Sikkerhetskopier tas automatisk, i et begrenset antall generasjoner, og lagres i EU/EØS.
- Opplysningene kan gjenopprettes til et tidligere tidspunkt innenfor et fastsatt tidsrom.
- Produksjonsdata er beskyttet mot utilsiktet sletting.
- Tjenestene har redundans og automatisk failover.
- Tjenestene er beskyttet mot tjenestenektangrep gjennom Google Cloud.

## 8 Sikkerhetsbrudd {#incidents}

- Brudd håndteres etter rutiner som bygger på EDPBs retningslinjer 9/2022.
- Alle brudd dokumenteres internt.
