---
title: Personvern for Lexolve OS
level: 4
anchored_in: 2-databehandleravtale
service: lexolve-os
effective_from: 2026-11-11
---

# Personvern for Lexolve OS

## 1 Om dokumentet {#about}

Dette dokumentet er for deg som bruker Lexolve OS, og for andre som omtales i [innholdet]{.term key=innhold}.
Opplysninger om andre som omtales, kommer fra det brukerne skriver eller laster opp i tjenesten.
Det forklarer hvilke personopplysninger som behandles, hvem som er ansvarlig, og hvilke rettigheter du har.
For [virksomheten]{.term key=virksomhet} du er tilknyttet, er dokumentet også beskrivelsen av behandlingen Låvli gjør på vegne av virksomheten.
Gjeldende versjon av dokumentet er tilgjengelig på [vilkar.lavli.no](https://vilkar.lavli.no).

Det er frivillig å gi opplysninger, men du må oppgi kontaktinformasjon for å få tilgang til tjenesten.

## 2 Hvem er behandlingsansvarlig? {#controller}

Virksomheten du er tilknyttet, er behandlingsansvarlig for innholdet og de andre opplysningene som behandles for virksomheten.
Låvli er databehandler for disse opplysningene og behandler dem bare etter virksomhetens instruks.
For noen opplysninger er Låvli selv behandlingsansvarlig.

<!-- data: processing.yaml view=roles services=lexolve-os -->
| Opplysninger | Formål | Behandlingsansvarlig |
| --- | --- | --- |
| Saksinnhold, spørsmål, KI-svar, opplastede dokumenter og dokumenter som lages med maler, og tidsstempel, som kan omfatte særlige kategorier av personopplysninger | Levere tjenesten | Virksomheten |
| Spørsmål, KI-svar og opplastede dokumenter | Anonymisering for å lage aggregert statistikk | Virksomheten |
| Navn, e-postadresse, telefonnummer, rolle og innloggingstokener | Innlogging, brukerkonto og tilgangskontroll | Låvli |
| Trafikkdata, nettlesertype og operasjonelle logger, uten meldingsinnhold | Drift, feilretting og sikkerhet | Låvli |
| Tekniske spor av agentkjøringer, som kan inneholde spørsmål og svar | Feilsøking i KI-funksjonene | Virksomheten |
| Logg over hvem som har fått tilgang til eller åpnet innhold, og når | Kontroll med tilgang til innhold | Virksomheten |
| Kopier av opplysningene over | Gjenoppretting etter feil eller hendelser | Virksomheten |
| Navn og e-postadresse | Meldinger om konto, sikkerhet, innlogging og endringer i tjenesten og vilkårene | Låvli |
| Navn og e-postadresse | Nyhetsbrev og tilbud på e-post | Låvli |
| Bruker-ID, e-postadresse og hendelser i tjenesten | Forstå hvordan tjenesten brukes, og forbedre den | Låvli |
| Navn og e-postadresse til dem som signerer, dokumentet som signeres, fingeravtrykk av dokumentet og PAdES-signaturen | Elektronisk signering av dokumenter | Virksomheten |
| Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | Fakturering og abonnement | Låvli |
| Navn, e-postadresse og innholdet i henvendelsen | Brukerstøtte | Låvli |
<!-- /data -->

## 3 Hva behandles for virksomheten? {#processing}

Låvli behandler disse opplysningene på vegne av [virksomheten]{.term key=virksomhet}, for å levere tjenesten.
Det rettslige grunnlaget fastsettes av virksomheten.

<!-- data: processing.yaml view=business services=lexolve-os -->
| Opplysninger | Registrerte | Formål | Lagringstid | Sletting |
| --- | --- | --- | --- | --- |
| Saksinnhold, spørsmål, KI-svar, opplastede dokumenter og dokumenter som lages med maler, og tidsstempel, som kan omfatte særlige kategorier av personopplysninger | Brukere og personer som omtales i saker og dokumenter | Levere tjenesten | Så lenge kontoen består | Automatisk i trinn, med arkivering, gjenopprettingsperiode og permanent sletting. Ved opphør etter 30 dager, når fristen for å kreve eksport er ute, og i sikkerhetskopier innen ytterligere 30 dager |
| Spørsmål, KI-svar og opplastede dokumenter | Brukere og personer som omtales i samtaler og dokumenter | Anonymisering for å lage aggregert statistikk | Ikke lenger enn innholdet. Statistikken inneholder ikke personopplysninger | Når lagringstiden er ute |
| Tekniske spor av agentkjøringer, som kan inneholde spørsmål og svar | Brukere og personer som omtales i samtaler | Feilsøking i KI-funksjonene | 30 dager | Når lagringstiden er ute |
| Logg over hvem som har fått tilgang til eller åpnet innhold, og når | Brukere og Låvlis driftspersonell | Kontroll med tilgang til innhold | 400 dager | Når lagringstiden er ute |
| Kopier av opplysningene over | Som for opplysningene som kopieres | Gjenoppretting etter feil eller hendelser | Et begrenset antall generasjoner, lagret i EU/EØS | Innen 30 dager etter at opplysningene er slettet ved opphør |
| Navn og e-postadresse til dem som signerer, dokumentet som signeres, fingeravtrykk av dokumentet og PAdES-signaturen | De som signerer | Elektronisk signering av dokumenter | Så lenge kontoen består | Når lagringstiden er ute |
<!-- /data -->

## 4 Digital signering {#signing}

Når [virksomheten]{.term key=virksomhet} sender et dokument til elektronisk signering, får Signicat dokumentet og navn og e-postadresse til dem som skal signere.
Signeringen skjer hos Signicat.
Låvli får tilbake det signerte dokumentet med en PAdES-signatur, navnet på den som har signert, og et fingeravtrykk av dokumentet, men ikke fødselsnummer.

## 5 Hva behandler Låvli selv? {#own-processing}

For disse opplysningene er Låvli behandlingsansvarlig.

<!-- data: processing.yaml view=lavli services=lexolve-os -->
| Opplysninger | Registrerte | Formål | Rettslig grunnlag | Lagringstid | Sletting |
| --- | --- | --- | --- | --- | --- |
| Navn, e-postadresse, telefonnummer, rolle og innloggingstokener | Brukere | Innlogging, brukerkonto og tilgangskontroll | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å gi virksomhetens brukere sikker tilgang) | Så lenge kontoen eller avtalen består. Sesjoner så lenge sesjonen varer | Når lagringstiden er ute |
| Trafikkdata, nettlesertype og operasjonelle logger, uten meldingsinnhold | Brukere | Drift, feilretting og sikkerhet | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i sikker og stabil drift) | 30 dager | Når lagringstiden er ute |
| Navn og e-postadresse | Brukere | Meldinger om konto, sikkerhet, innlogging og endringer i tjenesten og vilkårene | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å informere brukerne) | Så lenge kontoen består | Når lagringstiden er ute |
| Navn og e-postadresse | Brukere | Nyhetsbrev og tilbud på e-post | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å markedsføre egne tjenester til kunder), jf. markedsføringsloven § 15 | Til du melder deg av | Når lagringstiden er ute |
| Bruker-ID, e-postadresse og hendelser i tjenesten | Brukere | Forstå hvordan tjenesten brukes, og forbedre den | GDPR art. 6 nr. 1 bokstav a (samtykke), jf. ekomloven | 11 måneder | Når lagringstiden er ute |
| Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | Virksomhetens fakturakontakt | Fakturering og abonnement | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å fakturere virksomheten) og bokstav c (bokføringsloven) | 5 år etter utgangen av regnskapsåret | Når lagringstiden er ute |
| Navn, e-postadresse og innholdet i henvendelsen | Brukere | Brukerstøtte | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å hjelpe brukerne) | Så lenge kontoen består | Når kontoen slettes, eller tidligere hvis du ber om det |
<!-- /data -->

