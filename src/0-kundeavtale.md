---
title: Kundeavtale
level: 0
anchored_in: null
service: null
effective_from: 2026-11-11
fields:
  - name: kundeNavn
    label: Virksomhetens navn
    question: Hva heter virksomheten?
    type: text
    required: true
  - name: kundeOrgnr
    label: Org.nr.
    question: Hva er virksomhetens organisasjonsnummer?
    type: text
    required: true
  - name: kundeAdresse
    label: Adresse
    question: Hva er virksomhetens adresse?
    type: text
    required: true
  - name: lavliKontakt
    label: Kontaktperson hos Låvli
    question: Hvem er kontaktperson hos Låvli? Oppgi navn og e-postadresse.
    type: text
    required: true
  - name: kundeKontakt
    label: Kontaktperson hos virksomheten
    question: Hvem er kontaktperson hos virksomheten? Oppgi navn og e-postadresse.
    type: text
    required: true
  - name: domene
    label: Domene
    question: Hvilket underdomene på lavli.no skal tjenesten ha?
    type: text
    required: true
  - name: produksjonsdato
    label: Produksjonsdato
    question: Hvilken dato settes tjenesten i produksjon?
    type: date
    required: true
  - name: oppsett
    label: Oppsett før produksjon
    question: Hva skal Låvli sette opp før tjenesten settes i produksjon, for eksempel kunnskapsbase og innlogging med virksomhetens identitetsløsning?
    type: text
    required: true
  - name: kreditterPerManed
    label: KI-kreditter per måned
    question: Hvor mange KI-kreditter har virksomheten per måned?
    type: number
    required: false
    default: "1 000"
  - name: manedspris
    label: Pris per måned
    question: Hvor mange kroner koster Låvli Plattform per måned?
    type: amount
    required: false
    default: "30 000"
  - name: overforbrukPris
    label: Pris per KI-kreditt ved overforbruk
    question: Hvor mange kroner koster en KI-kreditt ut over den månedlige rammen?
    type: amount
    required: false
    default: "30"
  - name: tillegg
    label: Tillegg
    question: Hvilke tillegg bestiller virksomheten, for eksempel moduler eller oppsett av kunnskapsbase?
    type: table
    required: false
    columns:
      - { name: post, label: Post }
      - { name: omfang, label: Omfang }
      - { name: pris, label: Pris }
  - name: fakturering
    label: Fakturering
    question: Hvor ofte faktureres faste beløp og overforbruk?
    type: choice
    required: false
    default: kvartalsvis
    options:
      - { value: månedlig, label: Månedlig }
      - { value: kvartalsvis, label: Kvartalsvis }
      - { value: årlig, label: Årlig }
  - name: startdato
    label: Første avtaleperiode begynner
    question: Hvilken dato begynner den første avtaleperioden?
    type: date
    required: true
  - name: avvik
    label: Avvik
    question: "Hvilke avvik fra standardvilkårene er avtalt? Hvert avvik begynner med «I stedet for punkt … gjelder: …», «I tillegg til punkt … gjelder: …» eller «I tillegg gjelder: …»."
    type: list
    required: false
  - name: lavliSignatar
    label: Signatar for Låvli
    question: Hvem signerer for Låvli? Oppgi navn og stilling.
    type: text
    required: true
  - name: kundeSignatar
    label: Signatar for virksomheten
    question: Hvem signerer for virksomheten? Oppgi navn og stilling.
    type: text
    required: true
---

# Kundeavtale

## 1 Parter og kontaktpersoner {#parties}

Låvli: Låvli AS, org.nr. 918 567 852, Kongens gate 3, 0153 Oslo.
Kontaktperson: {{lavliKontakt}}.

Virksomheten: {{kundeNavn}}, org.nr. {{kundeOrgnr}}, {{kundeAdresse}}.
Kontaktperson: {{kundeKontakt}}.

Den som er oppgitt som kontaktperson for [virksomheten]{.term key=virksomhet}, er også kontaktperson etter vilkårene.

## 2 Leveranse {#delivery}

Låvli leverer Låvli Plattform til [virksomheten]{.term key=virksomhet} på {{domene}}.lavli.no.
Tjenesten settes i produksjon {{produksjonsdato}}.
Før det setter Låvli opp {{oppsett}}.

## 3 Bestilling {#order}

- Låvli Plattform: {{kreditterPerManed}} [KI-kreditter]{.term key=KI-kreditt} per måned, {{manedspris}} kr per måned.
- Overforbruk ut over den månedlige rammen: {{overforbrukPris}} kr per KI-kreditt.
{{#each tillegg}}
- {{post}}: {{omfang}}, {{pris}} kr.
{{/each}}

Faste beløp faktureres {{fakturering}} på forskudd, overforbruk {{fakturering}} etterskuddsvis.
Prisene kan justeres etter [punkt 2 om avtale, pris og betaling](3-spesielle-vilkar-plattform.md#payment) i Spesielle vilkår for Låvli Plattform.

## 4 Avtaleperiode {#term}

Den første avtaleperioden begynner {{startdato}}.
Varighet og fornyelse følger [punkt 5 om oppsigelse og sletting](3-spesielle-vilkar-plattform.md#termination) i Spesielle vilkår for Låvli Plattform.

## 5 Avtaledokumenter {#documents}

Følgende dokumenter er også en del av avtalen, i gjeldende versjon, og er tilgjengelige på [vilkar.lavli.no](https://vilkar.lavli.no):

- [Overordnede vilkår for Låvlis tjenester](1-overordnede-vilkar.md)
- [Generelle vilkår for virksomheter](2-generelle-vilkar-virksomheter.md)
- [Spesielle vilkår for Låvli Plattform](3-spesielle-vilkar-plattform.md)
- [Databehandleravtale](2-databehandleravtale.md)
- [Personvern for Låvli Plattform](4-personvern-plattform.md)
- [Sikkerhet](2-sikkerhet.md)

Endringer i dokumentene varsles etter reglene i dem, og gjelder også for denne avtalen.
Avvikene nedenfor kan bare endres skriftlig av begge parter.

## 6 Avvik fra standardvilkårene {#deviations}

{{#each avvik}}
- {{this}}
{{else}}
Det er ingen avvik fra standardvilkårene.
{{/each}}

## 7 Signaturer {#signatures}

Avtalen signeres digitalt.

For Låvli AS: {{lavliSignatar}}

For {{kundeNavn}}: {{kundeSignatar}}
