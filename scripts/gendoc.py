#!/usr/bin/env python3
"""Verktøy for dokumentene i repoet.

  python scripts/gendoc.py update   Skriver tabeller fra data/, punktnumre og numre i henvisninger inn i dokumentene.
  python scripts/gendoc.py check    Kontrollerer dokumentene. Avslutter med feil hvis noe er galt.
  python scripts/gendoc.py build    Lager HTML i site/: diagrammet som forside og ett HTML-dokument per dokument,
                                    og en PDF med alle dokumentene for hver tjeneste. Krever pandoc og WeasyPrint.
  python scripts/gendoc.py build --uten-pdf   Som build, men uten PDF-ene.

Reglene står i AGENTS.md.
"""

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "src"
DOC_PATTERN = re.compile(r"^[0-4]-[a-z0-9-]+\.md$")

SERVICES = ["privat", "bedrift", "lexolve-os", "plattform"]
CONTROLLER_LABELS = {"lavli": "Låvli", "business": "Virksomheten"}
ROLE_LABELS = {
    "processor": "Underleverandør",
    "independent_controller": "Selvstendig behandlingsansvarlig",
    "unresolved": "Uavklart",
}
PART_LABELS = {
    "business": "Behandling for virksomheten",
    "lavli": "Låvlis egen behandling",
    "both": "Begge",
}

# Fraser som ikke skal brukes, uansett stor eller liten forbokstav.
FORBIDDEN_PHRASES = [
    "herunder",
    "inkludert, men ikke begrenset til",
    "forbeholder seg retten",
    "for så vidt gjelder",
    "i den utstrekning",
    "sørger for",
    "påser",
    "særvilkår",
    "særlige vilkår",
    "næringsvilkår",
    "fellesvilkår",
    "personvernerklæring",
    "personvernforordningen",
]
# Ord som ikke skal stå med stor forbokstav midt i en setning.
NO_CAPITAL_MID_SENTENCE = [
    "Behandlingsansvarlig",
    "Databehandler",
    "Leverandøren",
    "Kunden",
    "Virksomheten",
    "Tjenesten",
    "Avtalen",
]
# Ord som ikke skal brukes i dokumentteksten, med nøyaktig skrivemåte.
FORBIDDEN_EXACT = ["DPA"]

REQUIRED_METADATA = ["title", "level", "anchored_in", "service", "effective_from"]

MARKER = re.compile(r"(<!-- data: (?P<spec>[^>]*?) -->\n)(?P<body>.*?)(<!-- /data -->)", re.DOTALL)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ANCHOR = re.compile(r"\{#([a-z0-9-]+)\}\s*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TERM = re.compile(r"\[([^\]]+)\]\{\.term(?:\s+key=([^\s}]+))?\}")
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
H2 = re.compile(r"^## (?:\d+ )?(.+?) \{#([a-z0-9-]+)\}[ \t]*$", re.M)
REF = re.compile(r"\[punkt(?: \d+)? om ([^\]]+)\]\(([^)\s#]*)#([a-z0-9-]+)\)")
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def load(name):
    with open(DATA / name, encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def resolve(value, service):
    """Henter verdien for en tjeneste når feltet har én verdi per tjeneste."""
    if isinstance(value, dict):
        return value.get(service)
    return value


def cell(value):
    if value is None or value == "":
        return "–"
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(cell(v) for v in row) + " |")
    return "\n".join(lines) + "\n"


def parse_spec(spec):
    parts = spec.split()
    source = parts[0]
    params = dict(p.split("=", 1) for p in parts[1:])
    return source, params


DEFAULT_DELETION = "Når lagringstiden er ute"
SERVICE_NAMES = {"privat": "Låvli Privat", "bedrift": "Låvli Bedrift", "lexolve-os": "Lexolve OS", "plattform": "Låvli Plattform"}


def service_list(hits, services):
    if set(hits) == set(services):
        return "Alle"
    names = [SERVICE_NAMES[s] for s in hits]
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " og " + names[-1]


def deletion(row, service):
    return resolve(row.get("deletion"), service) or DEFAULT_DELETION


# Felt i maler, etter malformatet i legal-knowledge (docs/PIPELINE.md, «Tenant templates»).
FIELD_NAME = re.compile(r"^[a-z][a-zA-Z0-9]*$")
FIELD_LABEL = re.compile(r"^[A-ZÆØÅ][A-ZÆØÅ0-9 ._/\-,()]*$")
FIELD_TYPES = {"text", "date", "amount", "number", "choice", "multichoice", "boolean", "list", "table"}
FIELD_KEYWORDS = {"if", "unless", "each", "else", "check", "eq", "includes", "this"}
HANDLEBARS = re.compile(r"\{\{([^{}]*)\}\}")