Låvli bruker ikke innholdet til forskning eller til å trene KI-modeller.
Interesseavveiningen for behandlingen som bygger på berettiget interesse, får du på forespørsel.

## 6 Hvem får opplysningene? {#recipients}

Tabellen viser hvem som får opplysninger, og om de er underleverandører som behandler opplysningene for Låvli, eller selvstendig behandlingsansvarlige.

<!-- data: recipients.yaml view=business services=lexolve-os -->
| Mottaker | Oppgave | Rolle | Gjelder | Opplysninger | Lokasjon | Overføringsgrunnlag |
| --- | --- | --- | --- | --- | --- | --- |
| Google Cloud (Google Ireland Ltd.) | Infrastruktur, database, lagring og kjøring av KI-modeller | Underleverandør | Begge | All lagring | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Google (Vertex AI og Gemini) | Saksagent, dokumentanalyse, utlesing av opplysninger, sammendrag, søk og oversettelse | Underleverandør | Behandling for virksomheten | Saksinnhold, dokumenter og spørsmål | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Google Firebase | Innlogging | Underleverandør | Låvlis egen behandling | E-postadresse, telefonnummer og innloggingstokener | USA | Data Privacy Framework (DPF), med standardkontrakter (SCC) som reserve |
| Twilio | SMS og engangskoder ved innlogging | Underleverandør | Låvlis egen behandling | Telefonnummer og innholdet i SMS-en | USA | Data Privacy Framework (DPF) og bindende virksomhetsregler (BCR), med standardkontrakter (SCC) som reserve |
| SendGrid (Twilio) | E-post med invitasjoner til konto og signering, og kontroll av e-postadresser | Underleverandør | Begge | Navn, e-postadresse og innholdet i e-posten, for eksempel dokumenttittel | USA | Data Privacy Framework (DPF), med standardkontrakter (SCC) som reserve |
| Chargebee | Fakturering og abonnement | Underleverandør | Låvlis egen behandling | Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Customer.io | Markedsføring og meldinger gjennom kundeforholdet | Underleverandør | Låvlis egen behandling | Bruker-ID, e-postadresse, egenskaper og hendelser | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Intercom | Brukerstøtte | Underleverandør | Låvlis egen behandling | Navn, e-postadresse og innholdet i henvendelsen | USA | Data Privacy Framework (DPF), med standardkontrakter (SCC) som reserve |
| Amplitude | Produktanalyse og inntektshendelser | Underleverandør | Låvlis egen behandling | Bruker-ID, e-postadresse og hendelser | USA | Data Privacy Framework (DPF), med standardkontrakter (SCC) som reserve |
| Signicat | Elektronisk signering | Underleverandør | Behandling for virksomheten | Navn og e-postadresse til dem som signerer, og dokumentene som skal signeres | Norge | – |
| Tavily | Websøk for saksagenten | Underleverandør | Behandling for virksomheten | Søkestrenger som er avidentifisert før de sendes, uten personopplysninger | USA | – |
| Lovdata | Søk i rettskilder | Selvstendig behandlingsansvarlig | Behandling for virksomheten | Spørsmålsteksten, som kan inneholde detaljer fra saken | Norge | – |
| Offentlige myndigheter | Utlevering når loven krever det | Selvstendig behandlingsansvarlig | Begge | Det loven krever | Norge | – |
<!-- /data -->

