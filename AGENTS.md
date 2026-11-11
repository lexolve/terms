# AGENTS.md

Instrukser for KI-agenter og andre som endrer dokumentene i dette repoet.

## Hva repoet inneholder

Vilkår og personverninformasjon for tjenestene til Låvli AS: Låvli Privat, Låvli Bedrift, Lexolve OS og Låvli Plattform.
Repoet er eneste kilde.
Publiserte versjoner lages fra git-tagger.

## Struktur

Dokumentene ligger i `src/`. Filnavnet begynner med nivået.

| Nivå | Filer | Innhold |
| --- | --- | --- |
| 0 | `0-kundeavtale.md` | Mal for kundeavtale. Signeres per virksomhet og omfatter dokumentpakken. Brukes bare for Låvli Plattform |
| 1 | `1-overordnede-vilkar.md` | Gjelder alle tjenester og kunder |
| 2 | `2-sikkerhet.md` | Sikkerhetstiltak for alle tjenester |
| 2 | `2-vilkar-privat.md` | Vilkår for Låvli Privat |
| 2 | `2-generelle-vilkar-virksomheter.md`, `2-databehandleravtale.md` | Gjelder virksomhetstjenestene |
| 3 | `3-spesielle-vilkar-<tjeneste>.md` | Ett dokument per virksomhetstjeneste: `bedrift`, `lexolve-os` og `plattform` |
| 4 | `4-personvern-<tjeneste>.md` | Informasjon om behandling av personopplysninger. For virksomhetstjenestene også beskrivelsen av behandlingen etter databehandleravtalen |
| – | `data/` | `glossary.yaml`, `processing.yaml` og `recipients.yaml`. Eneste kilde for innholdet i tabellene |

Tjenestene heter `privat`, `bedrift`, `lexolve-os` og `plattform` i filnavn.

### Forankring

- Kundeavtalen omfatter dokumentpakken for tjenesten, i gjeldende versjon.
- For Privat, Bedrift og Lexolve OS inngås avtalen ved aksept i tjenesten. Aksepten lenker til dokumentene på web.
- Vilkårene for Låvli Privat hjemles i de overordnede vilkårene.
- Sikkerhetsbeskrivelsen hjemles i de overordnede vilkårene.
- De generelle vilkårene for virksomheter hjemles i de overordnede vilkårene.
- De spesielle vilkårene for Bedrift, Lexolve OS og Plattform hjemles i de generelle vilkårene for virksomheter.
- Databehandleravtalen hjemles i de generelle vilkårene for virksomheter.
- Personvern for Privat forankres i vilkårene for Låvli Privat.
- Personvern for Bedrift, Lexolve OS og Plattform forankres i databehandleravtalen.

Privat-siden og virksomhetssiden skal ikke henvise til hverandre.
Begge sider kan henvise til sikkerhetsbeskrivelsen.

### Kundens egen databehandleravtale

En virksomhet kan bruke sin egen databehandleravtale hvis Låvli godtar den.
Dokumentene skal ikke nevne denne muligheten. Strukturen skal bare gjøre det mulig.
Da legges personverndokumentet for tjenesten og sikkerhetsbeskrivelsen ved kundens avtale.
Derfor skal disse dokumentene kunne stå alene:

- Sikkerhetsbeskrivelsen skal ikke henvise til andre dokumenter i teksten. Hjemmelen står bare i metadata.
- Personverndokumentene for virksomhetstjenestene kan henvise til sikkerhetsbeskrivelsen. Brukes personverndokumentet med kundens avtale, følger sikkerhetsbeskrivelsen med.
- Personverndokumentene skal selv inneholde formål, opplysningstyper, registrerte, mottakere, lagringssted, lagringstid og sletting.
- Tabeller fra `data/` regnes ikke som henvisninger. De står utfylt i dokumentet.

### Rangordning

Dokumentene har ingen rangordning. Alminnelige tolkningsregler gjelder.
Et avvik i en kundeavtale viser til punktet i standarddokumentet det erstatter eller utfyller, og begynner med «I stedet for [punkt om …](…) gjelder: …» eller «I tillegg til [punkt om …](…) gjelder: …». Avvik uten et punkt å vise til begynner med «I tillegg gjelder: …».
Skriv ikke inn rangordning noe sted.