def field_problems(fields, body):
    """Kontrollerer feltene i metadata mot feltene som brukes i teksten."""
    problems, declared = [], set()
    for f in fields or []:
        name = f.get("name", "")
        if not FIELD_NAME.match(name):
            problems.append(f"ugyldig feltnavn: {name!r}")
        if name in declared:
            problems.append(f"feltet er deklarert flere ganger: {name}")
        declared.add(name)
        if not FIELD_LABEL.match(str(f.get("label", "")).upper()):
            problems.append(f"ugyldig label for feltet {name}: {f.get('label')!r}")
        if f.get("type") not in FIELD_TYPES:
            problems.append(f"ukjent type for feltet {name}: {f.get('type')!r}")
        for key in ("label", "question", "type", "required"):
            if key not in f:
                problems.append(f"feltet {name} mangler {key}")
        if "default" in f and f.get("required"):
            problems.append(f"feltet {name} har default, men er påkrevd")
        if f.get("type") == "table":
            declared.update(c["name"] for c in f.get("columns", []))
    used = set()
    for inner in HANDLEBARS.findall(body):
        inner = re.sub(r'"[^"]*"', "", inner)
        used.update(w for w in re.findall(r"[a-zA-Z][a-zA-Z0-9]*", inner) if w not in FIELD_KEYWORDS)
    problems += [f"feltet brukes, men er ikke deklarert: {n}" for n in sorted(used - declared)]
    problems += [f"feltet er deklarert, men brukes ikke: {n}" for n in sorted(declared - used)]
    return problems


def processing_rows(params, controller=None):
    service = params["services"]
    for row in load("processing.yaml"):
        if service not in row.get("services", []):
            continue
        ctrl = resolve(row.get("controller"), service)
        if controller and ctrl != controller:
            continue
        yield row, service, ctrl


def render(spec):
    source, params = parse_spec(spec)
    view = params.get("view")

    if source == "glossary.yaml":
        rows = sorted(load("glossary.yaml"), key=lambda r: r["term"].casefold())
        return table(["Begrep", "Definisjon"], [[r["term"][:1].upper() + r["term"][1:], r.get("definition")] for r in rows])

    if source == "recipients.yaml":
        service = params["services"]
        rows = [r for r in load("recipients.yaml") if service in r.get("services", [])]
        if view == "business":
            return table(
                ["Mottaker", "Oppgave", "Rolle", "Gjelder", "Opplysninger", "Lokasjon", "Overføringsgrunnlag"],
                [[r["name"], r.get("task"), ROLE_LABELS.get(r.get("role")), PART_LABELS.get(r.get("part")),
                  resolve(r.get("personal_data"), service), r.get("location"), r.get("transfer_basis")] for r in rows],
            )
        return table(
            ["Mottaker", "Oppgave", "Rolle", "Opplysninger", "Lokasjon", "Overføringsgrunnlag"],
            [[r["name"], r.get("task"), ROLE_LABELS.get(r.get("role")), resolve(r.get("personal_data"), service),
              r.get("location"), r.get("transfer_basis")] for r in rows],
        )

    if source == "processing.yaml":
        if view == "roles":
            return table(
                ["Opplysninger", "Formål", "Behandlingsansvarlig"],
                [[resolve(r.get("personal_data"), s), resolve(r.get("purpose"), s), CONTROLLER_LABELS.get(c, "TODO")]
                 for r, s, c in processing_rows(params)],
            )
        if view == "business":
            return table(
                ["Opplysninger", "Registrerte", "Formål", "Lagringstid", "Sletting"],
                [[resolve(r.get("personal_data"), s), resolve(r.get("data_subjects"), s), resolve(r.get("purpose"), s),
                  resolve(r.get("retention"), s), deletion(r, s)]
                 for r, s, c in processing_rows(params, controller="business")],
            )
        if view in ("lavli", "privat"):
            return table(
                ["Opplysninger", "Registrerte", "Formål", "Rettslig grunnlag", "Lagringstid", "Sletting"],
                [[resolve(r.get("personal_data"), s), resolve(r.get("data_subjects"), s), resolve(r.get("purpose"), s),
                  resolve(r.get("legal_basis"), s), resolve(r.get("retention"), s), deletion(r, s)]
                 for r, s, c in processing_rows(params, controller="lavli")],
            )
        if view == "dpa-lavli":
            services = params["services"].split(",")
            rows = []
            for r in load("processing.yaml"):
                hits = [s for s in services if s in r.get("services", []) and resolve(r.get("controller"), s) == "lavli"]
                # Én rad per ulik verdi, slik at tjenester med egne opplysninger eller formål får sin egen rad.
                groups = {}
                for s in hits:
                    key = (resolve(r.get("personal_data"), s), resolve(r.get("purpose"), s))
                    groups.setdefault(key, []).append(s)
                for (personal_data, purpose), group in groups.items():
                    rows.append([personal_data, purpose, service_list(group, services)])
            return table(["Opplysninger", "Formål", "Tjenester"], rows)

    raise ValueError(f"Ukjent tabell: {spec}")