Noen leverandører behandler opplysninger utenfor EU/EØS.
Tabellen viser hvor, og hvilket overføringsgrunnlag som brukes.
Du kan få en kopi av standardkontraktene ved å kontakte Låvli.

[Sikkerhetsbeskrivelsen](2-sikkerhet.md) forklarer hvordan Låvli sikrer opplysningene.

## 7 Dine rettigheter {#rights}

Du har rett til innsyn, retting, sletting, begrensning, dataportabilitet og å protestere (GDPR art. 15–21).
Du kan når som helst trekke tilbake et samtykke du har gitt.
Du kan når som helst protestere mot markedsføring på e-post, for eksempel ved å melde deg av i e-posten.

For innholdet og de andre opplysningene som behandles for virksomheten, kontakter du [virksomheten]{.term key=virksomhet} du er tilknyttet, og Låvli hjelper virksomheten.
For opplysningene Låvli behandler selv, kontakter du Låvli.
Låvli svarer innen én måned.

Låvli treffer ikke avgjørelser som utelukkende bygger på automatisert behandling, og som har rettsvirkning for deg eller påvirker deg i betydelig grad.

## 8 Kontakt og klage {#contact}

Låvli AS, org.nr. 918 567 852, Kongens gate 3, 0153 Oslo, er behandlingsansvarlig for opplysningene Låvli behandler selv.
For henvendelser om personvern kan du bruke personvern@lexolve.com.

Du kan klage til Datatilsynet, Postboks 458 Sentrum, 0105 Oslo, datatilsynet.no.
