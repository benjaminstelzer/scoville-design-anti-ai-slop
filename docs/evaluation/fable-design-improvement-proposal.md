# Fable design-improvement proposal

Source: persisted Fable consultation 7d03e896-c898-42a4-abee-b39d759bde77, requested claude-fable-5-1 / high. Backend model name not returned. Read-only installed-package review followed by concrete improvement proposals. This is the unaltered answer, not evidence of implementation or effectiveness. User selected this direction for implementation planning on 2026-09-04.

## Befundprüfung am Paket

Ich habe alle 31 Dateien gelesen und die Befunde gegengeprüft. Ergebnis:

- **Aufrechterhalten:** Befunde 2, 3, 5, 6, 9 sowie Schreibweisenmix, Kleinbuchstaben in `concept-development-and-selection.md:102` und `editorial-and-fixed-media-design.md:80`, fehlende Load-IDs C10 und C19, Generierungskommentar in `SKILL.md:151`, WCAG-Nummern im Motion-Modul.
- **Befund 1 eingegrenzt:** Anti-Generik-Passagen stehen in 16 Modulen, nicht nur in vier. Konkrete visuelle Marker liefern aber nur `style-direction.md:98-104`, `logo-and-identity-mark-design.md:53-55` und `imagery-and-art-direction.md:80-82`. Alles andere sind Einzeiler wie "consistent but generic". Ein positives Gegenprogramm fehlt weiterhin. Kern des Befunds bleibt.
- **Befund 4 umformuliert:** Das Budget ist in `modules.yaml:59-67` ausdrücklich als "advisory" deklariert, Überschreitungen gelten nicht als Fehler. Es liegt also keine Regelverletzung vor. Der Vergleichswert 1500 ist aber für rund 190 dichte Zeilen unrealistisch. Nach Zeichenzahl schätze ich den Kern auf das Doppelte bis Zweieinhalbfache. Nicht gemessen.
- **Befund 7 korrigiert:** Scoville UI und Scribe kommen in sieben Dateien vor, nicht in acht. Inhalt des Befunds bleibt.
- **Befund 8 teilweise zurückgenommen:** "expert", "field owner" und "soft observer" sind in `SKILL.md:33-35` und `61-62` definiert. Undefiniert bleiben "leaf", "falsifier" und "claim ceiling". Die Routing-Tabellenzellen in `SKILL.md:74-80` bleiben kryptisch.
- **Kleinbefund korrigiert:** Neun Module setzen keine Backticks um Quellen-IDs, nicht zehn. Fünf Module haben keine Markdown-Zeilenumbrüche nach Status und Intervention. Beides bestätigt.
- **Nicht prüfbar:** Die Datierungen 2025 und 2026 im Quellenindex. Sie sind intern konsistent mit dem Research-Freeze vom 2026-09-02 in `source-index.md:4`. Die referenzierten Ledger-Dateien unter docs/research liegen nicht im Paket.

## Gestaltungshilfen je Modul

Alle Einfügetexte folgen der Paketlogik: Signatur, zu prüfende Ursache, legitimer Fall, subjektspezifischer Gegenzug. Kein Verbotskatalog, das würde `style-direction.md:115-117` und `ui-workflow-and-interaction-design.md:110-112` widersprechen.

**1. Neues Modul statt Verstreuung.** Ich empfehle eine neue Datei `references/generic-signatures-and-subject-specificity.md`, geroutet über ein neues Signal `generic_cliche` im Enum in `modules.yaml:13` und einen Indexeintrag in `SKILL.md`. Das Label "generic-cliche judgment" in `modules.yaml:368` und `critique-and-validation.md:10` wandert dorthin. So bleibt das Critique-Modul beim Lifecycle und die Token-Ziele halten. Kerninhalt der neuen Datei:

