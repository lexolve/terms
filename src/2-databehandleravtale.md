---
title: Databehandleravtale
level: 2
anchored_in: 2-generelle-vilkar-virksomheter
service: null
effective_from: 2026-11-11
---

# Databehandleravtale

## 1 Partene og rollene {#parties}

Avtalen gjelder mellom Låvli og [virksomheten]{.term key=virksomhet} når virksomheten bruker Låvli Bedrift, Lexolve OS eller Låvli Plattform.
Virksomheten er behandlingsansvarlig, og Låvli er databehandler.

Virksomheten skal ha behandlingsgrunnlag for opplysningene som legges inn, også for særlige kategorier av personopplysninger og fødselsnummer.
Virksomheten skal informere de registrerte, og kan vise til personverndokumentet for tjenesten.

## 2 Behandlingen avtalen gjelder {#scope}

Avtalen gjelder personopplysningene Låvli behandler på vegne av [virksomheten]{.term key=virksomhet}, først og fremst i [innholdet]{.term key=innhold}.
Formålet er å levere tjenesten: å lagre innholdet og bruke KI-modeller til å besvare spørsmål og lage dokumenter.

Typer opplysninger, kategorier av registrerte og lagringstid står i personverndokumentet for tjenesten:

- [Låvli Bedrift](4-personvern-bedrift.md#processing)
- [Lexolve OS](4-personvern-lexolve-os.md#processing)
- [Låvli Plattform](4-personvern-plattform.md#processing)

Behandlingen varer så lenge avtalen gjelder.

## 3 Låvlis egen behandling {#own-processing}

Låvli er selv behandlingsansvarlig for opplysningene i tabellen, og den behandlingen er ikke omfattet av denne avtalen.
Andre opplysninger behandler Låvli bare som databehandler.

<!-- data: processing.yaml view=dpa-lavli services=bedrift,lexolve-os,plattform -->
| Opplysninger | Formål | Tjenester |
| --- | --- | --- |
| Navn, e-postadresse, rolle, innloggingsmetode, sesjonstokener og IP-adresse | Innlogging, brukerkonto og tilgangskontroll | Låvli Bedrift og Låvli Plattform |
| Navn, e-postadresse, telefonnummer, rolle og innloggingstokener | Innlogging, brukerkonto og tilgangskontroll | Lexolve OS |
| Trafikkdata, nettlesertype og operasjonelle logger, uten meldingsinnhold | Drift, feilretting og sikkerhet | Alle |
| Navn og e-postadresse | Meldinger om konto, sikkerhet, innlogging og endringer i tjenesten og vilkårene | Alle |
| Navn og e-postadresse | Nyhetsbrev og tilbud på e-post | Lexolve OS |
| Pseudonymiserte utdrag av spørsmål og svar | Forskningsprosjektet med SINTEF AS | Låvli Bedrift |
| Bruksstatistikk uten informasjonskapsler og uten lagret IP-adresse | Forstå hvordan tjenesten brukes, og forbedre den | Låvli Bedrift og Låvli Plattform |
| Bruker-ID, e-postadresse og hendelser i tjenesten | Forstå hvordan tjenesten brukes, og forbedre den | Lexolve OS |
| Fritekst brukeren skriver i tilbakemeldingsskjemaet | Behandle tilbakemeldinger og forbedre tjenesten | Låvli Bedrift og Låvli Plattform |
| Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | Fakturering og abonnement | Alle |
| Navn, e-postadresse og innholdet i henvendelsen | Brukerstøtte | Alle |
<!-- /data -->

[Forskningsuttrekk]{.term key=forskningsuttrekk} kan bare tas fra tjenester der de spesielle vilkårene eller kundeavtalen uttrykkelig tillater det.
Virksomheten gir Låvli instruks om å anonymisere [innholdet]{.term key=innhold} for å lage aggregert statistikk.
Statistikken inneholder ikke personopplysninger, og Låvli kan bruke den til egne formål.
Låvli skal ikke bruke innholdet til egne formål ut over det som står i dette punktet.

## 4 Instruks {#instructions}

Låvli skal bare behandle personopplysningene etter dokumentert instruks fra [virksomheten]{.term key=virksomhet}.
Instruksen består av denne avtalen, vilkårene for tjenesten og skriftlige instrukser fra virksomhetens kontaktperson.
Virksomheten kan sende skriftlige instrukser til personvern@lexolve.com.
Lagringstidene og mottakerne i personverndokumentet for tjenesten er en del av instruksen.

Låvli skal si fra uten ugrunnet opphold hvis en instruks ikke kan følges innenfor tjenestens standardoppsett.
Virksomheten kan da si opp avtalen med umiddelbar virkning.

Låvli skal også si fra straks hvis en instruks etter Låvlis vurdering er i strid med personvernregelverket.
Hvis EØS-rett eller norsk rett krever at Låvli behandler opplysningene utenfor instruksen, skal Låvli varsle virksomheten først, med mindre det er forbudt.

## 5 Taushetsplikt {#confidentiality}

Låvli skal bare gi tilgang til personopplysningene til personer som trenger det, og som har taushetsplikt etter avtale eller lov.
Låvli skal periodisk gå gjennom hvem som har tilgang.
Tilgangen skal fjernes når den ikke lenger trengs.

Andre får ikke tilgang uten instruks fra [virksomheten]{.term key=virksomhet} eller plikt etter EØS-rett eller norsk rett, med unntak av det som står i [punkt 3 om Låvlis egen behandling](#own-processing).

## 6 Sikkerhet {#security}

Låvli skal sikre personopplysningene med tiltakene i [sikkerhetsbeskrivelsen](2-sikkerhet.md).

## 7 Underleverandører {#subprocessors}

[Virksomheten]{.term key=virksomhet} godkjenner at Låvli bruker underleverandørene i personverndokumentet for tjenesten.
Låvli skal varsle virksomhetens kontaktperson på e-post minst 45 dager før en underleverandør legges til eller byttes.

Virksomheten kan protestere innen fristen.
Endringen regnes som godtatt hvis virksomheten ikke protesterer.
Hvis partene ikke blir enige, kan virksomheten si opp avtalen med 30 dagers varsel, uten andre kostnader enn løpende vederlag.

Låvli skal kontrollere at underleverandørene ved avtale er bundet av plikter som er minst like strenge som Låvlis etter denne avtalen.
Låvli svarer overfor virksomheten for at underleverandørene følger dem.

## 8 Overføring utenfor EU/EØS {#transfers}

Låvli skal ikke overføre personopplysningene ut av EU/EØS uten dokumentert instruks fra [virksomheten]{.term key=virksomhet}, med mindre EØS-rett eller norsk rett krever det.
Instruksen omfatter overføring til mottakerne som står med lokasjon utenfor EU/EØS i personverndokumentet for tjenesten.
For underleverandører med morselskap utenfor EU/EØS skal Låvli i tillegg bruke et gyldig overføringsgrunnlag, som EUs standardkontrakter.

## 9 Bistand og de registrertes rettigheter {#assistance}

Henvendelser fra registrerte om innholdet skal Låvli sende videre til [virksomheten]{.term key=virksomhet}.
Låvli skal på skriftlig forespørsel hjelpe virksomheten med å oppfylle de registrertes rettigheter etter GDPR kapittel III, slik at virksomheten kan overholde fristene i personvernregelverket.
Låvli skal slette opplysninger innen 14 virkedager etter at virksomheten har bedt om det.

Låvli skal også hjelpe virksomheten med sikkerhet, vurderinger av personvernkonsekvenser og forhåndsdrøftelser med Datatilsynet, ut fra det Låvli vet om behandlingen.

## 10 Brudd på personopplysningssikkerheten {#breaches}

Låvli skal varsle [virksomheten]{.term key=virksomhet} om brudd på personopplysningssikkerheten uten ugrunnet opphold, og senest 48 timer etter at Låvli ble kjent med bruddet.
Varselet skal beskrive bruddet, kategorier og omtrentlig antall berørte registrerte og opplysninger, de sannsynlige konsekvensene, tiltakene og hvem hos Låvli virksomheten kan kontakte.

Virksomheten melder bruddet til Datatilsynet og de registrerte når det kreves, og Låvli skal hjelpe til.

## 11 Revisjon {#audits}

Låvli skal gi [virksomheten]{.term key=virksomhet} informasjonen som trengs for å vise at avtalen følges, også oppdatert teknisk dokumentasjon.

Virksomheten, eller en revisor virksomheten velger, kan gjennomføre revisjon, også inspeksjon, høyst én gang i året og med minst 30 dagers varsel.
Begrensningene gjelder ikke etter et brudd på personopplysningssikkerheten eller ved pålegg fra Datatilsynet.
Før en revisjon kan Låvli tilby oppdatert dokumentasjon eller uavhengige rapporter.

## 12 Endringer {#changes}

Låvli skal varsle [virksomheten]{.term key=virksomhet} minst 30 dager før en endring i denne avtalen trer i kraft, og virksomheten kan si opp avtalen før det.
Låvli skal gi virksomheten beskjed på e-post når personverndokumentet for tjenesten eller sikkerhetsbeskrivelsen endres vesentlig.
Endringer i hvilke leverandører Låvli bruker, følger [punkt 7 om underleverandører](#subprocessors).

Forbudet mot å bruke innholdet til egne formål i [punkt 3 om Låvlis egen behandling](#own-processing) og punktet om taushetsplikt kan ikke endres til ugunst for virksomheten uten at den samtykker.
Det samme gjelder garantiene i punktet om forskning i personverndokumentet for tjenesten.

## 13 Varighet, sletting og eksport {#termination}

Avtalen gjelder så lenge Låvli behandler personopplysninger for [virksomheten]{.term key=virksomhet}.

Når avtalen opphører, kan virksomheten kreve eksport av opplysningene innen 30 dager.
Låvli skal slette personopplysningene når fristen for å kreve eksport er ute, og kopier i sikkerhetskopier innen 30 dager etter det.
Låvli skal på forespørsel bekrefte skriftlig at opplysningene er slettet.

Opplysninger Låvli er pålagt å lagre, skal sperres i stedet for å slettes.
