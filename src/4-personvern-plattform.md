---
title: Personvern for Låvli Plattform
level: 4
anchored_in: 2-databehandleravtale
service: plattform
effective_from: 2026-11-11
---

# Personvern for Låvli Plattform

## 1 Om dokumentet {#about}

Dette dokumentet er for deg som bruker Låvli Plattform, og for andre som omtales i [innholdet]{.term key=innhold}.
Opplysninger om andre som omtales, kommer fra det brukerne skriver eller laster opp i tjenesten, og fra kilder virksomheten legger inn i kunnskapsbasen.
Det forklarer hvilke personopplysninger som behandles, hvem som er ansvarlig, og hvilke rettigheter du har.
For [virksomheten]{.term key=virksomhet} du er tilknyttet, er dokumentet også beskrivelsen av behandlingen Låvli gjør på vegne av virksomheten.
Gjeldende versjon av dokumentet er tilgjengelig på [vilkar.lavli.no](https://vilkar.lavli.no).

Det er frivillig å gi opplysninger, men du må oppgi kontaktinformasjon for å få tilgang til tjenesten.

## 2 Hvem er behandlingsansvarlig? {#controller}

Virksomheten du er tilknyttet, er behandlingsansvarlig for innholdet og de andre opplysningene som behandles for virksomheten.
Låvli er databehandler for disse opplysningene og behandler dem bare etter virksomhetens instruks.
For noen opplysninger er Låvli selv behandlingsansvarlig.

<!-- data: processing.yaml view=roles services=plattform -->
| Opplysninger | Formål | Behandlingsansvarlig |
| --- | --- | --- |
| Spørsmål, KI-svar, opplastede dokumenter og tidsstempel, som kan omfatte særlige kategorier av personopplysninger | Levere tjenesten | Virksomheten |
| Spørsmål, KI-svar og opplastede dokumenter | Anonymisering for å lage aggregert statistikk | Virksomheten |
| Navn, e-postadresse, rolle, innloggingsmetode, sesjonstokener og IP-adresse | Innlogging, brukerkonto og tilgangskontroll | Låvli |
| Trafikkdata, nettlesertype og operasjonelle logger, uten meldingsinnhold | Drift, feilretting og sikkerhet | Låvli |
| Tekniske spor av agentkjøringer, som kan inneholde spørsmål og svar | Feilsøking i KI-funksjonene | Virksomheten |
| Logg over hvem som har fått tilgang til eller åpnet innhold, og når | Kontroll med tilgang til innhold | Virksomheten |
| Kopier av opplysningene over | Gjenoppretting etter feil eller hendelser | Virksomheten |
| Navn og e-postadresse | Meldinger om konto, sikkerhet, innlogging og endringer i tjenesten og vilkårene | Låvli |
| Bruksstatistikk uten informasjonskapsler og uten lagret IP-adresse | Forstå hvordan tjenesten brukes, og forbedre den | Låvli |
| Fritekst brukeren skriver i tilbakemeldingsskjemaet | Behandle tilbakemeldinger og forbedre tjenesten | Låvli |
| Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | Fakturering og abonnement | Låvli |
| Navn, e-postadresse og innholdet i henvendelsen | Brukerstøtte | Låvli |
<!-- /data -->

## 3 Hva behandles for virksomheten? {#processing}

Låvli behandler disse opplysningene på vegne av [virksomheten]{.term key=virksomhet}, for å levere tjenesten.
Det rettslige grunnlaget fastsettes av virksomheten.

<!-- data: processing.yaml view=business services=plattform -->
| Opplysninger | Registrerte | Formål | Lagringstid | Sletting |
| --- | --- | --- | --- | --- |
| Spørsmål, KI-svar, opplastede dokumenter og tidsstempel, som kan omfatte særlige kategorier av personopplysninger | Brukere og personer som omtales i samtaler og dokumenter | Levere tjenesten | Stilles inn av virksomheten | Automatisk i trinn, med arkivering, gjenopprettingsperiode og permanent sletting. Ved opphør etter 30 dager, når fristen for å kreve eksport er ute, og i sikkerhetskopier innen ytterligere 30 dager |
| Spørsmål, KI-svar og opplastede dokumenter | Brukere og personer som omtales i samtaler og dokumenter | Anonymisering for å lage aggregert statistikk | Ikke lenger enn innholdet. Statistikken inneholder ikke personopplysninger | Når lagringstiden er ute |
| Tekniske spor av agentkjøringer, som kan inneholde spørsmål og svar | Brukere og personer som omtales i samtaler | Feilsøking i KI-funksjonene | Om lag 14 dager | Når lagringstiden er ute |
| Logg over hvem som har fått tilgang til eller åpnet innhold, og når | Brukere og Låvlis driftspersonell | Kontroll med tilgang til innhold | 400 dager | Når lagringstiden er ute |
| Kopier av opplysningene over | Som for opplysningene som kopieres | Gjenoppretting etter feil eller hendelser | Et begrenset antall generasjoner, lagret i EU/EØS | Innen 30 dager etter at opplysningene er slettet ved opphør |
<!-- /data -->

## 4 Egen instans og kunnskapsbase {#instance}

[Virksomheten]{.term key=virksomhet} har en egen instans av Låvli, og virksomhetens administratorer bestemmer hvem som har tilgang.
Administratorene har ikke innsyn i den enkelte brukers samtaler eller dokumenter, med mindre brukeren selv gir andre i virksomheten tilgang til [innholdet]{.term key=innhold}.

Virksomheten kan legge egne kilder, dokumenter og maler inn i en kunnskapsbase som KI-modellene bruker når de svarer.
Opplysninger i kunnskapsbasen behandles på samme måte som annet innhold.

## 5 Hva behandler Låvli selv? {#own-processing}

For disse opplysningene er Låvli behandlingsansvarlig.

<!-- data: processing.yaml view=lavli services=plattform -->
| Opplysninger | Registrerte | Formål | Rettslig grunnlag | Lagringstid | Sletting |
| --- | --- | --- | --- | --- | --- |
| Navn, e-postadresse, rolle, innloggingsmetode, sesjonstokener og IP-adresse | Brukere | Innlogging, brukerkonto og tilgangskontroll | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å gi virksomhetens brukere sikker tilgang) | Så lenge kontoen eller avtalen består. Sesjoner så lenge sesjonen varer | Når lagringstiden er ute |
| Trafikkdata, nettlesertype og operasjonelle logger, uten meldingsinnhold | Brukere | Drift, feilretting og sikkerhet | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i sikker og stabil drift) | 30 dager | Når lagringstiden er ute |
| Navn og e-postadresse | Brukere | Meldinger om konto, sikkerhet, innlogging og endringer i tjenesten og vilkårene | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å informere brukerne) | Så lenge kontoen består | Når lagringstiden er ute |
| Bruksstatistikk uten informasjonskapsler og uten lagret IP-adresse | Brukere | Forstå hvordan tjenesten brukes, og forbedre den | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å forbedre tjenesten) | 1 år | Når lagringstiden er ute |
| Fritekst brukeren skriver i tilbakemeldingsskjemaet | Brukere | Behandle tilbakemeldinger og forbedre tjenesten | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å forbedre tjenesten) | 1 år | Når lagringstiden er ute |
| Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | Virksomhetens fakturakontakt | Fakturering og abonnement | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å fakturere virksomheten) og bokstav c (bokføringsloven) | 5 år etter utgangen av regnskapsåret | Når lagringstiden er ute |
| Navn, e-postadresse og innholdet i henvendelsen | Brukere | Brukerstøtte | GDPR art. 6 nr. 1 bokstav f (berettiget interesse i å hjelpe brukerne) | Så lenge kontoen består | Når kontoen slettes, eller tidligere hvis du ber om det |
<!-- /data -->