```markdown
# Generic signatures and subject specificity

Status: `stub`  
Intervention: `focus`  
Sources: `SRC-CRITIQUE-CANON`, `SRC-CONCEPT-EVIDENCE`, `SRC-FOUNDATION-GRAPHIC`, `SRC-STYLE-HISTORY`

## Load when

Load when an artifact must be judged or repaired for interchangeability, or
when a thesis must become subject-specific before execution. Do not load for
a deliberate quiet utility direction whose familiarity job is recorded, or for
an incumbent-system execution with no open visual decision.

## Subject evidence inventory

Before generating or judging, inventory the verified subject evidence the work
may carry: process or method, object or product geometry, material and its
behaviour, place and route, language and naming, data and its shape, routine
or ritual, tension or conflict, audience behaviour. Mark each
`supplied | observed | inferred | unknown`. Only `supplied` or `observed`
items may carry a decision.

## Specificity ladder

| Level | Test | Typical cause when stuck here |
| --- | --- | --- |
| 0 subject-free | swapping logo and nouns serves any unrelated subject | mechanism came from a template, trend or mood keywords |
| 1 category | fits any competitor in the same category | category shorthand replaced evidence, such as leaf for eco, spark for AI, globe for global |
| 2 subject-specific | only this subject's evidence explains the carrier | normal execution gate |
| 3 subject-and-context | also explains this audience, moment, medium or place | required when placement or timing is the message |

Level 2 is the normal gate. A quiet utility direction may stay at level 1
deliberately; record that choice and its falsifier instead of adding
decoration to climb the ladder.

## Recognisable generic signatures

Use this inventory to localise interchangeability, not to ban patterns. A row
is a defect only when the cause is confirmed and the legitimate case does not
apply.

| Signature | Cause to test | Legitimate when | Subject-specific counter-move |
| --- | --- | --- | --- |
| Uniform card or bento grid over unrelated content | container chosen before content relations; every unit given equal consequence | units are true peers and scannable comparison is the task | rank consequence, merge or split units, vary span and density by relation, drop containers that only decorate |
| Mesh, blob or purple-to-blue gradient background with glow | background has no material, light or content cause | gradient reproduces a real material, light or data continuum and survives print, dark and forced-colour states | surface derived from subject material, a real image, flat incumbent colour, or nothing |
| Centered hero: headline, subline, two buttons, floating device mockup | page structure copied from a landing template rather than from the argument order | the product is the argument and the first decision is one action | rebuild section order from the audience's first question; show the real product state or evidence first |
| Three feature columns, icon plus title plus sentence, repeated per section | content fitted into a template rhythm; icons are decorative | the three items are true peers and each icon carries a distinct meaning | vary structure by content type; replace icons with real screenshots, data or objects, or drop them |
| Pseudo-3D glossy icons, isometric city, abstract floating shapes | illustration chosen by mood keyword, not by image job | subject is literally spatial, mechanical or architectural | derive imagery from the subject's real objects, process steps, place, hands, materials |
| Default sans, one weight scale, uniform radius and shadow everywhere | framework defaults used without a role map | incumbent design system mandates them | assign type and token roles from subject voice and reading task; keep defaults only where they carry a role |
| All-caps tracked eyebrow label above every heading | one hierarchy device applied by habit | it distinguishes a real category or section level | remove where it marks nothing; use the fewest signals that separate roles |
| Stock-style people photo: laughing team at laptop, handshake, pointing at whiteboard | image selected by mood keyword; no subject relation | the depicted event is the real subject | photograph or brief the actual place, task, object or person with a role |
| Sparkle, wand or orb motif signalling "AI" or "innovation" | category shorthand replaced subject evidence | the motif is an incumbent asset | show what the feature does on the user's real content |
| Placeholder social proof: "10k+ users", five-star row, generic logo bar | fabricated evidence filled a template slot | supplied, verifiable and rights-cleared | remove or replace with supplied evidence; label placeholders explicitly |
| Fade-up stagger on every element; parallax on scroll | motion applied as a template effect without a temporal thesis | motion carries state, order or attention transfer | route to Motion; derive motion from the subject's actual change or remove it |
| KPI tile row with gauges or donut charts | metric model absent; encoding taken from a dashboard library | task is monitoring a few accepted thresholds | route to Information Design; encode from decision and field semantics |

## Counter-move and removal test

Removing a signature is not the repair. The repair binds one verified subject
fact to the affected decision. After the repair, hide the loudest remaining
cue and check that the whole still reads as this subject. Then rerun the
level-0 swap test.

## Proof, ownership and claim ceiling

This leaf owns the specificity judgment and counter-move. Concept owns the
thesis; craft owners execute. A level rating is a reviewer judgment on the
inspected artifact, not audience recognition or originality evidence.
```

**2. SKILL.md, Schritt 3 "Make or inspect", nach Zeile 84.** Ein Satz, der den Anspruch des Paketnamens im Kern verankert:

```markdown
   A thesis is subject-specific when at least one verified subject fact
   visibly shapes hierarchy, type, colour, image or motion, and swapping logo
   and nouns would no longer let the artifact serve an unrelated subject.
   Record which fact carries which decision; "none yet" is a valid interim
   state for a utility artifact, not a defect.
```

Zusätzlich in Zeile 52 die Feldliste um `subject evidence` ergänzen.

**3. composition-and-layout.md, Schritt 3, nach Zeile 58:**

```markdown
   Derive at least one spatial constant from the subject rather than from a
   framework default: a product module, a page or tile size, a data cadence,
   a route, a document format, a manufacturing tolerance. Record its origin
   as `supplied | measured | inferred | default`. A default is allowed but is
   not a design decision.
```

Tabelle nach Zeile 87, zwei Zeilen:

```markdown
| Uniform card or bento grid, or blanket centring | container or template preceded content relations; every unit received equal consequence and span |
| Section stack with identical heights and rhythm | page composed from a section library rather than from argument order and content consequence |
```

