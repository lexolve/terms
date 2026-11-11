# Låvlis vilkår og personverninformasjon

Repoet inneholder kundeavtalen, vilkårene, databehandleravtalen, sikkerhetsbeskrivelsen og personverninformasjonen for Låvli Privat, Låvli Bedrift, Lexolve OS og Låvli Plattform.
Dokumentene ligger i [`src/`](src/).
Struktur, skriveregler og arbeidsregler står i [AGENTS.md](AGENTS.md).
[document-structure.html](document-structure.html) viser hvordan dokumentene henger sammen. Åpne filen i en nettleser.

## Kommandoer

```sh
pip install -r requirements.txt
python scripts/gendoc.py update   # skriver tabeller fra data/, punktnumre og numre i henvisninger inn i dokumentene
python scripts/gendoc.py check    # kontrollerer dokumentene
python scripts/gendoc.py build    # lager HTML i site/, med diagrammet som forside, og en PDF per tjeneste (krever pandoc og WeasyPrint)
python scripts/gendoc.py build --uten-pdf   # som build, men uten PDF-ene
```

PDF-ene ligger i `site/pdf/` og inneholder alle dokumentene som gjelder én tjeneste, med forside og innholdsfortegnelse.
Hvilke dokumenter som er med, står i `PACKAGES` i `scripts/gendoc.py`.
WeasyPrint trenger Pango. Se installasjonsveiledningen til WeasyPrint.
Skriftene IBM Plex ligger i `assets/fonts/`, så verken nettstedet eller PDF-ene henter noe fra Google Fonts.

Kontrollen kjøres også ved hver pull request og push til `main`.
Da bygges også HTML-versjonen og PDF-ene, som kan lastes ned som artefaktet «dokumenter-html» fra kjøringen under Actions.
Ved push til `main` publiseres den på <https://vilkar.lavli.no/>.
Den skal gi 0 feil. Merknadene om TODO viser hva som venter på avklaringer.

## Kryssjekk

Kommandoen `/crosscheck` i Claude Code kontrollerer lovkravene og at dokumentene stemmer med hverandre og med `data/`.
Den vurderer også om endringene som ikke er publisert, krever varsel. Med en commit som argument vurderer den endringene siden den commiten.
Kjør den før en endring publiseres.

Rapporten skrives til `verification/rapport.md`, som ikke er med i git. Kommandoen endrer ingen dokumenter.
Instruksen står i `.claude/commands/crosscheck.md`.