Låvli bruker ikke innholdet til forskning, med mindre kundeavtalen sier noe annet.
Låvli bruker ikke innholdet til å trene KI-modeller.
Interesseavveiningen for behandlingen som bygger på berettiget interesse, får du på forespørsel.

## 6 Hvem får opplysningene? {#recipients}

Tabellen viser hvem som får opplysninger, og om de er underleverandører som behandler opplysningene for Låvli, eller selvstendig behandlingsansvarlige.

<!-- data: recipients.yaml view=business services=plattform -->
| Mottaker | Oppgave | Rolle | Gjelder | Opplysninger | Lokasjon | Overføringsgrunnlag |
| --- | --- | --- | --- | --- | --- | --- |
| Google Cloud (Google Ireland Ltd.) | Infrastruktur, database, lagring og kjøring av KI-modeller | Underleverandør | Begge | All lagring | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Anthropic | Claude-modeller for hovedresonnering, kjørt via Google Cloud | Underleverandør | Begge | Spørsmål og svar | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Google (Gemini) | Sekundæroppgaver som klassifisering, oppslag og titler | Underleverandør | Begge | Spørsmål og svar | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Amazon Web Services | Reserve for kjøring av KI-modeller ved failover | Underleverandør | Begge | Spørsmål og svar ved failover | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Kinde | Innlogging og sesjon | Underleverandør | Låvlis egen behandling | Identitets- og autentiseringsdata | EU | Standardkontrakter (SCC) |
| LangChain (LangSmith) | Teknisk sporing av agentkjøringer, med kort oppbevaring | Underleverandør | Begge | Kan inneholde spørsmål og svar | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| PostHog | Produktanalyse uten informasjonskapsler, autocapture eller opptak av økter | Underleverandør | Låvlis egen behandling | Bruksstatistikk. Ikke samtaleinnhold, men fritekst i tilbakemeldingsskjemaet | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Staan.ai | Websøk utenfor rettskildebasene, med maskert søkestreng | Underleverandør | Begge | Maskert søkestreng | EU | – |
| Customer.io | Tjenestemeldinger | Underleverandør | Låvlis egen behandling | Kontaktopplysninger | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Chargebee | Fakturering og abonnement | Underleverandør | Låvlis egen behandling | Virksomhet, fakturakontakt, e-postadresse og betalingsstatus | EU | Standardkontrakter (SCC) som tilleggsgaranti |
| Lovdata | Søk i rettskilder | Selvstendig behandlingsansvarlig | Behandling for virksomheten | Automatisk genererte søkeord | Norge | – |
| Offentlige myndigheter | Utlevering når loven krever det | Selvstendig behandlingsansvarlig | Begge | Det loven krever | Norge | – |
<!-- /data -->

