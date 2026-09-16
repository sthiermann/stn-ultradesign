# GitHub-Landschaft für einen eigenständigen Design-Skill

**Abruf und Vergleichsstand: 16.09.2026.** Gegenstand sind veröffentlichte Fähigkeiten und Nachweise, keine Übernahme fremder Skills. Gelesen wurden Repository-Übersichten, README-Darstellungen, Lizenzmetadaten und eine verlinkte Fallstudie. Es wurde kein fremder Skill installiert, ausgeführt, geklont oder in unser Paket übernommen. Anweisungen aus fremden Repositories wurden nicht als Arbeitsanweisungen ausgeführt. Die Quellen stehen auf veränderlichen Hauptzweigen; ein späterer reproduzierbarer Vergleich muss konkrete Revisionen festhalten.

## Was die betrachteten Projekte tatsächlich anbieten

### UI UX Pro Max

[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) beschreibt eine durchsuchbare Sammlung von Design- und Technologieempfehlungen sowie die Erzeugung und Speicherung projektspezifischer Designregeln. Die aktuelle Übersicht nennt zahlreiche Stile, Farbschemata, Schriftkombinationen, Diagrammtypen und Web-/Native-Technologien. Dokumentiert werden auch Barrierefreiheit, robuste Textdarstellung, Versionsbezug und Katalogpflege.

**Stärke laut Dokumentation:** große strukturierte Breite und schneller Zugang zu konkreten Gestaltungsvorschlägen. **Zu prüfen:** Ob die Empfehlungen das richtige Nutzerproblem treffen und komplexe Abläufe zuverlässig verbessern, lässt sich aus Kataloggröße nicht ableiten. Eine Abbildung oder ein Demo ist kein Vergleichsexperiment. Das README kennzeichnet ein verlinktes historisches Video ausdrücklich als Inspiration statt Benchmark. Dies ist kein Nachweis, dass das Projekt keine weiteren Tests besitzt.

**Lizenzmetadatum:** Die [Lizenzdatei](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/LICENSE) nennt MIT. Unser Vorhaben verwendet daraus weder Datensätze noch Quellcode, Templates oder Anweisungstexte.

### Impeccable

