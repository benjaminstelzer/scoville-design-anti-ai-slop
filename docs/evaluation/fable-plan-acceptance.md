# Fable plan acceptance

## Result

Accepted on 2026-09-04 in the same persisted Fable session
`7d03e896-c898-42a4-abee-b39d759bde77`. Requested model: `claude-fable-5-1`;
effort: `high`; resolved backend name not returned.
Both reviews resumed that session with Read/Grep/Glob only and no customizations
or external sources. The full plan, contract and Decision were supplied inline.
This is a plan-level review, not execution or release evidence.

The first review was not accepted and is retained in fable-plan-review-r1.json.
The revised plan addresses all eight required corrections and the three initial
recommendations; the full acceptance response is retained below and in
fable-plan-review-r2.json.

## Exact accepted documents

| Document | SHA-256 |
| --- | --- |
| docs/plans/0006-implement-fable-design-improvements.md | 4D3CA59A033F118B2D8963A19AFCA3A24B09BB533785429A0E11B15B51EBFBDC |
| docs/evaluation/fable-implementation-contract.md | 1F99646A6C9232250680C11617C86101495D06FD5257F50AB90E7E8B0F87C23A |
| docs/decisions/0055-plan-the-fable-design-successor.md | 2B24B9F82B50E366A38CD3EE32A75775C581BA49236E2B06E471FCB2EDFF3B77 |

## State and implementation notes

PLAN-0006 remains draft and all four Work Items remain todo. PROJECT_INDEX
remains idle. ADR-0055 records the user's selected planning direction under
the standing authorization to accept Decisions. No runtime change, model
design test, installation, commit, push, tag, release or publication occurred.

The accepted review includes three non-blocking implementation notes:
- Adapt the generator before the two-module route milestone; never create a
  temporary handwritten index.
- Preserve a Brief route for an open communication concern even if all brief
  fields were supplied.
- Add local-synthesis to the source index's class vocabulary as well as the
  new source entry and validator convention.

These are review notes, not an independent lifecycle owner. At implementation
start, incorporate the ordering clarification through the normal editable-todo
Plan operation before starting W-001. The other notes clarify the already
required complete routing and source-consistency outcomes. Keep the exact
approved hashes above as the acceptance receipt; do not retroactively replace
them with subsequent execution-plan or runtime hashes.

Native structural validation passed: 6 Plans, 35 Work Items, 55 Decisions,
0 errors and 0 warnings. This confirms record structure only.
Runtime source and installed-form review snapshot remain at package digest
`2D8718FF68019BA7D4AC21943F8A98D7823629B4B07C5BD7AE9EFFC06FE8D91B`.

## Full Fable acceptance

## Urteil: angenommen

Geprüft wurden die drei Dokumente in den gelieferten Fassungen mit den Hashes 4D3CA59A…, 1F99646A… und 2B24B9F8…. Alle acht notwendigen Korrekturen und die drei Empfehlungen aus meiner vorigen Prüfung sind sachgerecht eingearbeitet. Der Plan deckt meine Gestaltungshilfen und Verbesserungsvorschläge vollständig ab, ist konkret umsetzbar, und Reihenfolge und Prüfungen reichen für die geplanten Änderungen aus.

**Bestätigte Einarbeitung der Korrekturen**

- **Solo-Handoff:** Der Kern behält den Dreifelder-Record und trägt bedingt Quelle, Schutzconstraint und Unbekanntes. R06 und die W-001-Abnahme nennen den Solo-Fall ausdrücklich. Widerspruch beseitigt.
- **Provenienzreihenfolge:** Die Konvention `SRC-PACKAGE-LOCAL-SYNTHESIS` mit eigener Klasse wird in W-001 Schritt 2 vor jeder Validierung eingerichtet, W-003 prüft nur noch den Gehalt. Kein Kopf wartet auf W-003.
- **Katalogdatierung:** G01 ist auf den 2026-09-04 datiert, als Beispielauswahl gekennzeichnet und mit Recheck-Trigger versehen.
- **Evidenzsemantik:** Leere Liste bedeutet kein ausgeführter Beleg, nur echte W-004-Receipts dürfen eingetragen werden, und die Trennung von getestetem und annotiertem Manifest ist geregelt. Das ist genauer als mein Vorschlag.
- **Fall 7 und named_style:** Beide sind in W-004 enthalten und in der Abnahme verankert.
- **Dispositionen und Konsumenten:** Die drei Werte sind festgelegt, Zurückstellungen erfordern eine Scope-Entscheidung, und die Mindestliste der Moduskonsumenten entspricht meiner.
- **Teilung, Kommunikationsrecord, Hostlane:** W-001 und W-002 sind getrennt mit Meilenstein vor den Craft-Ergänzungen, der erweiterte Kommunikationsrecord geht an Brief, und eine unverfügbare Hostlane blockiert den Abschluss von W-004 ausdrücklich.

**Hinweise für die Umsetzung, nicht abnahmerelevant**

- **Generator vor Meilenstein.** W-001 Schritt 5 soll die direkte Routbarkeit beider neuen Module belegen. Dazu muss der generierte Index sie bereits enthalten. Die Generatoranpassung aus Schritt 6 sollte daher vor Schritt 5 laufen, sonst droht ein handgeschriebener Zwischenindex, den der Vertrag verbietet. Die Abnahmekriterien erzwingen den richtigen Endzustand, die Schrittfolge sollte ihn aber nicht behindern.
- **Ladebedingung von Brief.** `brief-framing-and-criteria.md:11` schließt vollständige Briefs aus. Wenn der Kommunikationsrecord dorthin wandert, muss die Ladebedingung einen offenen Kommunikationsbelang wie Fehllesungsrisiko oder Modalrelation ausdrücklich nennen, damit ein vollständiger Brief mit materiellem Kommunikationsrisiko das Modul noch erreicht.
- **Klassenliste im Quellenindex.** `source-index.md:22-23` zählt die zulässigen Quellklassen auf. Die neue Klasse local-synthesis muss dort ergänzt werden, sonst widerspricht der Index seiner eigenen Definition.

**Grenzen dieses Urteils**

Die Abnahme bestätigt Treue zu meinen Vorschlägen, Umsetzbarkeit und Hinlänglichkeit der Prüfungen auf Planebene. Sie ist kein Beleg für Wirksamkeit, kein Start der Umsetzung und keine Freigabe für Installation oder Veröffentlichung. Die angesetzten Hosttests, Paarvergleiche und Quellenprüfungen sind geplante Arbeit, deren Ergebnisse erst W-004 liefert. Die Aufnahme von ADR-0055 als accepted ist eine Nutzerentscheidung, die ich nur zur Kenntnis nehme.

