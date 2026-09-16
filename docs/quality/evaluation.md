# Prüfstand der Version 0.1.0

Stand: 16. September 2026. Diese Fassung wurde auf Paketkonsistenz, Verhalten des Audit-Prüfers und ausgewählte Skill-Entscheidungen geprüft. Sie ist kein Beleg für universelle Designüberlegenheit, vollständige WCAG-Konformität oder einen bestimmten Verbesserungsfaktor.

## Technische Paketprüfungen

| Prüfung | Ergebnis | Aussagegrenze |
| --- | --- | --- |
| Eigene Repository-Prüfung | Bestanden; 234 lokale Markdown-Verweise geprüft | Dateiziele und Paketkonsistenz; keine Online-Linkprüfung oder Inhaltszertifizierung. |
| 24 Verhaltenstests für `audit_coverage.py` | Bestanden | Prüft den Umgang mit Ledgerdaten, nicht die tatsächliche Anwendung. |
| Mit Codex bereitgestellter Skill-Validator | Bestanden | Frontmatter, Name und Format; keine Qualitätsmessung der Empfehlungen. |
| Mit Codex bereitgestellter Plugin-Validator | Bestanden | Paketmanifest und Skill-Metadaten; kein Installationstest. |
| Claude Code: Pluginmanifest, `--strict` | Bestanden, keine Warnungen | Formale Pluginprüfung. |
| Claude Code: Marketplace, `--strict` | Bestanden, keine Warnungen | Formale Marketplaceprüfung. |

Die abschließenden Python-Prüfungen liefen mit Python 3.12.14; die Claude-Manifestprüfung mit Claude Code 2.1.263. Die 24 Tests decken erfolgreiche Abdeckung, untersuchte Fehler gegenüber bestandenem Produktverhalten, blockierte/ungeprüfte Fälle, unvollständiges Inventar, Kontextpflichten, Graphverweise, API-Verträge, Evidenzmethoden, alte Datenformate, Scope-Änderungen, fachliche Nichtanwendbarkeit, ungültige Referenzen/Duplikate und fehlerhafte Datentypen ab. Sie prüfen beobachtbare Ergebnisse des Prüfers statt dessen Implementierungsdetails.

Die eigene Repository-Prüfung kontrolliert zusätzlich Paketnamen, Versionen, erwartete Dateien, lokale Markdown-Verweise, Python-Syntax und JSON. Sie ist ein kleines projektspezifisches Hilfsmittel und ersetzt keine vollständigen Client-Schemas. Beide Befehle laufen ohne zusätzliche Python-Pakete aus dem Repository-Stamm:

