# Scoville Design: Audit der praktischen Gestaltungshilfen

Datum: 5. September 2026 · Status: abgeschlossener Inhaltsaudit, Ergänzungen vorgeschlagen

## Ergebnis

Scoville Design hat eine breite fachliche Grundlage. Die wesentlichen Themen sind vorhanden: Hierarchie, Gruppierung, Weißraum, Rhythmus, Schriftwahl und -kombination, Mikrotypografie, Farbrelationen, Bildregie, Informationsdarstellung, Medienanpassung, Identität, Bewegung und Produktion. Auch Diagnose, Reparatur, Ausnahmen und Nachweisgrenzen sind überwiegend ausdrücklich beschrieben.

**Der größte Ergänzungsbedarf liegt in der Übersetzung von Fachbegriffen und Prüfkriterien in konkrete Entwurfsverfahren.** Häufig steht bereits, welche Variablen zu untersuchen sind. Weniger häufig zeigt das Modul anhand eines kleinen Vergleichs, welche Variable bei welchem Befund wie geändert wird und woran die Entscheidung anschließend zu beurteilen ist.

Das ist keine pauschale Feststellung fehlenden Designwissens. Es sind drei unterschiedliche Befunde:

- **Nicht ausgearbeitete Technik:** etwa Kurvenkonstruktion, optischer Formausgleich oder der Aufbau einer Palette in konkreten Schritten.
- **Vorhandene Regel mit zu wenig Anwendungshilfe:** etwa gekoppelter Textsatz, Rasterableitung oder Auswahl responsiver Transformationen.
- **Ausreichend abgedeckter Zweck:** insbesondere bei Quellen, Rechten, Darstellungsschutz und Zusammenarbeit. Hier rechtfertigt die bloße Möglichkeit weiterer Beispiele keine zusätzliche Pflichtregel.

Für die 30 Fachmodule ergibt die redaktionelle Priorisierung **11 P1-Kandidaten, 12 P2-Kandidaten und 7 Module ohne begründeten Erweiterungsbedarf**. Der Core hat einen eigenen P2-Befund. P1 bezeichnet hier die erste Ausbaustufe praktischer Hilfen, keinen nachgewiesenen Laufzeitfehler oder Releaseblocker. Einen neuen P0-Befund hat dieser Audit nicht festgestellt; eine vollständige Complianceprüfung ist damit nicht verbunden.

Die erste Ausbaustufe sollte Typografie, Komposition und Farbe vertiefen. Danach folgen Form- und Bildkonstruktion sowie Auswahlhilfen für Informationsdarstellung, responsive Gestaltung und Bewegung. Zusätzliche Verbote, ein größerer Trendkatalog oder neue Module allein würden diesen Bedarf nicht lösen.

## Prüfstand und Methode

Untersucht wurde die lokale kanonische Skillquelle unter `Z:\Projekts\AI\scoville-design-anti-ai-slop\scoville-design-anti-ai-slop`:

- Git-Stand des Repositorys: `b5a824bfe844c363be363aa4c1eca605e3340cb3`.
- Vollständig gelesen: `SKILL.md` und alle 30 direkt gerouteten Fachmodule.
- Zusätzlich geprüft: Modulmetadaten, die Einleitung und Nachweisgrenzen des nicht gerouteten Quellenindex, bestehende Forschungsmethode und Priorisierung, ein historischer Kompositionsaudit, der aktive Plan und die relevante Entscheidung zur Abstands- und Medienzuständigkeit.
- Der gelesene installierte Core stimmt per SHA-256 mit dem Repository-Core überein: `F0D6DC581866E095950DCA728DF66D885987DFC29F786AD1BE2925F9BB9939B9`. Ein vollständiger Installationsabgleich aller Fachmodule war nicht Teil des Audits.
- Ergänzende Primärquellen wurden am 5. September 2026 in den unten genannten Abschnitten geöffnet und textlich geprüft. Fremde Abbildungen wurden nicht übernommen oder als visuell geprüft ausgegeben.

Pro Modul wurden vorhandenes Wissen, praktische Lücke, kleinstmögliche Ergänzung, Zuständigkeit und ein möglicher widerlegender Test betrachtet. Fehlende Stichwörter allein gelten nicht als Lücke. Eine bereits im zuständigen Nachbarmodul enthaltene Regel soll nicht erneut eingebaut werden.

**Nachweisgrenze:** Dies ist eine Quelltext- und Lehrbarkeitsprüfung durch einen Reviewer mit gezieltem Quellenabgleich. Keine neuen Modellvergleiche, Nutzerstudien, Renderexperimente oder unabhängigen Zweitreviews wurden durchgeführt. Das Fehlen einer expliziten Anleitung ist aus dem Text feststellbar. Ob ein konkretes Modell sie benötigt und ob sie seine Ergebnisse verbessert, bleibt eine zu prüfende Hypothese. Alle nachfolgenden Prüffälle sind vorgeschlagen, nicht ausgeführt.

Die historischen W-011-Audits betreffen einen älteren Zuschnitt und teilweise wesentlich kürzere Referenzen. Ihre damaligen Lücken wurden nicht als aktuelle Befunde übernommen. Insbesondere sind die Trennung von Raster und CSS, Medienzuständigkeiten sowie viele Satzdetails inzwischen vorhanden.

Der aktive `PLAN-0006` führt `W-004` als `paused`. Dessen nächste Aktion betrifft die Auswertung der vorhandenen Terra-Host-Ergebnisse und den fehlenden Composition-Read in DH5; außerdem bleibt der dort benannte abschließende Fable-Review offen. Dieser Audit bewertet oder ersetzt diese Ergebnisbelege nicht und verändert weder Plan noch Acceptance. Bei der Bestandsprüfung wurden keine als `proposed` markierten Decision-Dateien gefunden.

## Prioritäten und Befundarten

| Kürzel | Bedeutung in diesem Audit |
| --- | --- |
| P1 | Praktisches Verfahren im bestehenden Fachumfang zuerst vertiefen; Nutzen anschließend prüfen. |
| P2 | Sinnvolle Anwendungshilfe oder Präzisierung, nachrangig gegenüber den gestalterischen Grundlagen. |
| Bestand | Keine ausreichend begründete neue Regel für den Modulzweck gefunden. |
| T | Technik im aktuellen Text nicht als ausführbares Verfahren ausgearbeitet. |
| A | Regel vorhanden, Anwendung oder Abwägung könnte konkreter werden. |

Die Sicherheit der Textbeobachtung ist hoch, soweit eine konkrete Stelle angegeben wird. Die erwartete Wirkung einer Ergänzung ist eine fachliche Einschätzung mit noch ausstehendem Verhaltenstest. Priorität, Schwere eines Fehlers und Sicherheit einer Wirkungsbehauptung sind unterschiedliche Größen.

## Modulübersicht