PRIVAT_SIDE = {"2-vilkar-privat.md", "4-personvern-privat.md"}
SECURITY = "2-sikkerhet.md"
BUSINESS_PRIVACY = {"4-personvern-bedrift.md", "4-personvern-lexolve-os.md", "4-personvern-plattform.md"}


def is_business_side(name):
    return name in {"0-kundeavtale.md", "2-generelle-vilkar-virksomheter.md", "2-databehandleravtale.md"} \
        or name.startswith("3-") or name in BUSINESS_PRIVACY


def reference_problems(source, target):
    """Reglene for henvisninger mellom dokumenter, se AGENTS.md."""
    if source == SECURITY:
        yield "sikkerhetsbeskrivelsen skal ikke henvise til andre dokumenter"
    if source in BUSINESS_PRIVACY and target != SECURITY:
        yield "personverndokumentet kan bare henvise til sikkerhetsbeskrivelsen"
    if (source in PRIVAT_SIDE and is_business_side(target)) or (is_business_side(source) and target in PRIVAT_SIDE):
        yield "Privat-siden og virksomhetssiden skal ikke henvise til hverandre"


def documents():
    return sorted(p for p in DOCS.iterdir() if DOC_PATTERN.match(p.name))


def section_numbers():
    """Nummeret til hvert hovedpunkt (##), per dokument og anker."""
    numbers = {}
    for path in documents():
        anchors = [m.group(2) for m in H2.finditer(path.read_text(encoding="utf-8"))]
        numbers[path.name] = {a: i for i, a in enumerate(anchors, 1)}
    return numbers


def updated(name, text, numbers):
    """Teksten slik skriptet vil ha den: tabeller fra data/, nummererte punkter og henvisninger."""
    text = MARKER.sub(lambda m: m.group(1) + render(m.group("spec")) + m.group(4), text)
    counter = iter(range(1, 1000))
    text = H2.sub(lambda m: f"## {next(counter)} {m.group(1)} {{#{m.group(2)}}}", text)

    def ref(m):
        topic, file, anchor = m.group(1), m.group(2), m.group(3)
        n = numbers.get(file or name, {}).get(anchor)
        if n is None:
            return m.group(0)
        return f"[punkt {n} om {topic}]({file}#{anchor})"

    return REF.sub(ref, text)


def cmd_update():
    numbers = section_numbers()
    for path in documents():
        text = path.read_text(encoding="utf-8")
        new = updated(path.name, text, numbers)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(f"Oppdatert: {path.name}")


def headings(text):
    anchors, errors = [], []
    for line in text.splitlines():
        m = HEADING.match(line)
        if not m:
            continue
        a = ANCHOR.search(line)
        if a:
            anchors.append(a.group(1))
            if len(a.group(1)) > 20:
                errors.append(f"ankeret er for langt, bruk et kort engelsk anker: {a.group(1)}")
        elif len(m.group(1)) > 1:
            errors.append(f"overskrift uten anker: {line.strip()}")
    return anchors, errors