```sh
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

Die GitHub-Actions-Konfiguration führt dieselben beiden Befehle mit Python 3.12 aus. Der erste [GitHub-Lauf](https://github.com/sthiermann/stn-ultradesign/actions/runs/35088621779) für Commit `31ed66c026eb0c5a15fc63ab2b23767963348c6a` wurde nach Veröffentlichung erfolgreich abgeschlossen. Die offiziellen Codex-Validatoren wurden separat in der Entwicklungsumgebung mit Python 3.12 und PyYAML ausgeführt; deren Quellcode oder Abhängigkeiten werden nicht mitgeliefert.

## Unabhängiger synthetischer Auditlauf

Der evaluierende Agent erhielt den Skill, einen begrenzten Auftrag und eine eigens erstellte Anwendung mit drei Seiten. Der [Auditbericht](../../evals/audit-result.md) dokumentiert Browserinteraktionen, Quellstellen und offene Prüfungen. Die [Fixture](../../evals/audit-fixture/index.html) enthält ausschließlich erfundene Inhalte und simulierte Aktionen. Die unabhängigen Aufgabenläufe fanden während der Entwicklung statt, vor der anschließenden Überarbeitung der maschinenlesbaren Abdeckungsprüfung. Sie sind keine erneuten Ende-zu-Ende-Tests dieser späteren Fassung.

Laut protokollierten Beobachtungen wurden in Microsoft Edge unter macOS alle drei Hauptseiten, beide Projekt-Drilldowns, die Webhook-Detailansicht und die drei Dialogausgänge aufgerufen. Der Bericht enthält zehn priorisierte Befunde, unter anderem eine per Tastatur nicht erreichbare Speicheraktion, Entwurfsverlust beim Fehler, unvollständiges Dialogverhalten und eine irreführende Diagrammskala. Er unterscheidet unmittelbar beobachtetes Verhalten, Schlussfolgerungen aus Quelltext und ungetestete Annahmen. Accessibility-Tree-Beobachtungen werden ausdrücklich nicht als Screenreader-Hörtest ausgegeben.

Die Bildschirmprüfung war später durch eine gesperrte Sitzung blockiert. Responsive Zustände, eine vollständige Tastaturmatrix, echte Touch-/Screenreader-Nutzung und das vollständige WCAG-Kriterienregister blieben offen. Screenshots wurden im Lauf betrachtet, aber nicht als Dateien archiviert. Ein vollständiger Auditabschluss wird deshalb nicht behauptet. Zehn Befunde sind eine Ergebniszahl dieses einzelnen Laufs, keine gemessene Trefferquote gegen einen verblindeten Sollkatalog.

## Unabhängiger synthetischer Konzeptlauf

Ein zweiter Auftrag verlangte ein diskutierbares Einstellungskonzept für ein erfundenes Museumsprodukt. Produktionsumsetzung war nicht freigegeben. Der Agent erstellte einen [isolierten HTML-Prototyp](../../evals/concept-output/index.html), [Besprechungsnotizen](../../evals/concept-output/review.md) und einen [Designvertrag](../../evals/concept-output/design-contract.md).

Das Ergebnis trennt persönliche Benachrichtigungen, Mitgliederberechtigungen und Integrationen. Es kennzeichnet seine Annahmen, simulierte Daten, unbekannte Backendregeln und ausstehende Nutzerentscheidungen. Ein Produktionsprojekt wurde nicht verändert; die Freigabe wurde nicht erfunden.

Der [Prüfbericht des Konzeptlaufs](../../evals/concept-output/verification.md) weist bestandene HTML-Struktur- und JavaScript-Syntaxprüfungen aus. Browserstart beziehungsweise lokale Vorschau waren in der damaligen Testumgebung blockiert. Dieser unabhängige Lauf bestätigte keine gerenderten Screenshots, gemessenen Viewports, Laufzeitabläufe oder assistiven Interaktionen.

Anschließend betrachtete der koordinierende Agent die Ansicht der Benachrichtigungseinstellungen in einem Browser mit einer 1280 × 720 großen Ansicht. Die Oberfläche war sichtbar und in diesem einzelnen Zustand sauber angeordnet. Das ist ein begrenzter Sichtcheck einer Ansicht; die Angabe wird nicht als separat gemessener CSS-Viewport ausgegeben. Weitere Zustände, Speichern, Tastaturbedienung, Responsivität und Screenreader wurden bei diesem Nachcheck nicht geprüft. Daraus folgt keine Freigabe des Konzepts oder der Produktionsumsetzung.

**Ästhetisches Ergebnis: vom Auftraggeber abgelehnt, Überarbeitung offen.** Der Auftraggeber bewertete das sichtbare synthetische Konzept mit Note 5/6 und kritisierte generische Komponenten sowie langweilige Gestaltung von Layout, Anordnung, Farben, Formen, Struktur und Workflows. Der begrenzte Rendercheck ist daher ausdrücklich kein bestandener Gestaltungsnachweis. Das Konzept bleibt als Entwicklungsbefund erhalten, nicht als Qualitätsreferenz für den Anspruch des Skills.

Als Reaktion wurden die Konzept- und Gestaltungsanweisungen substanziell erweitert: produktbezogene visuelle These, strukturelle Alternativen, bewusst gestaltete Informationsbeziehungen, Typografie und Dichte sowie gerenderte Prüfung der Zielgrößen mit konkreter Selbstkritik. Diese Anweisungsänderung ist noch kein Nachweis, dass ein neuer Entwurf den Auftraggeber überzeugt. Eine erneute Bewertung bleibt erforderlich; einzelne Farben, Schriften oder Effekte wurden nicht zu allgemeinen Qualitätsregeln erklärt.

## Prüfung der Skill-Anweisungen

Ein separater Review fand eine relevante Widersprüchlichkeit: Zwei Fachmodule konnten im reinen Auditmodus zusätzliche Konzeptfreigabe und Implementierung verlangen. Die Module unterscheiden jetzt Audit, Konzept und bereits autorisierte Umsetzung. Vorhandene Freigaben werden respektiert; vollständige Audits behalten ihre verbindliche Prüfung jeder Nutzung und jedes definierten relevanten Übergangs. Die Korrektur wurde anschließend durch erneutes Lesen geprüft, nicht durch einen weiteren unabhängigen Anwendungslauf.

Ein weiterer Review zeigte fünf Lücken der ursprünglichen maschinenlesbaren Abdeckungsprüfung. Einfache Evidenztexte und eine gemeinsame Prozentzahl konnten unter anderem reine Quelltextprüfung, Stichproben oder verdeckte Zugriffslücken zu positiv darstellen. **Schema 2** trennt nun Inventar, Kontexte, geplante Pflichten und Ergebnisse. Es prüft Beziehungen von Nutzungen und Übergängen, verlangt passende deklarierte Evidenzmethoden einschließlich API-Beobachtung bei entsprechenden Übergängen und unterscheidet vereinbarten Teilumfang vom ursprünglich verlangten Vollumfang. Ein genehmigtes Sample schließt den ursprünglichen Vollaudit nicht ab. Fehlender Zugriff muss offen bleiben; er ist keine fachliche Nichtanwendbarkeit. Alte Schema-1-Ledger werden ausdrücklich abgelehnt und müssen neu abgeglichen werden.

Ein unabhängiger Gegencheck bestätigte die 24 Tests sowie zusätzliche Gegenfälle für ausschließlich als Quelltext klassifizierte Belege, genehmigtes Sampling, einen blockierten Admin-Kontext und heruntergestufte Übergangs-/API-Prüfpflichten. Alle verhinderten den Vollabschluss. In einem ergänzenden lokalen Robustheitsversuch erzeugten 1.862 Datentyp-Mutationen strukturierte Ergebnisse ohne Ausnahmeabbruch. Diese Prüfungen authentifizieren keine Belege und entdecken keine unbekannten Appseiten: Die Richtigkeit des Inventars, der Zustandsklassen und der tatsächlichen Beobachtungen bleibt fachlich zu prüfen. Auch ein gültiger Ledger belegt keine ästhetische Exzellenz.

## Noch nicht nachgewiesen

Es gibt bislang keine kontrollierte Vergleichsstudie gegen andere Skills, keine Studie mit repräsentativen Nutzern und keinen protokollierten Installationstest in sämtlichen unterstützten Client-Versionen. Auch ein vollständiger Concept-to-Code-Lauf mit echter Nutzerfreigabe und anschließendem Konformitätsnachweis steht aus. Das [Evaluationsverfahren](../../skills/stn-ultradesign/references/skill-evaluation.md) beschreibt die nächsten überprüfbaren Schritte.

Die veröffentlichten Evaluationsdateien sind ausschließlich synthetische Entwicklungsbeispiele. Sie enthalten keine Daten einer realen Anwenderanwendung. Pfade in den archivierten Aufgaben und Berichten wurden für dieses Repository normalisiert; die Audit-Fixture selbst blieb unverändert.