Låvli slår også opp i Enhetsregisteret og Regnskapsregisteret.
Tekst fra samtalene sendes ikke dit.

Opplysningene lagres og behandles i EU/EØS.
For leverandører med morselskap utenfor EU/EØS brukes EUs standardkontrakter som tilleggsgaranti.
Du kan få en kopi av standardkontraktene ved å kontakte Låvli.

[Sikkerhetsbeskrivelsen](2-sikkerhet.md) forklarer hvordan Låvli sikrer opplysningene.

## 7 Dine rettigheter {#rights}

Du har rett til innsyn, retting, sletting, begrensning, dataportabilitet og å protestere (GDPR art. 15–21).
Du kan når som helst trekke tilbake et samtykke du har gitt.

For innholdet og de andre opplysningene som behandles for virksomheten, kontakter du [virksomheten]{.term key=virksomhet} du er tilknyttet, og Låvli hjelper virksomheten.
For opplysningene Låvli behandler selv, kontakter du Låvli.
Låvli svarer innen én måned.

Låvli treffer ikke avgjørelser som utelukkende bygger på automatisert behandling, og som har rettsvirkning for deg eller påvirker deg i betydelig grad.

## 8 Kontakt og klage {#contact}

Låvli AS, org.nr. 918 567 852, Kongens gate 3, 0153 Oslo, er behandlingsansvarlig for opplysningene Låvli behandler selv.
For henvendelser om personvern kan du bruke personvern@lexolve.com.

Du kan klage til Datatilsynet, Postboks 458 Sentrum, 0105 Oslo, datatilsynet.no.