def cmd_check():
    errors, warnings = [], []
    docs = documents()
    names = {p.name for p in docs}
    stems = {p.stem for p in docs}
    anchors = {}
    texts = {}

    numbers = section_numbers()
    glossary = load("glossary.yaml")
    terms = {g["term"] for g in glossary}
    avoid = [w for g in glossary for w in g.get("avoid", [])]

    for path in docs:
        text = path.read_text(encoding="utf-8")
        texts[path.name] = text
        found, errs = headings(text)
        anchors[path.name] = found
        errors += [f"{path.name}: {e}" for e in errs]
        dupes = {a for a in found if found.count(a) > 1}
        errors += [f"{path.name}: anker brukt flere ganger: {a}" for a in dupes]

        fm = FRONT_MATTER.match(text)
        if not fm:
            errors.append(f"{path.name}: mangler metadata")
        else:
            meta = yaml.safe_load(fm.group(1)) or {}
            for key in REQUIRED_METADATA:
                if key not in meta:
                    errors.append(f"{path.name}: metadata mangler nøkkelen {key}")
            if str(meta.get("level")) != path.name[0]:
                errors.append(f"{path.name}: level stemmer ikke med filnavnet")
            if meta.get("anchored_in") and meta["anchored_in"] not in stems:
                errors.append(f"{path.name}: anchored_in viser til et dokument som ikke finnes: {meta['anchored_in']}")
            if meta.get("service") and meta["service"] not in SERVICES:
                errors.append(f"{path.name}: ukjent tjeneste: {meta['service']}")
            if "fields" in meta:
                body = FRONT_MATTER.sub("", text)
                errors += [f"{path.name}: {e}" for e in field_problems(meta["fields"], body)]

        if updated(path.name, text, numbers) != text:
            errors.append(f"{path.name}: tabeller, punktnumre eller henvisninger er ikke oppdatert. Kjør: python scripts/gendoc.py update")

        warnings += [f"{path.name}: {n} TODO" for n in [text.count("TODO")] if n]

    for name, text in texts.items():
        body = COMMENT.sub("", FRONT_MATTER.sub("", text))
        for target in LINK.findall(body):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            file, _, anchor = target.partition("#")
            file = file or name
            if file != name:
                for problem in reference_problems(name, file):
                    errors.append(f"{name}: {problem}: {target}")
            if file not in names:
                errors.append(f"{name}: lenke til dokument som ikke finnes: {target}")
            elif anchor and anchor not in anchors[file]:
                errors.append(f"{name}: lenke til anker som ikke finnes: {target}")
        for word, key in TERM.findall(body):
            if (key or word) not in terms:
                errors.append(f"{name}: begrepet finnes ikke i ordlisten: {key or word}")
        for phrase in FORBIDDEN_PHRASES + avoid:
            if re.search(r"\b" + re.escape(phrase) + r"\b", body, re.IGNORECASE):
                errors.append(f"{name}: bruker «{phrase}»")
        prose = re.sub(r"^#.*$", "", body, flags=re.M)
        for word in NO_CAPITAL_MID_SENTENCE:
            if re.search(r"(?<=[a-zæøå0-9,;:)»]\s)" + re.escape(word) + r"\b", prose):
                errors.append(f"{name}: «{word}» med stor forbokstav midt i en setning")
        for word in FORBIDDEN_EXACT:
            if re.search(r"\b" + re.escape(word) + r"\b", body):
                errors.append(f"{name}: bruker «{word}»")

    for w in warnings:
        print(f"Merknad: {w}")
    for e in errors:
        print(f"Feil: {e}")
    print(f"{len(docs)} dokumenter kontrollert, {len(errors)} feil.")
    return 1 if errors else 0



# Bygging av HTML -----------------------------------------------------------

SITE = ROOT / "site"
DIAGRAM = ROOT / "document-structure.html"
REPO = "https://github.com/lexolve/terms"
# Maler vises i diagrammet, men publiseres ikke som egne sider.
NOT_PUBLISHED = {"0-kundeavtale.md"}
SITE_URL = "https://vilkar.lavli.no/"

# Dokumentpakkene som kan lastes ned som PDF, med dokumentene i den rekkefølgen de står i pakken.
PACKAGES = {
    "privat": ["1-overordnede-vilkar.md", "2-vilkar-privat.md", "4-personvern-privat.md", "2-sikkerhet.md"],
    **{
        service: [
            "1-overordnede-vilkar.md", "2-generelle-vilkar-virksomheter.md", f"3-spesielle-vilkar-{service}.md",
            "2-databehandleravtale.md", f"4-personvern-{service}.md", "2-sikkerhet.md",
        ]
        for service in ["bedrift", "lexolve-os", "plattform"]
    },
}


def package_path(service):
    return f"pdf/avtalevilkar-{service}.pdf"
FIELD = re.compile(r"\{\{[^{}]*\}\}")