| Nr. | Modul-ID | Ergebnis | Größter praktischer Hebel |
| --- | --- | --- | --- |
| 01 | brief-framing-and-criteria | P2 · A | Ein ausgefüllter Weg von Auftrag zu entscheidbarer Gestaltungsfrage |
| 02 | concept-development-and-selection | P2 · A | Inhaltliche Mechanismen am gleichen Brief sichtbar unterscheiden |
| 03 | composition-and-layout | P1 · A | Rasterableitung, visuelle Gewichte und relationale Abstandsprobe |
| 04 | typography-and-typesetting | P1 · A | Satz- und Schriftvergleich mit konkreten Eingriffen |
| 05 | font-technology-and-script-safety | P2 · A | Kleines ausgefülltes Prüfblatt statt weiterer Variablen |
| 06 | colour-and-reproduction | P1 · T/A | Rollenpalette tatsächlich aufbauen und im Layout abstimmen |
| 07 | imagery-and-art-direction | P1 · T/A | Licht, Perspektive, Illustration und Beschnitt praktisch diagnostizieren |
| 08 | information-design-and-data-visualization | P1 · A | Aufgabe–Darstellungsform-Auswahl mit Gegenfällen |
| 09 | cartography-and-spatial-data | P2 · A | Kartenbeschriftung und Generalisierung im Maßstabswechsel |
| 10 | diagrams-and-relational-information | P1 · A | Topologie in eine nachvollziehbare Geometrie übersetzen |
| 11 | brand-and-visual-systems | P1 · T/A | Icon- und Mustersysteme konstruktiv ausarbeiten |
| 12 | logo-and-identity-mark-design | P1 · T/A | Kurven, Binnenformen und optische Varianten bearbeiten |
| 13 | instructional-and-explanatory-design | P2 · A | Durchgearbeitetes Beispiel, Gegenbeispiel und Transferaufgabe |
| 14 | advertising-and-campaign-art-direction | P2 · A | Proposition und rhetorische Bildoperation an einem Fall vergleichen |
| 15 | ui-workflow-and-interaction-design | P2 · A | Interaktionsmuster anhand konkreter Entscheidungskosten wählen |
| 16 | web-and-responsive-design | P1 · A | Drucksymptom–Transformation–Gegenfall als Auswahlhilfe |
| 17 | editorial-and-fixed-media-design | P1 · A | Unterschiedliche Medienjobs und einen Flatplan ausarbeiten |
| 18 | packaging-graphics-and-sku-systems | P2 · A | SKU-Unterscheidung und Panelgraph ausgefüllt zeigen |
| 19 | physical-wayfinding-and-signage-systems | P2 · A | Entscheidungspunkt, Pfeilbezug und Bestätigung konkret verbinden |
| 20 | motion-and-sequence | P1 · T/A | Verlauf, Tempo und zeitliche Staffelung auswählen |
| 21 | media-production-and-handoff | P2 · A | Produktionsfragen und einen kompakten Liefernachweis vormachen |
| 22 | critique-and-validation | P2 · A | Beobachtung, Ursache und Reparatur an Gegenbeispielen kalibrieren |
| 23 | culture-and-representation | Bestand | Bestehende kontextspezifische Autoritätsprüfung erhalten |
| 24 | people-privacy-and-media-integrity | Bestand | Vorhandene Medienmodi und Ableitungsprüfung erhalten |
| 25 | sustainability-claims | Bestand | Vorhandene Prüfung der visuellen Gesamtaussage erhalten |
| 26 | source-verification-and-evidence | Bestand | Vorhandene Anspruch–Quelle-Beziehungen erhalten |
| 27 | asset-rights-and-attribution | Bestand | Vorhandene nutzungsspezifische Rechte- und Creditprüfung erhalten |
| 28 | style-direction | P2 · A | Eine Stilrelation vom Quellenbefund in zwei Medien übersetzen |
| 29 | generic-signatures-and-subject-specificity | Bestand | Bereits konkrete Ursachen, legitime Fälle und Gegenmaßnahmen |
| 30 | coordination-with-sibling-skills | Bestand | Bereits ausreichender, schlanker Austauschvertrag |

## Detailaudit

### Core · P2 · A

**Beleg:** [SKILL.md](../../../scoville-design-anti-ai-slop/SKILL.md), Abschnitte „Studio loop“ und „Rules, exceptions and proof ceiling“.

**Vorhanden:** Ein vollständiger Ablauf von Framing über Auswahl und Ausführung bis zu Sichtprüfung und Reparatur. Er verlangt echte Inhalte, relevante Fachmodule, begründete Ausnahmen und angemessene Nachweise. Mehrere Richtungen sind bei offener Konzeptauswahl bereits vorgesehen.

**Lücke:** Es fehlt ein leicht erkennbares Format für die Anwendung einer einzelnen gestalterischen Heuristik. Der Agent kann eine Regel befolgen, ohne den entscheidenden Vergleich konkret zu machen.

**Ergänzung:** Bei einer schwierigen offenen Handwerksentscheidung eine kurze Arbeitsprobe verwenden: `Situation → veränderbare Beziehung → Eingriff → erhaltene Stärke → Gegenfall → Sichtprüfung`. Kein zusätzliches Pflichtdokument und keine Vergleichspflicht für jede Kleinigkeit. Die eigentliche Technik bleibt im Fachmodul.

**Prüffall:** Ein kleiner Absatzabstandsfehler soll zu einer lokalen Probe führen, ohne vollständiges Briefing oder Variantenproduktion. Ein schwieriger Schriftvergleich soll dagegen tatsächlich im gesetzten Text stattfinden. Das ist eine lokale methodische Empfehlung, kein extern nachgewiesenes Universalverfahren.

### 01 · brief-framing-and-criteria · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/brief-framing-and-criteria.md), Z. 16–79.

**Vorhanden:** Stilfreies Framing, genaue Inhalte, Autorität, Kommunikationsbarrieren sowie harte Bedingungen und vergleichende Kriterien. Das ist inhaltlich ausreichend.

**Lücke:** Die vielen Felder zeigen noch nicht, wie aus einem vagen Auftrag eine handhabbare visuelle Frage wird. Besonders wichtig ist die Trennung zwischen unbekannter Zielgruppenannahme und tatsächlich geliefertem Nutzungskontext.

**Ergänzung:** Ein kurzes, ausdrücklich konstruiertes Beispiel: Aus „Veranstaltungsplakat“ werden zuerst Informationspriorität und Erkennungssituation, danach die offene Hierarchieentscheidung. Zeigen, welche Information entscheidend fehlt und welche für einen ersten Entwurf entbehrlich ist. Keine zusätzliche Persona-Methode und kein neues Frageschema.

**Prüffall:** Der Agent konkretisiert einen unvollständigen Auftrag, ohne Publikumseigenschaften zu erfinden oder mit einer Font-/Farbentscheidung vorzugreifen. Grundlage der Empfehlung ist das bereits vorhandene Frame-Verfahren.

### 02 · concept-development-and-selection · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/concept-development-and-selection.md), Z. 14–87.

**Vorhanden:** Viele mögliche Bedeutungsträger, Vergleich kausal verschiedener Mechanismen, gleiche Inhalte und gleicher Ausarbeitungsgrad. Bloße Font-/Farbvarianten werden schon ausgeschlossen.

**Lücke:** „Mechanismus“ und „Carrier“ bleiben trotz guter Definition anspruchsvolle Abstraktionen. Ein Satz verschiedener Konzeptnamen beweist noch keine gestalterische Differenz.

**Ergänzung:** Einen gemeinsamen, fiktiven Brief in wenige vergleichbare Rohideen übersetzen: etwa direkte Demonstration, Vorher-Nachher-Kontrast und schrittweise Enthüllung. Jeweils die sichtbare Inhaltsbeziehung sowie eine nur kosmetisch abweichende Nicht-Alternative markieren. Keine feste Zahl von Konzepten als Laufzeitpflicht.

**Prüffall:** Der Agent verwirft eine anders eingefärbte Wiederholung, erhält aber eine nüchterne direkte Darstellung, wenn sie die Aufgabe trägt. Die Ergänzung erläutert vorhandene Regeln; sie begründet keinen neuen Kreativitätsstandard.

### 03 · composition-and-layout · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/composition-and-layout.md), Z. 41–103 und 117–129.

**Vorhanden:** Semantische Abstände, Gestaltkonflikte, negative Räume, optische gegenüber geometrischen Beziehungen, Rhythmus, Raster und kausale Reparaturreihenfolge. Diese Themen fehlen ausdrücklich nicht.

**Lücke:** Raster und visuelles Gleichgewicht werden gut eingefordert, aber kaum aus einem konkreten Inhaltssatz hergeleitet. Die Änderung von Größe, Kontrast, Dichte oder Position als alternative Eingriffe könnte greifbarer werden.