**4. typography-and-typesetting.md, Schritt 2, nach Zeile 52:**

```markdown
   Anchor voice in the subject's own typographic environment where one
   exists: its documents, labels, signage, packaging, code, data, era or
   script. Run the swap test: replace the candidate with the platform default
   and inspect whether hierarchy, voice or recognition changes. No change is
   acceptable for a utility role; record it, do not decorate it.
```

Tabelle nach Zeile 104:

```markdown
| Tight-tracked geometric display sans with gradient fill on every heading | template scale replaced a role map; display treatment applied to body-level roles |
| Eyebrow label, display size or weight jump where no role changes | hierarchy signal applied by habit rather than by a distinction |
```

**5. colour-and-reproduction.md, Schritt 2, nach Zeile 39:**

```markdown
   Record each hue's origin as `supplied | incumbent | material | data |
   place | invented`. Invented hues need a named role. A trend set such as
   neon accents on near-black or a purple-to-blue gradient is not a role.
```

Kritikliste nach Zeile 81:

```markdown
- **Palette reads as a trend set rather than a system.** Likely cause: hues
  came from fashion or a generator and no role, material, incumbent or data
  origin is recorded. Rebuild the role map from subject origins before
  choosing new hues.
```

**6. imagery-and-art-direction.md, Zeilen 80-82 ersetzen und ergänzen:**

```markdown
- **Illustration or generated image feels AI-generic:** symbolic shorthand
  such as orb, sparkle, isometric city, floating abstract shapes or glossy
  blob characters, pseudo-detail, inconsistent construction, irrelevant
  ornament, derivative style markers, or unresolved hands, text and objects
  replaces a subject-specific visual idea. Counter-move: brief from the
  subject's real objects, place, process step, working hands, light and
  scale; reference by mechanism, never "in the style of".
- **Photograph reads as stock:** laughing team at laptop, handshake, pointing
  at whiteboard, skyline drone shot, tidy desk flat lay. Cause: selection by
  mood keyword with no image thesis. Counter-move: capture or commission the
  actual subject in its real context; if no real asset exists, declare the
  constructed mode and keep the brief subject-bound.
```

**7. ui-workflow-and-interaction-design.md, Zeilen 93-95 ersetzen:**

```markdown
- **Shell-first dashboard:** sidebar, four KPI tiles, one line chart and a
  table precede the task. Cause is missing object or decision hierarchy.
  Rebuild IA and task pattern from the most frequent and highest-consequence
  decision, not surface personality; the first screen shows the state the
  actor must act on.
```

**8. web-and-responsive-design.md, Kritikliste nach Zeile 98:**

```markdown
- **Template page stack:** hero, logo bar, three features, testimonial,
  pricing, CTA with identical section heights. Cause: page composed from a
  section library rather than from the audience's question order. Rebuild
  from argument order; let section length follow content consequence.
```

**9. brand-and-visual-systems.md, Zeilen 116-117 ergänzen:**

```markdown
- **Consistent but generic:** uniform styling exists without a subject-
  specific thesis or distinctive relationship. Counter-move: choose one owned
  relation derived from subject evidence, such as a product geometry, a
  process rhythm, a place, a word behaviour or a material, and rank it as
  the invariant; then run the removal test on the loudest borrowed cue.
```

**10. logo-and-identity-mark-design.md, Zeile 91 ergänzen:** nach "category cliché or trend" einfügen: `such as gradient orb, swoosh, abstract letter in a rounded square, infinite loop, leaf, spark or shield`.

**11. motion-and-sequence.md, Tabellenzeile 74 ersetzen und Schritt 1 ergänzen:**

```markdown
| Sequence feels like generic slides or a template site | repeated effect such as fade-up stagger, parallax or hover lift on every element; interchangeable frames; no subject-specific thesis or continuity carrier |
```

```markdown
   Derive the thesis from the subject's actual change: a process, a state
   transition, a physical behaviour, a data trend. Motion with no subject
   change to show is a candidate for removal.
```

**12. information-design-and-data-visualization.md, Tabelle nach Zeile 89:**

```markdown
| Dashboard reads as equal tiles, gauges and donuts | metric model absent; encoding taken from a dashboard library rather than decision, task and field semantics |
```

**13. style-direction.md, Kritikliste nach Zeile 117:**

```markdown
- **No named style, but the current default look:** mesh gradient, glass
  panels, rounded everything, sparkle motifs, isometric props. An unnamed
  direction collapsed to the tool or trend centroid. Treat it like a named
  label: choose a dominant lineage or a subject-derived structural cause and
  record it.
```

**14. concept-development-and-selection.md, nach Zeile 38:** Ein Verweis genügt, wenn das neue Modul kommt: `Each territory must bind at least one supplied or observed subject fact to its primary carrier; rate candidates on the specificity ladder and record the level.` Ohne neues Modul gehört die Leiter hierher.

