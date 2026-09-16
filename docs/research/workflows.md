# Recherche: Workflows, Barrierefreiheit, Identität und Berechtigungen

Recherche- und Zugriffsdatum: **16. September 2026**. Verwendet wurden öffentlich zugängliche Primärquellen der jeweiligen Herausgeber. Die operativen Module sind eigenständig formuliert; fremde Skills, Quelltexte, Vorlagen oder Assets wurden nicht übernommen. Dieser Bericht ordnet Quellen und Grenzen ein. Die ausführlichen, direkt anwendbaren Prüfverfahren stehen in `skills/stn-ultradesign/references/`.

## Ergebnis und notwendige Unterscheidungen

Ein belastbarer Design-Skill braucht drei getrennte Ebenen: technische Anforderungen mit prüfbaren Kriterien, kontextgebundene veröffentlichte Gestaltungsmuster und eigene begründete Produktentscheidungen. Diese Ebenen dürfen im Audit nicht unter dem gemeinsamen Etikett „weltweiter Standard“ verschwinden. Dieselbe Bildschirmgestaltung kann in einer öffentlichen Antragsstrecke sinnvoll und in einem häufig benutzten professionellen Editor hinderlich sein.

WCAG 2.2 ist eine W3C Recommendation; die aktuell veröffentlichte Fassung trägt das Datum 12. Dezember 2024. Ihre Erfolgskriterien und Konformitätsregeln sind von erläuternden Understanding-Dokumenten zu unterscheiden. AA umfasst die zutreffenden A- und AA-Kriterien. Eine geprüfte Komponente allein belegt keine Konformität eines vollständigen Prozesses. [Quelle 1](https://www.w3.org/TR/WCAG22/)

Die präzise Einstufung verhindert typische Fehlbehauptungen: 24×24 CSS-Pixel sind der AA-Ausgangspunkt für Zielgrößen mit definierten Ausnahmen; 44×44 ist das gesonderte AAA-Kriterium. Ein gewünschtes größeres Touch-Ziel bleibt eine sinnvolle Produktentscheidung, muss aber richtig begründet werden. Focus Appearance ist AAA; Focus Not Obscured Minimum ist AA und verbietet vollständiges Verdecken durch vom Autor erzeugten Inhalt. [Quelle 2](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [Quelle 4](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [Quelle 5](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

Die WAI-ARIA Authoring Practices sind Umsetzungshilfen, keine Zusicherung, dass jedes Beispiel in jeder Browser-/Hilfsmittelkombination sofort produktionsreif funktioniert. COGA ist ergänzende kognitive Gestaltungshilfe, kein weiterer WCAG-Konformitätskatalog. Das Prüfverfahren muss deshalb technische Tests, reale Interaktion und menschliches Urteil verbinden. [Quelle 11](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/), [Quelle 12](https://www.w3.org/TR/coga-usable/), [Quelle 13](https://www.w3.org/WAI/test-evaluate/tools/selecting/)

Für Authentifizierung ist die finale NIST SP 800-63B-4 vom Juli 2025 maßgeblich für Aussagen über diesen NIST-Stand; ältere Entwürfe unterscheiden sich. Die Veröffentlichung ist keine pauschale Rechtsvorschrift für jede weltweite Anwendung. Die konkrete Assurance- und Organisationsrichtlinie muss vor einer Änderung geklärt sein. [Quelle 22](https://pages.nist.gov/800-63-4/sp800-63b.html)

## Konsequenz für unseren Skill

Die folgenden Punkte sind die eigene Synthese dieser Recherche:

1. **Workflows als Verträge formulieren.** Vor Implementierung müssen Akteur, Kontext, Einstieg, Voraussetzungen, Zustände, Übergänge, Validierung, Zurück/Abbrechen, Unterbrechung, Wiederaufnahme, Seiteneffekte und Erfolg feststehen. Desktop, Tablet, Smartphone, Tastatur und Hilfsmittel gehören zum selben Vertrag.
2. **Erst ein prüfbares Konzept abstimmen.** Das Konzept enthält reale Inhalte und relevante Fehlerzustände. Nach Verfeinerung und Nutzerfreigabe wird es nachvollziehbar umgesetzt. Materielle Abweichungen erfordern eine sichtbare Konzeptänderung, keine stillschweigende Umgestaltung.
3. **Die tatsächliche Anwendung inventarisieren.** Routen, Rollen, Zustände und externe Schritte ergeben den Prüfumfang. Nicht zutreffende Muster werden begründet ausgeschlossen. Eine endlose pauschale Liste ersetzt keine vollständige Abdeckung der konkreten Software.
4. **Bedeutungen trennen.** Leer, gefiltert leer, fehlende Berechtigung, Ladefehler, veraltet und offline sind unterschiedliche Zustände. Lokal gespeichert, zur Synchronisierung vorgemerkt und serverseitig gespeichert sind unterschiedliche Zusagen.
5. **Fehlerfolgen prüfen.** Wiederholen darf Zahlungen, Einladungen und Veröffentlichungen nicht unbeabsichtigt duplizieren. Abbrechen, Schließen und serverseitig Beenden sind unterschiedliche Vorgänge. Bei unbekanntem Ergebnis muss eine sichere Statusprüfung möglich sein.
6. **Sicherheitsgrenzen ausweisen.** Das Frontend erklärt Berechtigungen; ein ausgeblendeter Knopf beweist keine serverseitige Zugriffskontrolle. Ein schönes Passkey-Dialogdesign ersetzt weder Kontowiederherstellung noch korrekt implementierte Protokolle.
7. **Verbesserung messbar machen.** Aufgabenabschluss, kritische Fehler, Erholung nach Fehlern, Zeit bis zum nutzbaren Ergebnis und Verständlichkeit sind die relevanten Vergleichsgrößen. Visuelle Modernität und tatsächliche Gebrauchstauglichkeit erhalten getrennte Evidenz.

## Musterwahl und fachliche Grenzen

GOV.UK empfiehlt, Frageprozesse zunächst mit einer Frage je Seite zu gestalten. Daraus folgt keine allgemeine Pflicht, professionelle Einstellungsoberflächen in viele einzelne Seiten zu zerlegen. USWDS beschreibt seinen Schrittindikator für lineare Sequenzen und grenzt nichtlineare beziehungsweise dynamisch verzweigte Formulare ab. Diese Unterschiede werden im Skill als Entscheidungsregeln erhalten. [Quelle 14](https://design-system.service.gov.uk/patterns/question-pages/), [Quelle 18](https://designsystem.digital.gov/components/step-indicator/)

FIDO dokumentiert sowohl Passkey-Verwaltung als auch Anmeldung und Rückfallmöglichkeiten. Der Geltungsbereich ist zu beachten: Consumer-UX mit synchronisierten Passkeys ist nicht automatisch die Sicherheitsrichtlinie einer regulierten Organisation. [Quelle 23](https://www.passkeycentral.org/design-guidelines/required-patterns/), [Quelle 24](https://www.passkeycentral.org/design-guidelines/principles)

OWASP trennt Authentifizierung von Autorisierung und verlangt in seiner Autorisierungshilfe die Prüfung von Berechtigungen bei jeder Anfrage. Mandantenwechsel brauchen außerdem einen verlässlichen Kontext über Daten, Cache und Hintergrundarbeit hinweg. Diese Aussagen werden im Designaudit als Integrationsabhängigkeiten geführt; backendseitig nicht geprüfte Sicherheit wird ausdrücklich offen gelassen. [Quelle 26](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [Quelle 29](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)

Die operativen Module behandeln außerdem Upload/Import/Export, Suche/Filter/Bulk-Auswahl, Benachrichtigungen, destruktive Aktionen, Kauf/Abonnement/Kündigung, Zusammenarbeit und KI-Workflows. Die ergänzenden Primärlinks stehen direkt neben den entsprechenden Aussagen in den Modulen. Es wird weder behauptet, dass alle Branchen ein einheitliches Verfahren hätten, noch dass die bloße Umsetzung eines Musters Rechtskonformität nachweise.

## Was HTML, CSS und React dafür beherrschen müssen

Diese Lernziele sind eigene technische Ableitungen:

- **HTML:** native Aktionen und Navigation, sichtbare Labels, Gruppen/Legenden, angemessene Tabellenstruktur, Eingabezweck, Dateieingaben, Formularabschluss und semantische Statusdarstellung.
- **CSS:** belastbare Reflow-Layouts, Textvergrößerung und Spacing-Overrides, tatsächliche Hit-Areas, Fokusdarstellung, hohe Kontraste, lange Inhalte, Hilfsmittelmodi sowie Overlays ohne abgeschnittene Aktionen.
- **React:** explizite Zustände statt widersprüchlicher boolescher Flags, stabile Objektidentität, korrekte Fokusziele nach Übergängen, synchronisierte Formularwerte, Behandlung veralteter Antworten und Fehlergrenzen ohne Verlust der Wiederherstellbarkeit.
- **Integration:** fachlich wahre Speicher- und Prozesszustände, sichere Wiederholung, serverseitige Validierung, Berechtigungsmatrix, Session-Ablauf, Mandantenkontext und nachvollziehbare Grenzen der Frontendprüfung.
- **Qualitätssicherung:** reale Tastatur- und Screenreader-Wege, schmale und vergrößerte Ansicht, Fehler/Rückkehr/Unterbrechung, Rollenwechsel, parallele Bearbeitung und Vergleich zur freigegebenen Konzeptrevision.

## Verifizierter Kernkatalog: 30 Primärquellen

Alle Links wurden am **2026-09-16** geöffnet oder ihr Primärinhalt über die Recherche abgerufen. Laufende Hilfeseiten haben nicht überall ein belastbares Veröffentlichungsdatum; deshalb wird ihr Zugriffstag dokumentiert.

| Nr. | Herausgeber und direkte Quelle | Funktion im Skill |
|---|---|---|
| 1 | [W3C – WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Normative Grundlage und Konformitätsumfang |
| 2 | [WAI – Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | Zielgrößen einschließlich Ausnahmen |
| 3 | [WAI – Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Reflow und zweidimensionale Inhalte |
| 4 | [WAI – Focus Not Obscured Minimum](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) | Sichtbarkeit bei Overlays und Sticky-Flächen |
| 5 | [WAI – Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html) | AAA von AA sauber unterscheiden |
| 6 | [WAI – Accessible Authentication Minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) | Kognitive Barrieren in der Anmeldung |
| 7 | [WAI – Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) | Wiederholte Eingaben im gleichen Prozess |
| 8 | [WAI – Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | Resilienz gegen Nutzeranpassung |
| 9 | [WAI – Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) | Pointer-Alternative zusätzlich zur Tastatur |
| 10 | [APG – Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Fokus, Modalität und Rückkehr |
| 11 | [APG – Read Me First](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) | ARIA-Grenzen und Interoperabilität |
| 12 | [W3C – COGA Content Usable](https://www.w3.org/TR/coga-usable/) | Ergänzende kognitive Gestaltungshilfe |
| 13 | [WAI – Selecting Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | Grenzen automatisierter Prüfung |
| 14 | [GOV.UK – Question Pages](https://design-system.service.gov.uk/patterns/question-pages/) | Kontextbezogene Frageprozesse |
| 15 | [GOV.UK – Validation](https://design-system.service.gov.uk/patterns/validation/) | Fehlerauffindbarkeit und Korrektur |
| 16 | [GOV.UK – Check Answers](https://design-system.service.gov.uk/patterns/check-answers/) | Überprüfung vor Abschluss |
| 17 | [GOV.UK – Complete Multiple Tasks](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/) | Nichtlineare Aufgabenpakete |
| 18 | [USWDS – Step Indicator](https://designsystem.digital.gov/components/step-indicator/) | Passender Einsatz eines Fortschrittsindikators |
| 19 | [USWDS – Progress Easily](https://designsystem.digital.gov/patterns/complete-a-complex-form/progress-easily/) | Komplexe Formulare und Wiederaufnahme |
| 20 | [GOV.UK – Confirmation Pages](https://design-system.service.gov.uk/patterns/confirmation-pages/) | Abschlussnachweis und nächste Schritte |
| 21 | [GOV.UK – Create Accounts](https://design-system.service.gov.uk/patterns/create-accounts/) | Begründung einer Kontopflicht |
| 22 | [NIST – SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) | Aktueller Identitäts- und Authentifizierungsstand |
| 23 | [FIDO – Required Passkey Patterns](https://www.passkeycentral.org/design-guidelines/required-patterns/) | Anmeldung und Verwaltung als Einheit |
| 24 | [FIDO – Passkey Principles](https://www.passkeycentral.org/design-guidelines/principles) | Consumer-UX und Sicherheitsgrenzen |
| 25 | [OWASP – Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Kontodisclosure und Anmeldefehler |
| 26 | [OWASP – Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Durchsetzung von Berechtigungen |
| 27 | [OWASP – Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) | Wiederherstellung als eigener Prozess |
| 28 | [OWASP – Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Ablauf, Logout und Sicherheitsereignisse |
| 29 | [OWASP – Multi-Tenant Security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html) | Mandantenkontext und Isolation |
| 30 | [Android – Runtime Permissions](https://developer.android.com/training/permissions/requesting) | Kontextbezogene Rechteanfrage und Ablehnung |

## Gelieferte Module und verbleibende Prüfgrenze

- `references/workflows.md`: Entscheidungsregeln und vollständige Zustands-/Übergangsverträge für 22 Prüfbereiche.
- `references/accessibility.md`: WCAG-Einstufungen mit Ausnahmen und ein eigenständiger manueller/automatisierter Prüfablauf; der vollständige Kriterienkatalog bleibt zusätzlich verpflichtend zu inventarisieren.
- `references/identity-permissions.md`: Identitätslebenszyklus, Berechtigungen, Passkeys, Wiederherstellung und Mandantenwechsel mit expliziter Backend-Grenze.

Noch nicht belegt ist die Wirksamkeit des zusammengestellten Skills an einer realen Anwendung. Dafür braucht es einen Pilot mit derselben Ausgangsaufgabe vor und nach dem Eingriff, festgehaltener Konzeptfreigabe und nachvollziehbaren Nutzungsergebnissen. Die Recherche begründet die Methode; sie ersetzt diesen Wirksamkeitsnachweis nicht.