## Skriveregler

- Bruk denne tiltaleformen:

| Dokument | Om kunden eller brukeren | Om Låvli |
| --- | --- | --- |
| Overordnede vilkår | «du» om personen som bruker tjenesten | «Låvli» |
| Kundeavtale, generelle vilkår for virksomheter, databehandleravtale og spesielle vilkår for virksomhetstjenestene | «virksomheten» | «Låvli» |
| Vilkår og personvern for Privat | «du» | «vi» |
| Personvern for virksomhetstjenestene | «du» om den registrerte, «virksomheten» om virksomheten som bruker tjenesten | «Låvli» |

- Nevn rollene etter personvernregelverket én gang, for eksempel «Virksomheten er behandlingsansvarlig, og Låvli er databehandler». Bruk deretter navnene.
- Plikter skrives med «skal».
- Unntak: faste løfter om hvordan Låvli behandler opplysninger kan skrives i presens, for eksempel «Låvli selger ikke personopplysninger».
- Rettigheter og valg skrives med «kan».
- Bruk ikke «sørger for», «påser», «må» eller «bør» om plikter. «Bør» brukes bare om anbefalinger.
- Bruk ikke definerte termer med stor forbokstav. Bruk vanlige ord konsekvent, med liten forbokstav.
- Definerte begreper står i `data/glossary.yaml`. Legg til nye begreper bare hvis ordet ellers er uklart. Se avsnittet om definerte begreper.
- Bruk ikke advokatfraser som «herunder», «inkludert, men ikke begrenset til», «forbeholder seg retten til», «for så vidt gjelder» og «i den utstrekning».
- Bruk ikke store bokstaver eller fet skrift for å understreke.
- Skriv korte setninger. Ett punkt bør ha én regel.
- Unngå mange setninger som begynner med verbet i betingelsesform, som «Har du gitt samtykke, kan du …». Skriv heller med «hvis» eller begynn med subjektet.
- Teksten bør være i aktiv form og henvende seg til leseren, for eksempel «For henvendelser om personvern kan du bruke …» i stedet for «Henvendelser om personvern sendes til …».
- Bruk lovhenvisninger bare der de gir leseren en rettighet, eller der loven krever det.
- Skriv bokmål med anførselstegn « ».
- Skriv ikke at Låvli pålegger underleverandører plikter. Skriv at Låvli kontrollerer at underleverandørene ved avtale er bundet av plikter som er minst like strenge.
- Angreretten i vilkårene for Låvli Privat står i punktet om oppsigelse, angrerett og sletting, fordi brukeren uansett kan slette kontoen når som helst. Tabellen der er angreskjemaet, tilpasset en digital tjeneste: e-postadressen kontoen er registrert med, i stedet for adresse, og ingen underskrift. Endre ikke feltene uten beslutning.

Henvis til personverndokumentene med tittelen og stor forbokstav, for eksempel «Personvern for Låvli Privat», så det er tydelig at det er et dokument.
Generelle henvisninger som «personverndokumentet for tjenesten» har liten forbokstav.

Bruk disse betegnelsene:

| Bruk | Ikke |
| --- | --- |
| overordnede vilkår | fellesvilkår, Del A |
| generelle vilkår for virksomheter | næringsvilkår |
| spesielle vilkår | særvilkår, særlige vilkår |
| databehandleravtale | DPA i dokumentteksten |
| personvern | personvernerklæring |
| GDPR | personvernforordningen |
| virksomheten | kunden, kundens firmanavn, Behandlingsansvarlig |
| Låvli | Leverandøren, Databehandler, Låvli AS (utenom partsangivelsen) |

## Formatering

- Skriv én setning per linje.
- Gi hver overskrift et kort, fast anker på engelsk: `## Forskning {#research}`. Samme tema har samme anker i alle dokumentene, for eksempel `#changes`, `#liability` og `#termination`.
- Hovedpunktene (`##`) nummereres av skriptet. Skriv ikke nummeret selv.
- Henvis til et punkt med lenketeksten «punkt om …» og ankeret. Skriptet setter inn nummeret: `[punkt om ansvar](2-generelle-vilkar-virksomheter.md#liability)` blir `[punkt 9 om ansvar](…)`.
- Står punktet i et annet dokument, skriv dokumentnavnet etter lenken: «… i Generelle vilkår for virksomheter».
- Henvis til et helt dokument med tittelen som lenketekst i lister og tabeller.
  I løpende tekst kan du bruke den naturlige formen med liten forbokstav, for eksempel «databehandleravtalen» eller «sikkerhetsbeskrivelsen». Personverndokumentene har alltid tittelen, se skrivereglene.