[pbakaus/impeccable](https://github.com/pbakaus/impeccable) dokumentiert wesentlich mehr als visuelle Stilhinweise: Produktkontext, Entwurf vor Implementierung, Kritik, technische Audits, responsive Anpassung, Browseriteration und deterministische Prüfroutinen. Die beim Abruf gelesene Übersicht nennt 24 Befehle und 61 deterministische Regeln. Diese Zahlen sind Herstellerangaben zum damaligen Stand, keine unabhängig geprüfte Abdeckung.

**Stärke laut Dokumentation:** Verbindung von Gestaltungsarbeit, Projektkontext und praktischer Browserkontrolle. **Zu prüfen:** Ein erkannter Gestaltungshinweis ist nicht automatisch ein Nutzerproblem; ausdrücklich meinungsgeprägte Stilregeln brauchen Kontext. Es wäre sachlich falsch, diesem Projekt pauschal Konzeptarbeit oder Audits abzusprechen.

Die eigene [Neo-Mirai-Fallstudie](https://impeccable.style/cases/neo-mirai/) zeigt den beschriebenen Weg von visuellen Referenzen zur responsiven Website mit Browserkorrekturen. Sie ist ein Demonstrationsbeispiel; die gelesene Seite enthält kein kontrolliertes Vergleichsexperiment mit Nutzerergebnissen.

**Lizenzmetadatum:** [LICENSE](https://github.com/pbakaus/impeccable/blob/main/LICENSE) nennt Apache 2.0. Die dortige Erweiterung fremder Arbeit wird für unser Projekt nicht nachgebildet; wir schreiben eigenständige Materialien.

### Vercel Agent Skills

[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) ist eine Sammlung mehrerer spezialisierter Skills. Die gelesene Übersicht beschreibt React-/Next.js-Leistungsregeln und eine UI-Codeprüfung mit Themen wie Semantik, Fokus, Formularen, Bewegung, Navigation, Touch, Internationalisierung und Darstellung. Die README-Angabe umfangreicher Regelmengen ist eine Umfangsbeschreibung, kein gemessenes Qualitätsranking.

**Stärke laut Dokumentation:** technische Nähe zu Webimplementierung und klare Spezialisierung. **Zu prüfen:** Quellcodeprüfung allein kann reale Nutzeraufgaben, fachliche Berechtigungen oder visuelle Wirkung nicht vollständig bewerten. Diese Grenze gilt für unseren Skill ebenso. Die Sammlung als Ganzes darf nicht mit einem einzelnen darin enthaltenen Skill gleichgesetzt werden.

**Lizenzmetadatum:** Das README nennt MIT. Eine zusätzlich versuchte separate LICENSE-Adresse war nicht abrufbar; daraus wird keine genauere Lizenzanalyse abgeleitet. Es werden keine Dateien übernommen.

### Anthropic als separat behandelter Bezugspunkt

Das offizielle [Repository](https://github.com/anthropics/skills) und das [Frontend-Verzeichnis](https://github.com/anthropics/skills/tree/main/skills/frontend-design) wurden zur Zuordnung geöffnet. Die inhaltliche Primäranalyse dieses Skills erfolgt im übergeordneten Rechercheteil. Dieser Teilbericht ergänzt keine ungeprüften Behauptungen zu seiner aktuellen Reichweite oder Lizenz. Namen werden nur zur sachlichen Quellenzuordnung verwendet; daraus folgt keine Verbindung oder Unterstützung unseres Projekts durch die Anbieter.

## Belastbare Schlussfolgerung

Die Landschaft ist bereits anspruchsvoller als „KI bekommt ein paar hübsche Farben“. Einige Projekte verbinden Kontext, Entwurf, Umsetzung und Tests. Unser neues Repository sollte deshalb keine erfundene Lücke behaupten und keine Überlegenheit aus der Zahl eigener Regeln herleiten. In den hier geprüften Übersichten und der gelesenen Fallstudie fand sich kein ausreichender kontrollierter Nachweis, aus dem eine universelle Rangfolge nach Bedienqualität abgeleitet werden könnte. Das ist eine Grenze dieser Untersuchung, keine Aussage über alle unveröffentlichten oder andernorts vorhandenen Evaluationen.

Die folgenden Differenzierungsziele werden aus unserem Auftrag und der Primärforschung entwickelt. Sie sind weder Kopien fremder Module noch bereits bewiesene Wettbewerbsvorteile:

| Eigenes Ziel | Konkretes überprüfbares Ergebnis |
| --- | --- |
| Gesamte Anwendung nachvollziehbar untersuchen | Verzeichnis der Ansichten, Rollen, Zustände und entscheidenden Abläufe mit sichtbaren Abdeckungslücken |
| Konzept gemeinsam entscheiden | Versionierter Entwurf mit Annahmen, Alternativen, Nutzerfreigabe und Zuordnung zur Umsetzung |
| Empfehlungen unterschiedlich gewichten | Klare Trennung von Norm, Konvention, Nutzerbefund, Hypothese und Stilentscheidung |
| Fachliche Abläufe ernst nehmen | Prüfbare Fehler-, Wiederaufnahme-, Konflikt- und Berechtigungsszenarien |
| Analytische Richtigkeit sichern | Datenvertrag, überprüfte Transformationen und realistische Verständnisaufgaben |
| Verbesserung belegen | Vorher/Nachher-Ergebnisse derselben Aufgaben samt Grenzen und Regressionen |

## Eigenständiges Vergleichsverfahren für einen späteren Benchmark

Dieses Verfahren ist eine neue Konzeption für unser Projekt. Es wurde in dieser Recherche noch nicht ausgeführt.

**Aufgaben festlegen.** Eine kleine, bewusst verschiedene Sammlung bestehender Anwendungen verwenden: Verwaltungsoberfläche, analytisches Dashboard, mehrstufiger Vorgang, touchorientierte Anwendung und textreicher Dienst. Geeignete Ausgangsprojekte müssen selbst erstellt oder für den Versuch rechtmäßig nutzbar sein. Die Aufgaben enthalten reale Zustände und identische gewünschte Ergebnisse. Stärken und Schwächen der Ausgangsoberfläche werden vorab dokumentiert.

**Bedingungen vergleichbar halten.** Modell, Version, Werkzeuge, Ausgangsrevision, Zeit-/Tokenbudget, Aufgabenbeschreibung und zugelassene Bibliotheken festhalten. Jeder Kandidat erhält dieselben notwendigen Projektinformationen. Konzeptfreigaben werden nach einem vorab definierten Verfahren behandelt, damit zusätzliche menschliche Hilfestellung nicht unbemerkt den Vergleich verändert. Wiederholungen sind notwendig, weil generative Ergebnisse variieren.

**Qualität getrennt beurteilen.** Die visuelle Begutachtung erfolgt, soweit praktisch möglich, ohne Kenntnis des verwendeten Skills. Davon getrennt werden Aufgabenerfolg, Fehler, Wiederherstellung, Bedienung mit unterschiedlichen Eingaben, responsive Stabilität, Datenkorrektheit und technische Regressionen geprüft. Ein einzelner Gesamtscore darf schwerwiegende Fehler nicht durch gute Ästhetik ausgleichen. Die Prüfer benötigen gemeinsame Bewertungsanker und Beispiele für unterschiedliche Schweregrade.

**Fehlalarme mitzählen.** Bei Audits zählt nicht nur, wie viele Hinweise erzeugt werden. Erfasst werden bestätigte Probleme, übersehene bekannte Defekte, falsche Behauptungen, unbrauchbare Vorschläge und Kosten der Nacharbeit. Bei Umbauten werden erhaltene Funktionen und versehentlich entfernte Fähigkeiten überprüft. Bei Konzepten werden Klarheit der Entscheidungen und Genauigkeit ihrer späteren Umsetzung bewertet.

**Ergebnisse offen berichten.** Für jede Aufgabe Rohwerte, Zahl der Wiederholungen, erlaubte Eingriffe und verbleibende Unsicherheit zeigen. Gute Einzelergebnisse und misslungene Durchläufe gleichermaßen berücksichtigen. Wenn eine Methode nur bei bestimmten Anwendungstypen besser funktioniert, genau diese Grenze benennen. Bis zu dieser Evaluation bleibt „besser“ ein Entwicklungsziel. Sterne, Downloads und eindrucksvolle Screenshots ersetzen dieses Verfahren nicht.

## Herkunft für die Veröffentlichung

Der geplante Projektname `stn-ultradesign` steht für ein neues Paket. Dessen Text, Tests, Vorlagen und mögliche Werkzeuge entstehen aus den Nutzeranforderungen und eigener Synthese der gekennzeichneten Primärquellen. Die hier genannten fremden Repositories dienen ausschließlich dem sachlichen Vergleich. Veröffentlicht werden keine kopierten Skill-Dateien, Kataloge, Beispieloberflächen, Bilder, Logos oder programmspezifischen Befehlssammlungen. Lizenzbezeichnungen werden als verifizierte Repository-Metadaten berichtet, nicht als pauschales Versprechen vollständiger rechtlicher Prüfung.