**Ergänzung:** Zwei kompakte Hilfen: erstens Rasterkandidaten aus Textmaß, Bildverhältnis, wiederkehrenden Einheiten und nutzbarer Fläche konstruieren; zweitens einseitiges Gewicht zunächst als Massen-, Kontrast- oder Gruppierungsproblem unterscheiden. Symmetrie, Achse, modulare Ordnung und freiere Anordnung als mögliche Organisationsformen erklären, jeweils mit Gegenfall. BCcampus bietet dafür ein fachliches Vokabular und unterscheidet Organisationssysteme; daraus folgt kein universell bestes Raster. [Q1](#quellenabgleich)

**Prüffall:** Gleicher Inhalt in einer dichten und einer ruhigen Komposition. Die Reparatur soll die gewählte Dichte erhalten und die konkrete Beziehung verbessern, statt alles zu zentrieren oder zu vergrößern.

### 04 · typography-and-typesetting · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/typography-and-typesetting.md), Z. 38–94 und 119–142.

**Vorhanden:** Rollen vor Schriften, kombinatorische Kriterien, tatsächliche Schriftmerkmale, Schriftanzahl als Ergebnis, Kerning/Tracking/Wortabstand, gekoppelter Textsatz, Details, Umbruch und lateinischer Schwerpunkt.

**Lücke:** Der Agent erhält viele Prüfmerkmale, aber keine ausgearbeitete Satzprobe, die aus einem Befund einen bestimmten Eingriff ableitet. Auch „optisch vergleichen“ könnte zwischen gleicher nomineller Größe und gleicher wahrgenommener Größe unterscheiden.

**Ergänzung:** Einen realtextnahen Prüfsatz mit Headline, Absatz, Zahlen und kritischen Zeichen verwenden. Die zunächst festgehaltenen Variablen nennen; dann beispielsweise nur Maß und anschließend gegebenenfalls Durchschuss verändern. Beim Schriftpaar Hierarchie und Textur prüfen; eine Schrift mit größerer x-Höhe nicht allein wegen gleicher Punktzahl als gleich groß behandeln. Als getrennte Vergleichsfrage ist eine optisch angeglichene Probe zulässig.

Buttericks Werte von 45–90 Zeichen und 120–145 Prozent Zeilenabstand eignen sich als ausdrücklich autorenbezogene Vergleichsbereiche für passenden Fließtext, nicht als universelle Qualitätsgrenzen oder Pflichtwerte. [Q2, Q3](#quellenabgleich)

**Prüffall:** Langer deutscher Fließtext plus kurze Displayzeile. Der Agent muss unterschiedliche Satzprobleme unterscheiden und darf weder die Displaybehandlung auf Fließtext ausdehnen noch eine exakte Kopie zugunsten schöner Umbrüche umschreiben.

### 05 · font-technology-and-script-safety · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/font-technology-and-script-safety.md), Z. 40–78 und 125–151.

**Vorhanden:** Konkrete Fontdateien, Repertoire, Shaping, Features, Achsen, Fallbackmetriken, Bidi, vertikaler Satz, Embedding sowie eine angemessene Grenze zur sprachlichen Fachprüfung.

**Lücke:** Kein wesentlicher weiterer Regelbereich. Praktisch fehlt eher eine ausgefüllte kleine Probe: String, erwartete Eigenschaft, tatsächlich genutzter Font, Renderer und Ergebnis.

**Ergänzung:** Eine exemplarische Fallbackprüfung mit einem fehlenden Zeichen und verändertem Umbruch. Technische Abdeckung, korrektes Shaping und sprachlich angemessene Form als drei getrennte Befunde zeigen. Werkzeugbefehle bleiben beim tatsächlichen Implementierungswerkzeug und seiner aktuellen Dokumentation.

**Prüffall:** Ein vorhandener Codepunkt darf nicht als Beleg korrekter Schriftform gelten; ein Fallback muss im tatsächlich gelieferten Kontext geprüft werden. Ein Ausbau zu einem weltweiten Schriftgestaltungslehrgang ist durch diesen Audit nicht begründet.

### 06 · colour-and-reproduction · P1 · T/A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/colour-and-reproduction.md), Z. 15–65 und 98–133.

**Vorhanden:** Rollen, Farbherkunft, Helligkeit/Chroma/Hue, Flächenanteil und Nachbarschaft, Redundanz, Datenfarben, Zustände und Produktionskette. Farbharmonie wird bereits korrekt als mögliche Vergleichshilfe behandelt.

**Lücke:** Der Weg vom Rollenplan zu einer brauchbaren neuen Palette bleibt kurz. Es fehlen eine konkrete Abstimmungsfolge und ein Beispiel, bei dem die gleiche Palette wegen anderer Flächenanteile oder Umgebung anders funktioniert.

**Ergänzung:** Palette zuerst im tatsächlichen Layout testen: tragende Hell-Dunkel-Verhältnisse, neutrale Flächen, Funktions-/Identitätsfarbe, anschließend Chroma und Akzentfläche abstimmen. Bei Daten eine sequenzielle Rampe auf nachvollziehbare Helligkeitsentwicklung prüfen; bei Kategorien eine bedeutungslose Rangfolge vermeiden. Ein perzeptueller Farbraum kann als Arbeitsmittel erklärt werden, ohne ihn zum Stil oder zur Pflichttechnik zu machen. [Q4](#quellenabgleich)

**Prüffall:** Gleiche Farbwerte als kleine Swatches und als große Layoutflächen vergleichen; eine sichtbare Konkurrenz durch Flächen- oder Chromaänderung reparieren. Keine pauschale 60/30/10-Regel und keine Farbpsychologie nach Kulturklischee.

### 07 · imagery-and-art-direction · P1 · T/A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/imagery-and-art-direction.md), Z. 27–62 und 64–104.

**Vorhanden:** Licht, Perspektive, Geste, Fokus, Bildmodus, Illustrationseigenschaften, Kontaktbogen, Beschnitt und durchgängige Bildregie sind genannt. Das Modul besteht keineswegs nur aus Bildgenerierungs-Prompts.

**Lücke:** Viele bildnerische Größen bleiben eine Inventarliste. Wie man etwa Silhouette, Wertestruktur, Überschneidung, Perspektive oder Lichtrelation zur Diagnose nutzt, ist weniger ausgearbeitet. Fotografie und Illustration teilen sich einen sehr allgemeinen Erzeugungsablauf.

**Ergänzung:** Zwei kurze bedingte Zweige. Fotografie: tatsächlichen Standort/Blickwinkel, Beleuchtung, Fokus und Hintergrund auf den Bildjob beziehen; störende Trennung oder Überschneidung gezielt reparieren. Illustration: vom identifizierbaren Umriss über große Formen/Werte zu Details gehen; Perspektive und Licht konsistent halten, wenn der gewählte Modus sie beansprucht. Für expressive flache oder widersprüchliche Systeme einen legitimen Gegenfall zeigen. IBM liefert konkrete Beispiele für Abstraktion, Maßstab, Detailgrad und Bildregie; seine Markenregeln bleiben IBM-spezifisch. [Q5, Q6](#quellenabgleich)

**Prüffall:** Eine dekorativ attraktive, aber unklare Produktillustration und ein kontextschädigender Fotobeschnitt. Der Agent soll jeweils eine andere Ursache und Maßnahme wählen.

### 08 · information-design-and-data-visualization · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/information-design-and-data-visualization.md), Z. 42–76.

**Vorhanden:** Aufgaben und Variablentypen, Tabelle versus Chart, Nullpunkt-/Skalensemantik, Unsicherheit, fehlende Werte, Dashboardmodell und alternative Datenpfade.

**Lücke:** Aufgaben wie Rangfolge, Verteilung oder Abweichung werden aufgezählt; eine kompakte Zuordnung zu tatsächlich vergleichbaren Darstellungen fehlt. Der Agent muss den entscheidenden nächsten Schritt weitgehend selbst liefern.

**Ergänzung:** Auswahlhilfe `Frage → Kandidat → Stärke → typische Fehlverwendung → Kontrollform`. Beispielsweise Kategorienvergleich mit Balken/Punkten; zeitliche Entwicklung mit Linie; exakter Einzelwertvergleich mit Tabelle; viele vergleichbare Serien gegebenenfalls als kleine Mehrfachdiagramme. Nullpunkt, kontinuierliche Verbindung und fehlende Werte bei jeder Form erhalten. ONS zeigt diese aufgabenbezogene Organisation mit Beispielen; Datawrapper konkretisiert Unterschiede innerhalb zeitlicher Darstellungen. Das sind Ausgangspunkte, keine erschöpfende Chart-Taxonomie. [Q7, Q8](#quellenabgleich)

**Prüffall:** Der gleiche Datensatz soll je nach Frage zu unterschiedlichen geeigneten Darstellungen führen. Ein verbindendes Liniendiagramm für ungeordnete Kategorien muss begründet verworfen werden; eine legitime Linie darf bleiben.

### 09 · cartography-and-spatial-data · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/cartography-and-spatial-data.md), Z. 39–86.

**Vorhanden:** Kartenbedarf, Projektion, Ausdehnung, Normierung, Klassifikation, räumliche Schlussfolgerungen, Autorität, sensible Orte und Lesesystem.

**Lücke:** Beschriftung und Generalisierung haben gegenüber Daten- und Autoritätsfragen wenig operative Tiefe. „Labels koordinieren“ sagt noch nicht, wie eine Kollision oder ein verschwundener kleiner Ort repariert wird.

**Ergänzung:** Ein Maßstabsbeispiel mit wichtiger und nachrangiger Beschriftung: erst Priorität und kartografische Darstellung prüfen, dann Position, Versatz mit eindeutiger Zuordnung, Detailansicht oder Inset vergleichen. Punkt-, Linien- und Flächenbeschriftung unterscheiden. Keine neuen universellen Mindestabstände oder unterstellten GIS-Fakten.

**Prüffall:** Beim Verkleinern müssen kritische Orte/Relationen auffindbar bleiben und Beschriftungen eindeutig zugeordnet sein. Diese konkrete Reparaturhilfe ist hier eine lokale Empfehlung; die kartografischen Detailkonventionen benötigen vor Aufnahme einen gezielten fachlichen Quellenabgleich.

### 10 · diagrams-and-relational-information · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/diagrams-and-relational-information.md), Z. 35–61 und 81–91.

**Vorhanden:** Ein starkes Modell von Knoten, Kanten, Richtung, Kardinalität, Containment, Ansichten und semantischer Gleichheit.

**Lücke:** Der Übergang zur Geometrie umfasst im Wesentlichen allgemeine Aufforderungen zu Anordnung und Kantenführung. Die Wahl zwischen hierarchischer, radialer, zeitlicher oder netzwerkbezogener Anordnung wird nicht praktisch demonstriert.

**Ergänzung:** Eine kleine Auswahltafel für die Frage der Darstellung, ergänzt um einen Routingfall mit Ein-/Ausgangspunkten, Kantenbeschriftung, Rückkante und Kreuzung. Ein gerichtet geschichteter Entwurf kann Prozessordnung tragen; andere Topologien benötigen andere Vergleiche. Graphviz dokumentiert verschiedene Layoutfamilien, beweist aber weder ihre Verständlichkeit noch die fachliche Wahrheit eines Diagramms. [Q9](#quellenabgleich)

**Prüffall:** Einen kritischen Pfad in einem identischen Knoten-/Kantenmodell besser verfolgbar machen, ohne Kanten zu löschen, Eigentümerschaft zu erfinden oder Rückbeziehungen zu verstecken. Automatische Layouts dürfen Kandidaten liefern, aber keine Designabnahme ersetzen.

### 11 · brand-and-visual-systems · P1 · T/A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/brand-and-visual-systems.md), Z. 79–116, besonders Z. 97–100.

**Vorhanden:** Sehr ausführliche Identitätsautorität, Invarianten/Variablen, Architektur, Governance und Icon-Familienmerkmale. Icons, Piktogramme und grafische Muster sind schon dem System zugeordnet.

**Lücke:** Die eigentliche Konstruktion einer Icon-Familie ist auf wenige Zeilen verdichtet. Auch ein grafisches Muster wird als Systemelement genannt, ohne die Ableitung eines Motivs und seiner Wiederholung zu zeigen.

**Ergänzung:** Optisches Familienblatt mit unterschiedlich proportionierten Formen: gemeinsame Grundformen, visuelles Gewicht, Innenräume, Strich-/Flächenlogik, Detailstufen und Zeichenbedeutung prüfen. Bei Mustern Motiv, Wiederholung, Dichte und Randverhalten aus der Identitätsrelation ableiten. IBM zeigt konkrete Keyshape- und Gewichtsanleitungen; seine Rasterwerte, Winkel und Plex-bezogenen Formen sind keine allgemeinen Scoville-Vorgaben. [Q10](#quellenabgleich)

**Prüffall:** Eine schmale, eine runde und eine komplexe Form sollen als Familie funktionieren, ohne identische Bounding-Box-Ausfüllung zu erzwingen. Die Aussage bleibt Formkonsistenz im geprüften Satz, nicht erwiesene Symbolverständlichkeit.

### 12 · logo-and-identity-mark-design · P1 · T/A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/logo-and-identity-mark-design.md), Z. 45–92 und 137–172.

**Vorhanden:** Mechanismen, Figur/Grund, Silhouette, Binnenräume, Anschlüsse, Wortmarkenrhythmus und optische Varianten. Ein-Farb- und Kleinformatprüfungen sind bereits ausdrücklich enthalten.

**Lücke:** „Optisch korrigieren“ und „als zusammenhängende Form zeichnen“ liefern kaum konkrete Konstruktionstechniken. Ankerpunkte, Griffe, Kurvenanschlüsse und die Diagnose einer unruhigen Kontur sind nicht ausgearbeitet.

**Ergänzung:** Eine kurze Formkorrekturprobe: Kontur isolieren; beabsichtigte Ecke oder glatten Anschluss unterscheiden; Tangentenrichtung und Griffwirkung prüfen; unnötige lokale Wendungen beseitigen; anschließend Füllung, Negativform und Zielgröße vergleichen. Optischen Größenausgleich und unterschiedliche positive/negative Gewichtswirkung als zu prüfende Fälle erläutern. Adobe belegt die konkrete Arbeit mit Kurven und Griffen; Logoqualität und optische Entscheidungen sind eine weitergehende lokale Synthese. [Q11](#quellenabgleich)

**Prüffall:** Ein formal akzeptierter Markentwurf mit holprigem Anschluss soll präziser werden, ohne seinen Mechanismus zu ersetzen. Keine Kreisraster-Begründung als Qualitätsbeweis und kein neuer universeller Mindestgrößenwert.

### 13 · instructional-and-explanatory-design · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/instructional-and-explanatory-design.md), Z. 43–85, 87–127 und 150–166.

**Vorhanden:** Lernziel, Fehlvorstellung, Modell, Modalitätsverteilung, Referenten, Segmentierung, Checks, Warnketten, Gegenbeispiele und Transfer. Worked Examples werden bereits genannt.

**Lücke:** Ein Beispiel für die Ausführung dieses Verfahrens fehlt. Die Begriffe sollten nicht einfach erneut in eine längere Liste aufgenommen werden.

**Ergänzung:** Ein harmloses, vollständig geliefertes Sachmodell als korrektes Beispiel, plausibles Fehlbeispiel und neue Transferaufgabe darstellen. Sichtbar machen, welche Beschriftung oder räumliche Relation die entscheidende Unterscheidung trägt. Lernvoraussetzungen als gegeben oder unbekannt markieren.

**Prüffall:** Das Modell kann am neuen Fall richtig angewendet werden; bloßes Wiedererkennen der ersten Abbildung reicht nicht. Hier wird ein bereits vorhandener Testgedanke konkretisiert, keine neue pauschale Theorie des Lernens eingeführt.

### 14 · advertising-and-campaign-art-direction · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/advertising-and-campaign-art-direction.md), Z. 49–93.

**Vorhanden:** Ein reichhaltiger Katalog rhetorischer Möglichkeiten, funktionale Bild-/Textbeziehungen, Markenerkennung, Gesamtaussage, Platzierungsvarianten und kontrollierte Vergleiche.

**Lücke:** Die rhetorischen Operationen sind ausführlich benannt, aber an keiner identischen Proposition durchgespielt. Das lädt zu gut klingenden Konzeptbeschreibungen ein, deren sichtbare Unterschiede ungeklärt bleiben.

**Ergänzung:** Eine ausdrücklich fiktive, als Testeingabe festgelegte Produkteigenschaft als direkte Demonstration und als visuelle Analogie zeigen. Die Analogie auf unerwünschte Zusatzbehauptungen prüfen. Einen legitimen wörtlichen Ansatz erhalten. Für die spätere Ausführung exakt gelieferte Qualifikationen verwenden.

**Prüffall:** Aufmerksamkeit, Produktzuordnung und inhaltliche Aussage getrennt beurteilen. Kein Klick-/Conversiongewinn aus einem gelungenen Entwurf ableiten. Neue Marketingstrategien oder Medienkaufregeln gehören nicht in diese Ergänzung.

### 15 · ui-workflow-and-interaction-design · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/ui-workflow-and-interaction-design.md), Z. 39–89.

**Vorhanden:** Informationsarchitektur, Navigation, Taskflow, Formulardaten, Zustand, Wiederaufnahme, Fehlertypen und Systemeigentum sind stark abgedeckt.

**Lücke:** Das Modul verlangt Mustervergleiche nach Nutzungshäufigkeit, Risiko und Wiederherstellung, zeigt aber keinen konkreten Vergleich verwandter Muster.

**Ergänzung:** Ein kleiner Fall für direkte Bearbeitung gegenüber separater Detailansicht: Sicht auf Kontext, Vergleichsbedarf, Häufigkeit, Unterbrechung und Rückweg gegeneinander abwägen. Ein zweiter Gegenfall kann zeigen, warum dieselbe Wahl bei einem anderen Task scheitert. Frameworkkomponenten und Implementierungsmechanik bleiben beim UI-Owner.

**Prüffall:** Zwei Aufgaben mit denselben Daten, aber anderem Vergleichs- und Bearbeitungsbedarf dürfen unterschiedliche Muster ergeben. Keine maximale Klickzahl, Menüpunktzahl oder generelle Modalregel einführen. Dies ist eine lokale Anwendungshilfe für den bereits vorhandenen Kriterienkatalog.

### 16 · web-and-responsive-design · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/web-and-responsive-design.md), Z. 16–71.

**Vorhanden:** Inhaltlicher Druck statt Gerätevorgabe, ausführliche Transformationsoperatoren, priorisierte Beziehungen, echte Inhalte und Prüfung von Zwischenbreiten.

**Lücke:** Es fehlt die kurze Auswahlhilfe, welcher Operator welches sichtbare Problem behebt und welche Information dabei gefährdet ist. Die Operatorliste allein verhindert beispielsweise kein unnötiges Disclosure.

**Ergänzung:** `zu langes Textmaß → Maß begrenzen/neu gruppieren`; `Toolbar-Kollision → sinnvolles Wrapping oder nachrangige Aktionen zugänglich bündeln`; `zweidimensionaler Vergleich → orientiertes Scrollen oder alternative Ansicht`; `Motivverlust → anderer Crop/Source`. Dazu jeweils ein Gegenfall und erhaltene Inhalte. web.dev zeigt eine konkrete inhaltsgetriebene Breakpoint-Ableitung und warnt vor dem Verstecken von Inhalt allein wegen kleiner Flächen. Beispielbreiten bleiben beispielspezifisch. [Q12](#quellenabgleich)

**Prüffall:** Eine mittlere Breite und lange lokalisierte Inhalte erzwingen eine begründete Umordnung. Die Lösung muss Aufgabe, Reihenfolge und relevante Inhalte erhalten; ein bestandener Screenshot ersetzt keinen Laufzeittest.

### 17 · editorial-and-fixed-media-design · P1 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/editorial-and-fixed-media-design.md), Z. 18–70.

**Vorhanden:** Medienklassen, Flatplan, Seiten-/Doppelseiten-/Sequenzsicht, Anker, Dichte, Vorlagen, Bindung und Betrachtungskontext. Die Unterschiede zwischen Präsentation und Dokument sind bereits angesprochen.

**Lücke:** Sehr verschiedene Arbeitsfälle werden überwiegend durch einen gemeinsamen Absatz angeleitet. Eine konkrete Verteilung von Inhalt auf Einzelseite, Doppelseite, Vortrag und selbstständig lesbares Dokument fehlt.

**Ergänzung:** Kurze fallabhängige Einstiegshilfen: Plakat über Informationspriorität und Distanz; Publikation über Flatplan, Anker und Seitenwechsel; Livepräsentation über sichtbare Aussage und Sprecherkontext; Dokument über Navigation und selbstständige Lesbarkeit. Einen Flatplan mit unterschiedlichen Inhaltsmengen durchspielen, einschließlich einer legitim dichten Seite. Keine neuen Fachmodule oder verpflichtende Schablonen.

**Prüffall:** Identischer Stoff als Vortrag und als Lesedokument darf andere Inhaltsverteilung erhalten, muss aber alle jeweils erforderlichen Informationen bewahren. Die konkrete medienübergreifende Lehrprobe ist eine lokale Empfehlung; vorhandene BCcampus-Grundlagen stützen nur die relationalen Organisationsprinzipien. [Q1](#quellenabgleich)

### 18 · packaging-graphics-and-sku-systems · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/packaging-graphics-and-sku-systems.md), Z. 56–94.

**Vorhanden:** Autoritative Geometrie, Panelgraph, echte Texte, SKU-Invarianten und -Unterschiede, Montagezustände, Regal und Thumbnail sind praktisch gut adressiert.

**Lücke:** Panelgraph und SKU-Grammatik könnten durch eine ausgefüllte kleine Vergleichsprobe verständlicher werden. Es fehlt kein weiterer pauschaler Verpackungsgrundsatz.

**Ergänzung:** Mit gelieferter Geometrie drei fiktive Varianten und ein besonders leicht verwechselbares Paar zeigen: Welche Merkmale bleiben konstant, welche unterscheiden Produktart beziehungsweise Variante, welche Information liegt auf welcher sichtbaren Fläche? Die Beziehung von flachem Entwurf und zusammengesetzter Ansicht markieren.

**Prüffall:** Kleinste Packung und längste gelieferte Variante müssen unterscheidbar bleiben, auch wenn Farbe als alleinige Hilfe wegfällt. Keine Dieline-Konstruktion, Barcodewerte oder Pflichttexte erfinden; keine Regalwirkung aus einem Mockup behaupten.

### 19 · physical-wayfinding-and-signage-systems · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/physical-wayfinding-and-signage-systems.md), Z. 53–95.

**Vorhanden:** Reise vor Schild, Ziele, Entscheidungspunkte, Bestätigung, Rückweg, Umgebung, temporäre Zustände und multimodale Anforderungen.

**Lücke:** Ein ausgefüllter Entscheidungspunkt würde die Beziehung zwischen Frage des Reisenden, Schildbotschaft, Pfeil, Sichtposition und nachfolgender Bestätigung greifbarer machen.

**Ergänzung:** Eine explizit gelieferte Route mit einer Abzweigung und einem Ebenenwechsel darstellen. Zeigen, wie Zielgruppen und Pfeile zusammengehören und welche weitere Bestätigung nach der Richtungsentscheidung benötigt wird. Fehlwege nur auf Basis der vorgegebenen Routendaten behandeln.

**Prüffall:** Hinweg, Rückweg und verpasste Abzweigung in derselben Karte nachvollziehen. Nicht durch bloße Vergrößerung aller Schilder reparieren. Buchstabenhöhen, Montagehöhen und Sicherheitswege bleiben bei ihren konkreten Fach- und Standortvorgaben; neue universelle Zahlen wären kein Gewinn.

### 20 · motion-and-sequence · P1 · T/A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/motion-and-sequence.md), Z. 35–70 und 93–130.

**Vorhanden:** Zeitliche Hierarchie, Zustände, Kontinuität, Haltephasen, Unterbrechung, Loops, kinetischer Satz und reduzierte Alternative sind stark. Timing und Easing werden ausdrücklich nicht als universelle Rezepte behandelt.

**Lücke:** Es fehlt eine konkrete Auswahlhilfe für Bewegungsverlauf, Beschleunigung, Abbremsen und Staffelung. Die Aufforderung, keine pauschalen Zeiten zu verwenden, hilft noch nicht beim Bestimmen passender Zeiten.

**Ergänzung:** Eintritt, sichtbare Zustandsänderung und Austritt als unterschiedliche Fälle erklären; Start-/Zielrelation, Weg, Größe, Aufmerksamkeit und Wiederholung zusammen prüfen. Kleine Bewegungsstudien mit identischem Inhalt und unterschiedlichem Verlauf verwenden. Carbon zeigt kontextbezogene Kurven und zeitliche Abstufungen; sein Bounce-Verbot und seine Millisekundenwerte sind IBM-Systemregeln, kein Scoville-Standard. [Q13](#quellenabgleich)

**Prüffall:** Ein häufig genutzter Zustandswechsel und eine expressive Einzelsequenz müssen unterschiedliche Prioritäten erhalten. Unterbrechen und reduzierte Darstellung dürfen die Zustandsaussage nicht verlieren. Der Audit validiert die im Modul enthaltenen Standardschwellen nicht neu.

### 21 · media-production-and-handoff · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/media-production-and-handoff.md), Z. 17–66 und 68–158.

**Vorhanden:** Sehr umfangreiche, formatspezifische Produktionsbedingungen, Quellen-/Ableitungskette, Rendern, Semantik, tatsächlicher Empfänger und getrennte Nachweisstufen.

**Lücke:** Ein kompakter realer Lieferfall fehlt. Weitere Checklisten würden die vorhandene Tiefe eher wiederholen. Die effektivste Ergänzung wäre die ausgefüllte kleine Anwendung.

**Ergänzung:** Beispiel für `editierbare Quelle → Export → Empfängerprüfung`, jeweils mit tatsächlich bekannten Parametern und offenem Nachweis. Optional eine kurze Fragenkarte für unbekannte Lieferbedingungen und die einfache Umrechnung effektiver Bildauflösung: verwendete Pixelbreite geteilt durch physische Breite in Zoll. Diese Rechnung bestimmt keinen universellen Qualitätszielwert.

**Prüffall:** Ein kleiner lokaler Export darf nicht zum kompletten Release-Dossier werden. Ein für einen realen Druckempfänger bestimmter Export darf dagegen keine unbestätigten Produktionsparameter als genehmigt ausgeben.

### 22 · critique-and-validation · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/critique-and-validation.md), Z. 45–97 und 111–147.

**Vorhanden:** Präzise Befundtypen, Beobachtung/Ursache/Absicht, Kontrollbedingungen, Abgrenzung von Präferenz und Fehler sowie Erhalt gelungener Beziehungen.

**Lücke:** Der Katalog würde von einer kurzen Kalibrierungsprobe profitieren. Insbesondere „sieht unruhig aus“ und „Text gehört sichtbar zur falschen Gruppe“ benötigen unterschiedliche Begründungen.

**Ergänzung:** Dieselbe ungewöhnliche Anordnung einmal als funktionierende Ausnahme und einmal als falsche Gruppierung untersuchen. Einen vollständigen kurzen Befund mit Ort, Beobachtung, vermuteter Wirkung, Ursache, kleinstem Eingriff und Gegenbeweis ausfüllen. Keine zusätzliche Punkteskala und kein Universalästhetik-Score.

**Prüffall:** Der Agent lokalisiert den belegten Fehler und erhält die gültige Abweichung. Die Übereinstimmung mit einem Beispiel darf nicht als unabhängige Qualitätsbewertung gelten. Der vorgeschlagene Mechanismus operationalisiert den vorhandenen Befundvertrag.

### 23 · culture-and-representation · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/culture-and-representation.md), Z. 41–109.

**Vorhanden:** Konkrete Darstellungsprobleme und Reparaturen: Rolle/Agency, kontextspezifisches Material, Stereotype, zeitliche Vermischung, Autorität, Namen, Beschnitt und Derivate.

**Urteil:** Keine neue allgemein gültige Gestaltungsregel begründbar. Das Modul bietet bereits sichere Alternativen wie autorisierte Beiträge, spezifischen Kontext, nichtrepräsentierende Struktur oder Weglassen. Ein weltweiter Symbol- oder Farbbedeutungskatalog könnte genau die undifferenzierten Annahmen verstärken, die das Modul vermeiden soll.

**Erhalten/prüfen:** Eine später auftretende konkrete Darstellungsfrage muss mit ihrer zuständigen Quelle und betroffenen Autorität geklärt werden. Ein möglicher Entwicklungsfall wäre eine Darstellung, deren spezifische Rolle durch einen Crop verloren geht. Dieser Audit ersetzt keine kulturelle Fachprüfung und belegt keinen aktuellen Praxisfehler.

### 24 · people-privacy-and-media-integrity · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/people-privacy-and-media-integrity.md), Z. 35–106.

**Vorhanden:** Konkrete Medienmodi, zulässige Eingriffe, Bild-/Textkontext, Metadaten, Offenlegung und Risiken von Derivaten. Die Unzulänglichkeit bloßer Unkenntlichmachung ist bereits erklärt.

**Urteil:** Kein zusätzlicher Regelbereich nötig, um praktische Gestaltung besser anzuleiten. Die handwerkliche Verbesserung von Bildern gehört zu Imagery. Eine neue Retuschier- oder Anonymisierungsrezeptur hier würde Zuständigkeiten vermischen.

**Erhalten/prüfen:** Modus und erforderlicher Kontext müssen durch Vorschaubild, Crop und Export erhalten bleiben. Ein sinnvoller späterer Test betrifft ein Derivat, das seine Offenlegung verliert; das ist bereits vom bestehenden Vertrag abgedeckt. Keine aktuelle Rechts- oder Anonymitätsprüfung durchgeführt.

### 25 · sustainability-claims · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/sustainability-claims.md), Z. 34–93.

**Vorhanden:** Gestaltung als Gesamtaussage, Hierarchie von Behauptung und Einschränkung, bildliche Zertifizierungssignale, Bezugsgröße und eng begrenzte belegbare Aussage. Reparaturen betreffen ausdrücklich auch die visuellen Mittel.

**Urteil:** Der praktische Gestaltungsbezug ist vorhanden. Ein allgemeiner Nachhaltigkeitsstil, eine Grünverbotsliste oder zusätzliche pauschale Rechtssätze wären nicht gerechtfertigt.

**Erhalten/prüfen:** Bei einem konkreten Auftrag müssten dominante Bildaussage und tatsächlich belegte Reichweite gemeinsam geprüft werden. Eine kleine Fußnote darf keine gegenteilige dominante Darstellung retten. Diese Anforderung steht bereits im Modul; der Audit bestätigt keine aktuelle juristische oder ökologische Freigabe.

### 26 · source-verification-and-evidence · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/source-verification-and-evidence.md), Z. 16–60 und 88–120.

**Vorhanden:** Atomare Aussagen, tatsächliche Quellenbeziehung, genaue Reichweite, Gegenbelege, Aktualität, Abhängigkeiten und Korrektur. Offline-Handlungsfähigkeit und Grenzen volatiler Aussagen sind ausdrücklich getrennt.

**Urteil:** Keine neue Regel zur praktischen Gestaltung erforderlich. Das Modul soll die Belegarbeit tragen, nicht Typografie- oder Diagrammentscheidungen wiederholen. Ein ausgefüllter Belegdatensatz wäre optionales Schulungsmaterial, allein aber kein begründeter Pflichtausbau.

**Erhalten/prüfen:** Bei späteren Craft-Ergänzungen muss die konkrete Passage die zugeschriebene Regel tatsächlich tragen. Der nicht geroutete Quellenindex macht bereits transparent, dass eine Quellenfamilie keine passagegenaue Begründung jeder Einzelregel ist. Dieser Audit fand daher keinen verdeckten Anspruch vollständiger Einzelbelegung.

### 27 · asset-rights-and-attribution · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/asset-rights-and-attribution.md), Z. 46–75 und 104–117.

**Vorhanden:** Tatsächliche Nutzung, eingebettete Bestandteile, getrennte Rechteebenen, Schriften, generierte Assets sowie sichtbare und dauerhaft erhaltene Credits.

**Urteil:** Die praktische Lücke ist nicht ein weiterer Regelkatalog. Credit-Platzierung ist bereits enthalten; die konkrete Lösung der Hierarchie und Satzfläche gehört zu Komposition beziehungsweise Typografie.

**Erhalten/prüfen:** Ein späterer Exportfall sollte zeigen, dass die erforderlichen Hinweise im gelieferten Artefakt überleben. Eine generelle automatische Freigabematrix für Lizenznamen ist nicht zu empfehlen. Dieser Audit prüft keine konkreten Assetlizenzen und behauptet keine rechtliche Freigabe.

### 28 · style-direction · P2 · A

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/style-direction.md), Z. 18–97.

**Vorhanden:** Bedeutungszweige, Quellenstatus, Struktur statt Motive, Herstellungsursache, dominante Richtung, begrenzte Einflüsse und Übersetzung in verschiedene Medien.

**Lücke:** Die Ableitung der „DNA“ ist anspruchsvoll und wird ohne vollständiges Beispiel erläutert. Das kann trotz guter Warnungen zu plausibler Beschreibung ohne sichtbare Umsetzung führen.

**Ergänzung:** Eine mit tatsächlich geprüften Referenzen belegte räumliche oder produktionstechnische Relation herausarbeiten und mit gleichen Inhalten in zwei Medien übersetzen. Sichtbar machen, welche Eigenschaft erhalten wird, welche medienbedingt entfällt und welche Kompensation nötig ist. Nicht alle Stilkomponenten künstlich besetzen.

**Prüffall:** Die Richtung muss über das auffälligste Oberflächenmotiv hinaus eine nachvollziehbare Struktur behalten, darf aber eine nützliche vertraute Orientierungshilfe erhalten. Keine verpflichtende Stil-Enzyklopädie. Das konkrete historische Lehrbeispiel wäre vor Erstellung gesondert zu recherchieren.

### 29 · generic-signatures-and-subject-specificity · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/generic-signatures-and-subject-specificity.md), Z. 25–68.

**Vorhanden:** Genau die praktisch hilfreiche Form, die andernorts öfter fehlt: Symptom, mögliche Ursache, legitimer Einsatz und konkrete Gegenmaßnahme. Dazu Evidenzstatus, Austauschbarkeitstest und begrenzte Aussagekraft.

**Urteil:** Den Katalog aktuell halten, aber nicht wegen des Audits verlängern. Mehr Trendbeispiele sind gegenüber vertieftem Handwerk nachrangig. Das Modul kann als Strukturvorbild für kleine Entscheidungshilfen dienen, ohne seinen gesamten Katalog in andere Module zu kopieren.

**Erhalten/prüfen:** Ein legitimes Kartenraster muss bestehen bleiben; ein durch Templategleichheit verfälschtes Inhaltsverhältnis muss repariert werden. Das bestehende Modul enthält beide Seiten. Ein Muster bleibt ein Prüfanlass, kein Beweis für KI-Ursprung oder schlechte Qualität.

### 30 · coordination-with-sibling-skills · Bestand

**Beleg:** [Modul](../../../scoville-design-anti-ai-slop/references/coordination-with-sibling-skills.md), Z. 15–65.

**Vorhanden:** Kleiner Austauschvertrag, echte Quelle/Version, geschützte Beziehungen, erlaubte Variation, offene Entscheidung und Nachweis. Design, UI und Wording sind ausreichend unterschieden.

**Urteil:** Keine neue Gestaltungsregel und kein zusätzlicher Aktivierungsmechanismus erforderlich. Ein Pflichtübergabedokument für jede Kleinigkeit wäre kontraproduktiv. Solo-Arbeit ist bereits im Core abgesichert.

**Erhalten/prüfen:** Ein tatsächlicher Implementierungskonflikt muss mitsamt Auswirkung an den Entscheidungsowner zurückgehen. Ein späterer Test kann eine nicht unterstützte Darstellung verwenden und prüfen, ob die beabsichtigte Beziehung erhalten bleibt. Ein solcher Test ist bereits eine Anwendung des bestehenden Vertrags, kein neuer Kompetenzbereich.

## Wie eine Ergänzung praktisch aussehen sollte

Die folgenden kleinen Beispiele demonstrieren das empfohlene Format. Es sind eigens konstruierte Lehrbeispiele und keine bereits getesteten Verbesserungen des Skills.

### Beispiel A: Raster aus Inhalt ableiten

**Situation:** Eine feste Informationsseite benötigt zwei tatsächlich gleichrangige Textspalten. Die nutzbare Breite beträgt in diesem Beispiel 168 mm; der zunächst angenommene Spaltenabstand 8 mm.

**Konstruktion:** Bei zwei gleich breiten Spalten ergibt sich `(168 − 8) / 2 = 80 mm` pro Spalte. Die Rechnung liefert Geometrie, noch kein gutes Textmaß. Deshalb echten Text mit den vorgesehenen Fonts und Größen in beide Spalten setzen.

**Entscheidung:** Falls das tatsächliche Textmaß nicht zum Lesen passt, Spaltenanzahl, nutzbare Breite, Abstand oder Satzparameter als zusammenhängende Optionen prüfen. Die Annahme gleichrangiger Spalten darf nur gelten, wenn die Inhalte wirklich gleichrangig sind.

**Gegenfall:** Ein kurzer Hinweis neben einem längeren Haupttext braucht nicht zwei gleich breite Spalten. Die mathematische Symmetrie wäre dann möglicherweise eine falsche Inhaltsbeziehung.

**Prüfung:** Vollständige Inhalte, Umbrüche, Gruppierung und Hierarchie in Zielgröße. Keine behauptete allgemeine 80-mm-Regel.

### Beispiel B: Abstände nach Beziehung reparieren

**Situation:** Eine Überschrift wirkt dem vorangehenden Absatz zugeordnet, obwohl sie den folgenden Absatz einleitet. Alle Inhalte und typografischen Rollen sind bereits korrekt.

**Eingriff:** Zunächst den Abstand zur vorangehenden Gruppe und zum nachfolgenden Absatz vergleichen. Eine Veränderung dieser beiden Beziehungen kann die Zuordnung klären, ohne die ganze Seite luftiger zu machen. Vorhandene Ausrichtung, Einfassung oder andere Gruppierungssignale mitprüfen.

**Gegenfall:** Ein absichtlich freistehender Kapitelauftakt kann einen größeren Abstand zum nachfolgenden Text benötigen. Dann müssen Hierarchie, Seitenrolle oder ein anderer sichtbarer Anker die Zuordnung tragen.

**Prüfung:** Die passende Gruppe muss erkennbar sein; die Gesamtkomposition und ihre beabsichtigte Dichte bleiben erhalten. Kein festes Abstandsverhältnis als allgemeines Gesetz.

### Beispiel C: Regel, Quelle und Systemgrenze gemeinsam liefern

**Situation:** Eine neue Icon-Familie wirkt uneinheitlich, obwohl alle Symbole in identischen Boxen stehen.

**Eingriff:** Silhouette, Innenräume und visuelles Gewicht vergleichen. Gemeinsame Hilfsformen können die Größenbeziehungen unterstützen; der tatsächliche Gegenstand darf eine abweichende Proportion verlangen. Im realen Zielmaß prüfen.

**Quellenbezug:** IBM zeigt Keyshapes, Gewicht und Formausnahmen in seiner eigenen Icongestaltung. Die spezifischen IBM-Raster-, Winkel-, Strich- und Markenmerkmale werden dadurch nicht allgemeine Scoville-Pflichten. [Q10](#quellenabgleich)

**Gegenfall:** Bei einem bestehenden Iconsystem werden dessen freigegebene Regeln angewandt; dieses Beispiel autorisiert keine neue Familie oder eigenmächtige Systemänderung.

## Empfohlene Aufnahme und Prüfung

Die folgenden Schritte sind eine Empfehlung innerhalb des Audits, kein neu aktivierter Implementierungsplan.

1. **Zuerst die Grundlagen vertiefen:** In Typografie, Komposition und Farbe jeweils die nachgewiesene Textlücke mit einer kleinen Entscheidungshilfe oder Arbeitsprobe schließen. Gute vorhandene Regeln und Ausnahmen erhalten.
2. **Danach Konstruktion und Darstellung:** Imagery, Brand und Mark um ihre jeweils eigenen Techniken erweitern; Information, Diagramme, Web, Fixed Media und Motion um konkretisierte Auswahlhilfen.
3. **P2 nur nach Nutzen ergänzen:** Ausgefüllte Beispiele sollen vorhandene Entscheidungen verständlicher machen. Ein zusätzliches Beispiel ohne neue Unterscheidung rechtfertigt keinen längeren Laufzeittext.
4. **Keine neuen Blätter allein aus Themenfülle:** Abstände bleiben gemäß der bestehenden Entscheidung bei ihren Beziehungen. Ein eigenständiges Icon-, Illustrations- oder Vektorblatt wäre erst bei belegtem unabhängigem Routing- und Aufgabennutzen eine neue Architekturfrage. Der aktuelle Audit empfiehlt zunächst Vertiefung in den bestehenden Ownern.
5. **Quellenrelation vor Aufnahme festhalten:** Genaue Passage, Regelart, Geltungsbereich und ausdrückliche Einschränkung dokumentieren. Lokale Synthesen als solche ausweisen; frei zugängliche Beispiele nicht automatisch als übernehmbar behandeln.
6. **Verbesserung am Verhalten prüfen:** Unveränderten Skill und Kandidaten unter gleichen Modell-/Werkzeugbedingungen vergleichen. Für jeden aufgenommenen Mechanismus eine Aufgabe, die die Lücke sichtbar macht, sowie einen legitimen Gegenfall verwenden. Sowohl Entwurf als auch Diagnose/Reparatur müssen im relevanten Kontext geprüft werden.

Eine Ergänzung besteht erst dann den praktischen Test, wenn sie zu einem konkreteren, angemessenen Eingriff führt, ohne falsche Pflichtregeln, unnötige Quellenabfragen, überflüssige Records oder neue Zuständigkeitsfehler zu erzeugen. Sichtprüfung muss das tatsächliche Ergebnis beurteilen; das bloße Auftauchen des neuen Fachworts reicht nicht.

Nicht empfohlen sind universelle Schriftanzahlen, obligatorische Serif/Sans-Paarungen, ein fixes Abstands- oder Spaltenraster, eine allgemeine Palette nach Prozentanteilen, pauschale UI-Gesetze, ein Golden-Ratio-Logoanspruch oder ein vollständiger Animationsprinzipienkatalog für jede Bewegung. Zahlen dürfen Ausgangswerte mit Kontext sein. Das aktuelle Verbot unbegründeter Universalität sollte nicht zum Verzicht auf nützliche, ausdrücklich vorläufige Ausgangswerte führen.

## Quellenabgleich

Abruf und textliche Abschnittsprüfung: 5. September 2026. Die Quellen unterstützen die jeweils bezeichneten Fachmechanismen oder zeigen eine konkrete Lehrform. Sie belegen **keinen gemessenen Vorteil von Scoville oder der vorgeschlagenen Änderungen**. Wo unten lediglich eine lokale Empfehlung vorliegt, wurde keine externe Bestätigung erfunden. Die übrigen Modulurteile beruhen auf den jeweils direkt verlinkten aktuellen Skilltexten.

| ID | Geprüfte Primärquelle und Abschnitt | Tragfähiger Bezug und Grenze |
| --- | --- | --- |
| Q1 | BCcampus, *Graphic Design and Print Production Fundamentals*: [3.3 Compositional Principles](https://opentextbc.ca/graphicdesign/chapter/3-3-compositional-principles-strategies-for-arranging-things-better/) und [3.4 Organizational Principles](https://opentextbc.ca/graphicdesign/chapter/3-3-organizational-principles/), insbesondere Alignment/Contrast sowie Grid und weitere Organisationssysteme; Buch 2015 | Inhaltlich begründete räumliche Organisation und verschiedene Anordnungsmechanismen. Didaktische Fachquelle, kein empirischer Beweis universeller Schönheit. Die Rechnung und Arbeitsprobe dieses Audits sind eigene Konstruktionen. |
| Q2 | Matthew Butterick, [Line length](https://practicaltypography.com/line-length.html), Fließtext und Längenempfehlung | 45–90 Zeichen als Empfehlung dieses Autors. Keine Übertragung auf alle Sprachen, Schriftrollen, Distanzen oder Medien. |
| Q3 | Matthew Butterick, [Line spacing](https://practicaltypography.com/line-spacing.html), Definition und Vergleich der Satzproben | 120–145 Prozent als autorenbezogener Bereich. Kein verbindlicher allgemeiner Zeilenabstand. Die Abbildungen wurden hier nicht separat visuell bewertet. |
| Q4 | Datawrapper, [What to consider when choosing colors for data visualization](https://www.datawrapper.de/academy/what-to-consider-when-choosing-colors-for-data-visualization), Farbrollen, Nachbarschaft, Helligkeitsverlauf, Kategorie/Verlauf | Konkrete Arbeit an Datenpaletten. Die Übertragung auf allgemeine Rollenpaletten ist eine begrenzte lokale Synthese; insbesondere keine universelle Maximalzahl von Farben übernehmen. |
| Q5 | IBM Design Language, [Illustration: Tips and techniques](https://www.ibm.com/design/language/illustration/tips-and-techniques/), Ways of seeing/Intent | Praktische Unterscheidung nach Abstraktion, Maßstab, Detail und Aufgabe. IBM-Stilvorgaben bleiben beim IBM-System; keine allgemeine Pflicht zu flacher oder isometrischer Darstellung. |
| Q6 | IBM Design Language, [Photography: Tips and techniques](https://www.ibm.com/design/language/photography/tips-and-techniques/), Perspective/Composition/Aspect ratio | Beispiel einer konkret formulierten Bildregie. Das IBM-2x-Raster, feste Bildverhältnisse und Perspektivbeschränkungen werden ausdrücklich nicht generalisiert. |
| Q7 | Office for National Statistics, [Chart types](https://service-manual.ons.gov.uk/data-visualisation/chart-types), Aufgabenfamilien und Beschreibung der Beispielstruktur | Belegt eine praktisch organisierte Auswahlhilfe mit Einsatzfällen. Nicht sämtliche verlinkten Spezialseiten wurden geprüft; die ONS-Auswahl ist kein vollständiger Katalog aller geeigneten Charts. |
| Q8 | Datawrapper, [What to consider when creating line charts](https://www.datawrapper.de/academy/what-to-consider-when-creating-line-charts), When to use line charts | Konkrete Unterscheidung von Zeitverlauf, Kategorienvergleich und Periodensummen. Die Formulierung der Quelle, Linien nur für Zeit zu verwenden, wird nicht als allgemeine Regel übernommen: Auch andere geordnete kontinuierliche Größen können Linien rechtfertigen. |
| Q9 | Graphviz, [Layout Engines](https://graphviz.org/docs/layouts/), Beschreibungen von dot/neato/fdp/circo/twopi; Seitenänderung 2022 | Belegt verschiedene tatsächlich verfügbare Anordnungsfamilien. Kein Nachweis, dass ein Algorithmus automatisch ein verständliches Diagramm erzeugt; keine neue Toolabhängigkeit empfohlen. |
| Q10 | IBM Design Language, [UI icons: Design](https://www.ibm.com/design/language/iconography/ui-icons/design/), Foundation/Key shapes/Strokes/Corners; angezeigte Aktualisierung 3. September 2026 | Konkrete Anleitung für Formenverhältnis und visuelles Gewicht mit zulässigen Formabweichungen. Systemwerte wie 32-px-Raster oder 2-px-Striche sind IBM-spezifisch. |
| Q11 | Adobe, [Draw curves with the Pen tool](https://helpx.adobe.com/illustrator/desktop/draw-shapes-and-paths/draw-shapes/draw-curves-with-the-pen-tool.html), C-/S-Kurven und Griffe; Aktualisierung 25. Februar 2026 | Technische Grundlage einer Kurven-Arbeitsprobe. Keine Begründung eines automatisch guten Logos oder eines universellen optischen Korrekturmaßes. |
| Q12 | Google/web.dev, [Responsive web design basics](https://web.dev/articles/responsive-web-design-basics), How to choose breakpoints/Avoid hiding content; angezeigte Aktualisierung 12. Februar 2019 | Konkretes Beispiel für inhaltsabhängige Anpassung. Beispielbreiten und Aussagen zu idealen Zeilenlängen bleiben kontextgebunden; hier kein aktueller Browser-Supportaudit. |
| Q13 | Carbon Design System, [Motion overview](https://carbondesignsystem.com/elements/motion/overview/), Easing/Duration | Zeigt Kurvenwahl nach Bewegungsrolle und eine zeitliche Abstufung. Carbon-Werte und Verbote sind Systemkonventionen; expressive Ausnahmen bleiben außerhalb dieses Systems möglich. |

Es wurden nur Erkenntnisse zusammengefasst und Quellen verlinkt. Eine Übernahme fremder Texte, Abbildungen, Schriftproben, Icons, Markenassets oder Vorlagen ist nicht Teil der Empfehlung. Vor einer tatsächlichen Übernahme wäre die konkrete Material- und Lizenzlage gesondert zu prüfen.

## Abschluss und unveränderte Grenzen

Der Audit deckt den Core und alle 30 aktuell gerouteten Fachmodule ab. Die Fachquellen stützen ausgewählte Ergänzungen; für andere Vorschläge ist die lokale Textanalyse ausdrücklich die einzige Grundlage. Der Bericht formuliert priorisierte Verbesserungen, keine beschlossene neue Skillarchitektur.

Es wurden keine Skillmodule, Metadaten, Quellenregister, Planrecords, Tests oder historischen Ergebnisse geändert und keine Veröffentlichungen vorgenommen. Der Bericht liegt separat im lokalen Ausgabeordner. Der Nachweis eines besseren Designresultats bleibt Aufgabe eines späteren, gezielten Vergleichs der tatsächlich umgesetzten Ergänzungen.

## Archivkopie für PLAN-0007

Diese Kopie hält den Audit als Entwicklungsquelle fest. Nur relative Dateiverweise wurden angepasst; die Befunde bleiben erhalten. Original: Z:\Projekts\AI\output\scoville-design-practical-guidance-audit-2026-09-05.md; SHA-256: 0D6E4FFF3962EC29F9CB518DF5751EFF4F5A95C5E533888B1031D830EC8E65F4. Aussagen über unveränderte Dateien beziehen sich auf den Auditturn vor dieser Planerstellung.