- Bruk tabeller når flere frister eller tall står sammen. En enkelt frist står i punktet den hører til.
- Hvert dokument skal begynne med metadata. `effective_from` er datoen den gjeldende versjonen trådte i kraft, se [Endringer som utløser varsel](#endringer-som-utløser-varsel). Versjonen ellers går fram av git-historikken.

```yaml
---
title: Vilkår for Låvli Privat
level: 2
anchored_in: 1-overordnede-vilkar
service: privat
effective_from: 2026-11-11
---
```

## Definerte begreper

Merk et definert begrep med klassen `term`:

```markdown
Vi tar [forskningsuttrekk]{.term} fra et utvalg samtaler.
```

Står ordet i en annen form enn i ordlisten, skal grunnformen oppgis som nøkkel:

```markdown
[forskningsuttrekkene]{.term key=forskningsuttrekk}
```

- Merk begrepet første gang det brukes i hvert hovedpunkt, ikke hver gang.
- Lenk ikke til ordlisten i teksten. Byggingen slår opp definisjonen og lager lenke og hjelpetekst.
- Vanlige forkortelser som KI, EØS, GDPR og SSO defineres ikke og merkes ikke.

Hvert begrep i `data/glossary.yaml` har grunnform, definisjon og ord som ikke skal brukes:

```yaml
- term: forskningsuttrekk
  definition: Pseudonymiserte utdrag av spørsmål og svar som tas ut til forskningsprosjektet.
  avoid: [uttrekk, forskningsutdrag]
```

Ordlisten står som generert tabell i `1-overordnede-vilkar.md`, se avsnittet om tabeller fra data.

## Faste maler

Kundeavtalen har disse punktene: Parter og kontaktpersoner, Leveranse, Bestilling, Avtaleperiode, Avtaledokumenter, Avvik fra standardvilkårene, Signaturer.
Felt som fylles ut for hver kunde, følger malformatet i legal-knowledge (`docs/PIPELINE.md`, avsnittet «Tenant templates»):

- Feltene deklareres under `fields` i metadata, med `name`, `label`, `question`, `type`, `required` og eventuelt `default`. Eksempelverdier står som `default`.
- I teksten brukes `{{feltnavn}}`, `{{#if …}}` og `{{#each …}}…{{else}}…{{/each}}`. Et tomt felt vises som `[LABEL]`.
- Hvert felt som brukes, skal være deklarert, og hvert felt som er deklarert, skal brukes. `python scripts/gendoc.py check` kontrollerer det.
- Kundeavtalen bruker ikke markdown-tabeller, fordi malformatet ikke tillater dem. Overskriftene nummereres av skriptet, som i de andre dokumentene.

De spesielle vilkårene har alltid disse fem punktene: Tjenesten, Avtale, pris og betaling, Personopplysninger, Ansvar, Oppsigelse og sletting.
Skriv «Ingen tillegg» der tjenesten ikke har noe tillegg.

Personverndokumentene for virksomhetstjenestene har disse punktene: Om dokumentet, Hvem er behandlingsansvarlig?, Hva behandles for virksomheten?, Hva behandler Låvli selv?, Hvem får opplysningene?, Dine rettigheter, Kontakt og klage.
Tillegg for en tjeneste settes inn rett etter tabellen de hører til.

## Tabeller fra data

Innholdet i tabellene har én kilde: filene i `data/`.
Dokumentene inneholder likevel tabellene utfylt, slik at hver fil er komplett og kan brukes som den er.

En generert tabell står mellom to merkelapper som sier hvilken fil og hvilket utvalg den kommer fra:

```markdown
<!-- data: recipients.yaml services=bedrift -->
| Mottaker | Oppgave | Rolle | Lokasjon |
| --- | --- | --- | --- |
| … | … | … | … |
<!-- /data -->
```

- Endre aldri en generert tabell for hånd.
- Endre filen i `data/`, og kjør `python scripts/gendoc.py update`. Skriptet oppdaterer tabellene, punktnumrene og numrene i henvisningene i alle dokumentene.
- Lever endringen i datafilen og i dokumentene i samme pull request.

### Nøkler i YAML

Nøklene i YAML, både i `data/` og i metadata øverst i dokumentene, skrives på engelsk.
Faste verdier som `controller`, `role` og `part` er også engelske.
Tekst som vises i dokumentene, skrives på norsk.

| Fil | Nøkler |
| --- | --- |
| `processing.yaml` | `id`, `personal_data`, `data_subjects`, `purpose`, `services`, `controller` (`lavli` eller `business`), `legal_basis`, `retention` (hvor lenge opplysningene lagres), `deletion` (hvordan og når de slettes) |
| `recipients.yaml` | `name`, `task`, `role` (`processor`, `independent_controller` eller `unresolved`), `part` (`business`, `lavli` eller `both`), `personal_data`, `location`, `transfer_basis`, `services` |
| `glossary.yaml` | `term`, `definition`, `avoid`, `abbreviation` |

Felt som er ulike mellom tjenestene, kan ha én verdi per tjeneste, med tjenestens navn som nøkkel.
`legal_basis` fylles bare ut når `controller` er `lavli`.

## Ikke dupliser

- Hver regel skal stå ett sted. Andre steder står en kort henvisning.
- Behandlinger med rolle, rettslig grunnlag og lagringstid, mottakere og ordlisten står i `data/`. Tabellene i dokumentene lages fra disse filene, se avsnittet om tabeller fra data.
- Fristene etter databehandleravtalen står bare i databehandleravtalen. Andre dokumenter viser til punktet der fristen står.
- Kopier ikke tekst mellom tjenestedokumentene. Er noe likt for alle tjenester på et nivå, hører det hjemme på nivået over.
- Unntak: garantiene i punktet om forskning står både i `4-personvern-privat.md` og `4-personvern-bedrift.md`. Endres det ene, skal det andre endres likt.
- Unntak: KI-forbeholdet står både i `1-overordnede-vilkar.md#ai` og i `2-vilkar-privat.md#eligibility`. Endres det ene, skal det andre endres likt.
- Unntak: at innholdet i Låvli Plattform ikke brukes til forskning med mindre kundeavtalen sier noe annet, står både i `3-spesielle-vilkar-plattform.md#privacy` og i `4-personvern-plattform.md#own-processing`, av pedagogiske hensyn. Endres det ene, skal det andre endres likt.

Overfor forbrukere i Låvli Privat kan informasjon som er viktig for å forstå tjenesten, gjentas i vilkårene for Privat, selv om regelen står i de overordnede vilkårene. Hensynet er pedagogisk: forbrukeren skal møte de viktigste forbeholdene der de leser. Gjentakelsen skal være kort, og regelen gjelder fortsatt der den står i de overordnede vilkårene.

## Ikke reguler i tilfelle

- Legg ikke inn bestemmelser for hendelser som ingen har vurdert som sannsynlige.
- Gjenta ikke det som følger av loven.

Dette skal likevel alltid være med:

- Databehandleravtalen skal inneholde alt som kreves etter GDPR art. 28 nr. 3.
- Personvern skal inneholde informasjonen som kreves etter GDPR art. 13 og 14.
- Vilkårene for Låvli Privat skal informere om angrerett og klageadgang.

## Endringer som utløser varsel

`effective_from` endres bare når en endring krever varsel.
Andre endringer gjelder fra de er publisert, og historikken på GitHub viser hva som er endret.

Vurder ved hver endring i `src/` eller `data/` om den krever varsel, og skriv vurderingen kort i beskrivelsen av pull requesten.
Vær pragmatisk. Varsel er for endringer brukeren eller virksomheten har grunn til å bry seg om, ikke for enhver justering.
En god test er om endringen betyr noe i praksis: Får brukeren eller virksomheten andre rettigheter, plikter, priser eller risiko, eller behandles opplysningene på en ny måte?

Disse endringene krever ikke varsel:

- Språk, struktur, rekkefølge, overskrifter, lenker og skrivefeil.
- Presiseringer som ikke endrer rettigheter eller plikter, for eksempel at teksten bringes i samsvar med tabellene eller med det som allerede gjelder.
- Endringer som bare er til gunst for brukeren eller virksomheten, for eksempel en ny garanti eller en lengre frist for kunden.
- Faktaopplysninger som ikke endrer behandlingen, for eksempel nytt firmanavn eller ny adresse hos en leverandør.

Disse endringene krever varsel etter dokumentene selv:

| Endring | Varsel | Står i |
| --- | --- | --- |
| Ny eller byttet underleverandør som behandler opplysninger for virksomheten («Behandling for virksomheten» eller «Begge» i `data/recipients.yaml`) | 45 dager på e-post til virksomhetens kontaktperson | `2-databehandleravtale.md#subprocessors` |
| Endring i databehandleravtalen | 30 dager, med rett til å si opp avtalen | `2-databehandleravtale.md#changes` |
| Vesentlig endring i personverndokumentene for virksomhetstjenestene eller i sikkerhetsbeskrivelsen, for eksempel nye formål, nye typer opplysninger, lengre lagringstid, overføring ut av EU/EØS eller svakere sikkerhetstiltak | Beskjed på e-post | `2-databehandleravtale.md#changes` |
| Endring i vilkårene for virksomheter som er vesentlig til ugunst for virksomheten, for eksempel pris, ansvar, oppsigelse eller hva tjenesten omfatter | 30 dager på e-post, med rett til å si opp avtalen | `2-generelle-vilkar-virksomheter.md#changes` |
| Vesentlig endring i vilkårene for Låvli Privat eller i Personvern for Låvli Privat | 30 dager på e-post. Nye vilkår gjelder først når brukeren har godtatt dem | `2-vilkar-privat.md#changes` |
| Endring som gjør Låvli Privat mer enn ubetydelig dårligere for brukeren | Varsel i god tid, med rett til å si opp uten kostnad innen 30 dager | `2-vilkar-privat.md#changes` |

Endringer i de overordnede vilkårene følger reglene for tjenesten de treffer.

Noen endringer krever mer enn varsel:

- Forbudet mot å bruke innholdet til egne formål, taushetsplikten og garantiene i punktet om forskning kan ikke endres til ugunst for virksomheten uten at den samtykker. Se `2-databehandleravtale.md#changes`.
- Endringer i garantiene om forskning i Privat gjelder bare forskningsuttrekk som tas etter endringen.
- Et nytt formål med behandlingen må stå i personverndokumentet før behandlingen begynner (GDPR art. 13 nr. 3).

Når en endring krever varsel:

- Foreslå en dato for `effective_from` i de endrede dokumentene. Datoen må gi hele varslingsfristen regnet fra dagen varselet sendes. Et menneske bestemmer datoen.
- Samle endringer som kommer samtidig, i ett varsel med én dato.
- Er du i tvil, skriv vurderingen og spør i stedet for å velge den strengeste løsningen.

## Commit-meldinger

Skriv commit-meldinger på engelsk, med en kort oppsummering i imperativ på første linje, for eksempel «Add notice rules for changes».
Dokumentene og beskrivelsen av pull requesten skrives fortsatt på norsk.

## Dette skal agenten ikke gjøre

- Endre rettslig grunnlag, roller, frister, lagringstider eller ansvarsbegrensninger uten at oppgaven sier det.
- Finne opp fakta om plattformen, som regioner, leverandører eller sikkerhetstiltak. Mangler noe, skriv et åpent spørsmål i pull requesten.
- Endre `effective_from` uten at et menneske har bestemt datoen.
- Legge kundespesifikke avtaler eller personopplysninger i repoet.

## Før du leverer

- Alle henvisninger skal peke på et anker som finnes.
- Ingen ord skal ha stor forbokstav midt i en setning, med unntak av egennavn.
- Ingen av de forbudte frasene skal forekomme.
- Alle ord merket med `{.term}` skal finnes i `data/glossary.yaml`, direkte eller via `key`.
- Alle genererte tabeller skal samsvare med `data/`.
- Kommentarer med `TODO` skal være fjernet når punktet er skrevet.
- `python scripts/gendoc.py check` skal gi 0 feil. Den kontrollerer det meste av listen over, også reglene for henvisninger mellom dokumentene.
- Ingen ord fra `avoid`-listene i ordlisten skal forekomme.
- Metadata skal være fylt ut.