PAGE = """<!doctype html>
<html lang="nb">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Låvli</title>
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/fonts.css">
<style>
:root{{--bg:#FAF9F7;--ink:#212121;--muted:#6F6F6F;--line:#E4E1DB;--card:#FFFFFF;--soft:#FDF5F2;--head:#015040;--link:#015040;--accent:#B8401F;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0E1513;--ink:#ECEFED;--muted:#A5ADA9;--line:#2A3430;--card:#18201D;--soft:#1F2925;--head:#BFE6D8;--link:#8FD3BC;--accent:#F08A66;color-scheme:dark}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;font-size:16px;line-height:1.6}}
nav{{max-width:860px;margin:0 auto;padding:22px 24px 0;font-size:14px;font-weight:500;display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px}}
nav .brand{{margin-right:auto;line-height:0}}
nav .brand img{{height:34px;width:auto}}
nav a{{color:var(--muted);text-decoration:none}}
nav a:hover{{color:var(--accent)}}
main{{max-width:860px;margin:16px auto 32px;padding:32px 36px;background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 16px 40px rgba(184,64,31,.06)}}
h1{{font-size:32px;font-weight:600;line-height:1.2;letter-spacing:-.02em;color:var(--head);margin:0 0 6px}}
.meta{{color:var(--muted);font-size:13px;margin:0 0 24px}}
.meta a{{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;color:inherit}}
.meta a:hover{{color:var(--accent)}}
.downloads{{color:var(--muted);font-size:13px;margin:-16px 0 24px}}
h2{{font-size:19px;font-weight:600;color:var(--head);margin:32px 0 8px;padding-top:12px;border-top:1px solid var(--line)}}
h3{{font-size:16px;font-weight:600;margin:20px 0 6px}}
a{{color:var(--link);text-underline-offset:2px}}
a:hover{{color:var(--accent)}}
table{{border-collapse:collapse;width:100%;font-size:13.5px;margin:12px 0;display:block;overflow-x:auto}}
th,td{{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}}
th{{background:var(--soft);font-weight:600}}
abbr.term{{text-decoration:underline dotted;text-decoration-color:var(--muted);cursor:help}}
.field{{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:13px;background:var(--soft);border:1px dashed var(--line);border-radius:4px;padding:0 4px}}
footer{{max-width:860px;margin:0 auto 40px;padding:0 24px;color:var(--muted);font-size:13px}}
footer a{{color:inherit}}
@media (max-width:600px){{main{{padding:20px 16px;border-radius:0;border-left:0;border-right:0}}nav{{padding:16px 16px 0}}h1{{font-size:26px}}}}
</style>
</head>
<body>
<nav>
<a class="brand" href="index.html"><picture><source srcset="assets/logo-white.png" media="(prefers-color-scheme:dark)"><img src="assets/logo.png" alt="Låvli" width="86" height="34"></picture></a>
<a href="index.html">Alle avtalevilkår</a>
<a href="{history}">Endringer i dokumentet</a>
</nav>
<main>
<h1>{title}</h1>
<p class="meta">{meta}</p>
{downloads}
{body}
</main>
<footer>Låvli AS · <a href="https://vilkar.lavli.no/">vilkar.lavli.no</a></footer>
</body>
</html>
"""


def page_name(name):
    """Navnet på HTML-siden: uten nivånummer, slik at adressen ikke endres hvis dokumentet flyttes til et annet nivå."""
    return re.sub(r"^[0-4]-", "", Path(name).stem) + ".html"