## Verbesserungsplan für die übrigen Befunde

Jeder Punkt nennt die Änderung und die Prüfung.

- **Status-Vokabular (Befund 2).** Alle 28 Module auf einen Status `draft` setzen, `stub` und `retained-floor` streichen, die Definition in `SKILL.md:144-146` durch einen Satz ersetzen. Das Feld `evidence` bleibt und bekommt später Fixture-IDs aus einem repository-only Ordner mit Before/Control/After-Paaren je Modul. Prüfung: modules.yaml parst; Grep auf `stub` und `retained-floor` in Laufzeitdateien liefert null Treffer; Indexskript regeneriert ohne Labels.
- **Records skalieren (Befund 3).** In `SKILL.md` unter "Studio loop" ein Minimalprotokoll definieren: `concern | decision/status | evidence status`. Vollprotokoll nur bei Handoff, angefochtener Ausnahme oder Mehrdomänen-Befund. Jedes Modul ersetzt "Record:" durch "Record only fields that are open; otherwise use the Core minimal record". Prüfung: Trockenlauf mit drei Aufgaben unterschiedlicher Größe, Protokollumfang muss sichtbar skalieren.
- **Token-Budget (Befund 4).** Kern mit einem Tokenizer messen. Dann Kern kürzen: Ownership-Absätze zu Scoville UI und Scribe in ein Koordinationsmodul, den Design-Record-Absatz in `SKILL.md:133-140` ins Critique-Modul, Generierungskommentar beim Build aus der installierten Kopie entfernen. Erst danach `core_token_ceiling` auf Messwert plus Reserve setzen. Module über 200 Zeilen ebenfalls messen und `token_ceiling` sowie die Summen in `planned_common_loads` neu berechnen. Prüfung: Messwerte im Repository dokumentiert, jeder Wert unter seiner Decke.
- **Boilerplate deduplizieren (Befund 5).** Im Kern einen Absatz "Proof and claim ceiling" definieren. Jedes Modul endet nur noch mit zwei bis vier Zeilen: was es besitzt und welche Claims es zusätzlich ausschließt. Prüfung: Grep auf Phrasen wie "A convincing render" und "Do not claim" darf pro Phrase höchstens in Kern plus einem Modul treffen.
- **style-direction als Modus (Befund 6).** In `SKILL.md:39-40` und `brand-and-visual-systems.md:21-22` auf drei Modi reduzieren. Modul und Signale bleiben. Prüfung: Grep auf den Modus-Backtick-String liefert nur noch Modulverweise.
- **Schwester-Skills (Befund 7).** Optionales Modul `coordination-with-sibling-skills` mit definierter Schnittstelle: was Design an UI übergibt, was UI zurückgibt, was der Wording-Owner erhält. Kern behält einen Satz. Prüfung: Grep auf "Scoville UI" und "Scribe" trifft nur Kern-Satz, Koordinationsmodul und Quellenindex.
- **Jargon und Routing (Befund 8).** Sechs-Zeilen-Glossar im Kern für leaf, falsifier, claim ceiling und control. Routing-Zellen in `SKILL.md:74-80` als ganze Sätze umschreiben, etwa "Not sufficient alone: responsive pressure belongs to Web; strengths already working; geometry or labels fixed by a specialist; packaging panel hierarchy belongs to Packaging". Prüfung: Lesetest durch eine paketfremde Person, jeder Glossarbegriff wird konsistent verwendet.
- **Implizite Aktivierung (Befund 9).** In `agents/openai.yaml` den default_prompt auf "design, critique or repair" umstellen und Critique als reinen Lesemodus nennen. Beschreibung in `SKILL.md:3` um konkrete Auslöser kürzen. Implizite Aktivierung nur belassen, wenn ein Hosttest mit designfernen Prompts sie nicht auslöst. Prüfung: YAML parst, Hosttest dokumentiert.
- **Formale Hygiene.** Fünf Module mit Zeilenumbrüchen nach Status und Intervention versehen, neun Module Backticks um Quellen-IDs setzen. Britische Schreibweise festlegen, da "colour" in Modulnamen und Signal-Enum verankert ist; die Grep-Trefferliste zeigt rund 40 amerikanische Formen. Kleinbuchstaben an den beiden genannten Stellen korrigieren. C10 und C19 vergeben oder die Lücke im Kommentar erklären. Die 2025/2026-Quellen gegen den repository-only Ledger prüfen. Prüfung: Header-Grep mit einheitlichem Muster trifft alle 28 Module, Spelling-Grep auf `authorized|behavior|organization` liefert null Treffer.

Nichts wurde geändert. Alle Vorschläge liegen als Text vor und können in den genannten Dateien und Zeilen übernommen werden.