def page_markdown(text, terms):
    """Gjør markdown klar for pandoc: lenker til .html, begreper med forklaring, felt i maler."""
    body = FRONT_MATTER.sub("", text)
    body = re.sub(r"^# .*\n", "", body, count=1, flags=re.M)

    def link(m):
        target = m.group(2)
        if not target.startswith(("http://", "https://", "mailto:")):
            target = re.sub(r"^([0-4]-[a-z0-9-]+\.md)", lambda t: page_name(t.group(1)), target)
        return f"[{m.group(1)}]({target})"

    body = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)(?!\{)", link, body)

    def term(m):
        word, key = m.group(1), m.group(2) or m.group(1)
        definition = terms.get(key, "")
        return f'<abbr class="term" title="{html.escape(definition, quote=True)}">{word}</abbr>'

    body = TERM.sub(term, body)
    body = FIELD.sub(lambda m: f'<span class="field">{html.escape(m.group(0))}</span>', body)
    return body


def diagram_with_links(names, pdf=True):
    """Diagrammet som forside, med lenke fra hver dokumentboks til HTML-versjonen."""
    page = DIAGRAM.read_text(encoding="utf-8")

    def box(m):
        section = m.group(0)
        f = re.search(r'<div class="file">([^<]*)</div>', section)
        if not f:
            return section
        if f.group(1) not in names:
            return section.replace(f.group(0), "")
        href = page_name(f.group(1))
        if f.group(1) in BUSINESS_PRIVACY:
            # Uten boksen med felles oppsett viser vi alle punktene, hentet fra dokumentet.
            text = (DOCS / f.group(1)).read_text(encoding="utf-8")
            items = "".join(f"<li>{html.escape(t)}</li>" for t in re.findall(r"^## (?:\d+ )?(.+?) \{#", text, flags=re.M))
            section = re.sub(r'<p class="sub">.*?</ul>', f"<ol>{items}</ol>", section, flags=re.S)
        section = re.sub(r"<h2>([^<]+)", lambda h: f'<h2><a class="doc" href="{href}">{h.group(1).strip()}</a> ', section, count=1)
        section = section.replace("<section ", f'<section data-doc="{f.group(1)}" ', 1)
        return section.replace(f.group(0), "")

    page = re.sub(r"<section\b.*?</section>", box, page, flags=re.S)
    # Boksen med felles oppsett for personvern er et hjelpemiddel for oss som skriver, ikke et dokument.
    page = re.sub(r'\s*<section class="[^"]*" id="pv-mal".*?</section>', "", page, flags=re.S)
    css = ("a.doc{color:inherit;text-decoration:none}a.doc:hover{text-decoration:underline}"
           ".box h2{margin-bottom:8px}"
           ".box:has(a.doc):hover{box-shadow:0 0 0 2px var(--hl),0 6px 18px var(--card-shadow)}"
           ".box:has(a.doc){cursor:pointer}")
    css += (".legend a.pdf{display:inline-flex;align-items:center;gap:6px;padding:4px 12px;border:1px solid var(--gray-b);"
            "border-radius:999px;background:var(--gray-f);color:var(--ink);font-weight:500;text-decoration:none}"
            ".legend a.pdf:hover,.legend a.pdf:focus-visible{border-color:var(--head);box-shadow:0 0 0 1px var(--head);outline:none}"
            ".legend a.pdf svg{width:13px;height:13px}"
            ".legend a.pdf{transition:opacity .15s}.legend a.pdf.dim{opacity:.35}"
            ".legend a.pdf.dim:hover,.legend a.pdf.dim:focus-visible{opacity:1}")
    page = page.replace("</style>", css + "</style>", 1)
    if not pdf:
        return finish(page)
    icon = ('<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="M8 2v8M4.5 6.5 8 10l3.5-3.5M3 13h10"/></svg>')
    links = ""
    for s in PACKAGES:
        selector = html.escape(",".join('[data-doc="' + d + '"]' for d in PACKAGES[s]))
        links += (f'\n      <a class="pdf" href="{package_path(s)}" data-service="{s}" data-docs="{selector}">'
                  f'{icon}{SERVICE_NAMES[s]}</a>')
    row = f'    <div class="legend" role="group" aria-label="Last ned som PDF">\n      <b>Last ned</b>{links}\n    </div>\n'
    end = "  </div>\n</header>"
    assert page.count(end) == 1, "Fant ikke slutten på forklaringene i diagrammet"
    page = page.replace(end, row + end)
    return finish(page)


def finish(page):
    script = ("<script>document.querySelectorAll('.box').forEach(function(b){var a=b.querySelector('a.doc');"
              "if(a){b.addEventListener('click',function(e){if(e.target.tagName!=='A'){location.href=a.getAttribute('href');}});}});"
              "var w=document.getElementById('wrap'),bs=w.querySelectorAll('.box');"
              "document.querySelectorAll('a.pdf').forEach(function(l){var s=l.getAttribute('data-docs');"
              "function on(){w.setAttribute('data-hl','');bs.forEach(function(b){b.classList.toggle('hit',b.matches(s));});}"
              "function off(){if(window.showLocked){showLocked();return;}"
              "w.removeAttribute('data-hl');bs.forEach(function(b){b.classList.remove('hit');});}"
              "l.addEventListener('mouseenter',on);l.addEventListener('focus',on);"
              "l.addEventListener('mouseleave',off);l.addEventListener('blur',off);});</script>")
    return page.replace("</body>", script + "</body>", 1)


def last_commit(*paths):
    """Kort hash, full hash og dato for siste commit som endret en av filene, eller None."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H %cs", "--", *(str(p.relative_to(ROOT)) for p in paths)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.split()
    except (OSError, subprocess.CalledProcessError):
        return None
    if len(out) != 2:
        return None
    sha, date = out
    y, m, d = date.split("-")
    return sha[:7], sha, f"{d}.{m}.{y}"


PDF_CSS = """
@page{size:A4;margin:20mm 18mm 22mm;
  @bottom-left{content:"Avtalevilkår for SERVICE";font:7.5pt "IBM Plex Sans";color:#6F6F6F}
  @bottom-right{content:"Side " counter(page) " av " counter(pages);font:7.5pt "IBM Plex Sans";color:#6F6F6F}}
@page:first{@bottom-left{content:none}@bottom-right{content:none}}
html{font-family:"IBM Plex Sans",sans-serif;font-size:9.5pt;line-height:1.5;color:#212121}
.cover{padding-top:30mm}
.cover img{height:12mm;width:auto}
.cover h1{font-size:26pt;font-weight:600;line-height:1.15;color:#015040;margin:22mm 0 4mm;bookmark-level:none}
.cover .meta{font-size:10pt;color:#6F6F6F;margin:0 0 1mm}
.cover .meta a{color:#6F6F6F}
.toc{margin-top:16mm;padding:0;list-style:none;font-size:11pt}
.toc li{margin:0 0 3mm}
.toc a{color:#212121;text-decoration:none}
.toc a::after{content:leader(". ") target-counter(attr(href), page);color:#6F6F6F}
.note{margin-top:16mm;font-size:8.5pt;color:#6F6F6F}
section.doc{break-before:page}
h1{font-size:19pt;font-weight:600;line-height:1.2;color:#015040;margin:0 0 2mm;bookmark-level:1}
.doc>.meta{font-size:8pt;color:#6F6F6F;margin:0 0 6mm}
.doc>.meta a{color:#6F6F6F;font-family:"IBM Plex Mono",monospace}
h2{font-size:11.5pt;font-weight:600;color:#015040;margin:7mm 0 2mm;padding-top:3mm;border-top:.5pt solid #E4E1DB;bookmark-level:2;break-after:avoid}
h3{font-size:10pt;font-weight:600;margin:4mm 0 1mm;bookmark-level:none;break-after:avoid}
p{margin:0 0 2.5mm;orphans:2;widows:2}
ul,ol{margin:0 0 2.5mm;padding-left:5mm}
li{margin:0 0 1mm}
a{color:#015040;text-decoration:none}
abbr{text-decoration:none}
table{width:100%;border-collapse:collapse;font-size:7.5pt;line-height:1.35;margin:2mm 0 4mm}
th,td{border:.5pt solid #D9D5CE;padding:1.5mm 2mm;text-align:left;vertical-align:top}
th{background:#FDF5F2;font-weight:600}
thead{display:table-header-group}
tr{break-inside:avoid}
.field{font-family:"IBM Plex Mono",monospace;font-size:8pt}
"""


def package_html(service, bodies, infos):
    """Én HTML-fil med forside, innholdsfortegnelse og alle dokumentene i pakken, klar for WeasyPrint."""
    names = PACKAGES[service]
    stems = {page_name(n): Path(page_name(n)).stem for n in names}

    def internal(body, stem):
        # Ankrene går igjen i flere dokumenter, så de får dokumentnavnet foran seg.
        body = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{stem}--{m.group(1)}"', body)

        def href(m):
            target = m.group(1)
            if target.startswith("#"):
                return f'href="#{stem}--{target[1:]}"'
            if re.match(r"[a-z]+:", target):
                return m.group(0)
            page, _, fragment = target.partition("#")
            if page in stems:
                return f'href="#{stems[page]}--{fragment}"' if fragment else f'href="#{stems[page]}"'
            return f'href="{SITE_URL}{target}"'

        return re.sub(r'href="([^"]*)"', href, body)

    title = f"Avtalevilkår for {SERVICE_NAMES[service]}"
    commit = last_commit(*(DOCS / n for n in names))
    version = (f'Versjon <a href="{REPO}/tree/{commit[1]}/src">{commit[0]}</a> av {commit[2]}'
               if commit else "Versjon som ikke er committet")
    effective = sorted({infos[n][1] for n in names if infos[n][1]})
    toc = "".join(f'<li><a href="#{stems[page_name(n)]}">{html.escape(infos[n][0])}</a></li>' for n in names)
    parts = [
        '<section class="cover"><img src="assets/logo.png" alt="Låvli">',
        f"<h1>{html.escape(title)}</h1>",
        f'<p class="meta">Gjelder fra {", ".join(effective)}</p>' if effective else "",
        f'<p class="meta">{version}</p>',
        f'<p class="meta"><a href="{SITE_URL}">{SITE_URL.removeprefix("https://").rstrip("/")}</a></p>',
        f'<ol class="toc">{toc}</ol>',
        f'<p class="note">Gjeldende versjon av dokumentene står alltid på {SITE_URL.removeprefix("https://").rstrip("/")}. '
        "Endringene i hvert dokument kan ses i historikken på GitHub.</p></section>",
    ]
    for n in names:
        stem = stems[page_name(n)]
        parts.append(
            f'<section class="doc" id="{stem}"><h1>{html.escape(infos[n][0])}</h1>'
            f'<p class="meta">{infos[n][2]}</p>{internal(bodies[n], stem)}</section>'
        )
    css = PDF_CSS.replace("SERVICE", SERVICE_NAMES[service])
    return (f'<!doctype html><html lang="nb"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<meta name="author" content="Låvli AS"><link rel="stylesheet" href="assets/fonts.css">'
            f"<style>{css}</style></head><body>{''.join(parts)}</body></html>")


def cmd_build(pdf=True):
    if not shutil.which("pandoc"):
        print("Fant ikke pandoc. Installer pandoc og prøv igjen.")
        return 1
    if pdf:
        try:
            import weasyprint
        except (ImportError, OSError) as error:
            print(f"Fant ikke WeasyPrint ({error}). Installer den, eller kjør build --uten-pdf.")
            return 1
    terms = {t["term"]: t.get("definition", "") for t in load("glossary.yaml")}
    docs = [p for p in documents() if p.name not in NOT_PUBLISHED]
    names = {p.name for p in docs}
    pages = [page_name(n) for n in names]
    duplicates = sorted({n for n in pages if pages.count(n) > 1})
    if duplicates:
        print("To dokumenter får samme HTML-navn: " + ", ".join(duplicates))
        return 1
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copytree(ROOT / "assets", SITE / "assets")
    bodies, infos = {}, {}
    for path in docs:
        text = path.read_text(encoding="utf-8")
        fm = FRONT_MATTER.match(text)
        meta = yaml.safe_load(fm.group(1)) if fm else {}
        markdown = page_markdown(text, terms)
        body = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html5", "--wrap=none"],
            input=markdown, capture_output=True, text=True, check=True,
        ).stdout
        commit = last_commit(path)
        if commit:
            short, sha, date = commit
            info = f'Versjon <a href="{REPO}/blob/{sha}/src/{path.name}">{short}</a> av {date}'
        else:
            info = "Versjon som ikke er committet"
        effective = meta.get("effective_from")
        if effective:
            if hasattr(effective, "strftime"):
                effective = effective.strftime("%d.%m.%Y")
            effective = html.escape(str(effective))
            info += f" · gjelder fra {effective}"
        title = meta.get("title", path.stem)
        bodies[path.name], infos[path.name] = body, (title, effective, info)
        packages = [s for s in PACKAGES if path.name in PACKAGES[s]] if pdf else []
        downloads = ""
        if packages:
            links = " · ".join(f'<a href="{package_path(s)}">{SERVICE_NAMES[s]}</a>' for s in packages)
            downloads = f'<p class="downloads">Last ned alle avtalevilkår for tjenesten som PDF: {links}</p>'
        (SITE / page_name(path.name)).write_text(
            PAGE.format(
                title=html.escape(title), meta=info, body=body, downloads=downloads,
                history=f"{REPO}/commits/main/src/{path.name}",
            ),
            encoding="utf-8",
        )
    (SITE / "index.html").write_text(diagram_with_links(names, pdf), encoding="utf-8")
    print(f"Bygget {len(docs)} dokumenter og forsiden i {SITE.relative_to(ROOT)}/")
    if pdf:
        missing = sorted({n for s in PACKAGES for n in PACKAGES[s]} - set(bodies))
        if missing:
            print("Dokumentpakkene viser til dokumenter som ikke finnes: " + ", ".join(missing))
            return 1
        (SITE / "pdf").mkdir()
        for service in PACKAGES:
            target = SITE / package_path(service)
            weasyprint.HTML(string=package_html(service, bodies, infos), base_url=str(SITE)).write_pdf(target)
            print(f"Bygget {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "update":
        cmd_update()
    elif command == "check":
        sys.exit(cmd_check())
    elif command == "build":
        sys.exit(cmd_build(pdf="--uten-pdf" not in sys.argv[2:]))
    else:
        print(__doc__)
        sys.exit(2)
