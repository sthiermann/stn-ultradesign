# Unabhängiger UI/UX-Audit: Luma Operations

Stand: 16. September 2026. Modus: ausschließlich Audit; die Anwendung wurde nicht geändert.

**Ergebnis:** Alle drei implementierten Seiten und alle im Quelltext definierten Anwendungsaktionen wurden in der laufenden Fixture aufgerufen, einschließlich beider Projekt-Drilldowns, sämtlicher Ausgänge des Löschdialogs und der Webhook-Detailansicht. Dabei wurden erhebliche Probleme bei Formularen, Tastaturbedienung, Dialogen und verlässlicher Rückmeldung bestätigt. **Dies ist noch kein abgeschlossener vollständiger UI/UX- oder WCAG-Audit:** Responsive Ansichten, mehrere Eingabemethoden und die vollständige Prüfung aller anwendbaren WCAG-Kriterien sind offen.

## Prüfgrundlage und tatsächlicher Umfang

- Auftrag: `evals/audit-fixture/task.md`.
- Angewandter Skill: `skills/stn-ultradesign/SKILL.md`; insbesondere `audit-method.md`, `verification.md`, `accessibility.md`, `data-visualization.md`, `business-administration.md` und `developer-platforms.md`.
- Einziger untersuchter Anwendungsquelltext: `evals/audit-fixture/index.html`, 21 Zeilen; SHA-256 `74ee7a4c906066c108c9cb10b3ad81bf8f7ab55062e19ad2f4301b0e4c4d76e3`.
- Laufzeit: `http://127.0.0.1:8767/`, Microsoft Edge unter macOS, eigener Tab. Browser- und Betriebssystemversion wurden nicht erfasst. CUA hatte keinen Browser-Provider; die Prüfung erfolgte über native App-Bedienung, Accessibility Tree und Screenshots.
- Sichtbare Rolle: ausschließlich „member“, Workspace „Example Workspace“, synthetische Identität Casey. Andere Rollen, Mandanten, Featureflags und Konfigurationen sind nicht implementiert.
- Der Browser bestätigte zum Ende 100 % Zoom. Eine kurze Änderung auf 110 % wurde zurückgesetzt. Versuche, 200 % herzustellen, führten zu keinem verifizierten 200-%-Test. Screenshot-Abmessungen von 1280 × 768 sind **keine** Messung des CSS-Viewports.
- Die Fixture besitzt keinen echten Server, keine echten Schlüssel und keine externen Seiteneffekte. Die angebliche Löschung wurde deshalb als autorisierte Simulation ausgeführt.
- Zum Ende meldete CUA, der Mac sei gesperrt und könne nicht automatisch entsperrt werden. Weitere Laufzeittests waren damit blockiert. Der letzte verifizierte Zustand ist `#missing`; ein anschließender Rückkehrversuch wurde durch die Sperre verhindert.

Andere Evaluationsdateien, Bewertungsmaßstäbe und Schlussfolgerungen wurden nicht gelesen. Es gab keine Änderung der App, keine Installation und keine Sicherheitsprüfung eines Backends.

## Evidenzprotokoll

Die folgenden Auszüge stammen aus den tatsächlich zurückgegebenen UI-Zuständen. Screenshots wurden visuell geprüft, aber nicht als separate Bilddateien archiviert; die Belege unten sind Beobachtungsprotokoll, Accessibility-Tree-Auszüge, Quellstellen und berechnete Kontraste.

| ID | Tatsächlich ausgeführte Prüfung und Beobachtung |
|---|---|
| E01 | Einstieg `/`: Overview, Settings und Developers vorhanden. Übersicht zeigt Jan 98 %, Feb 99 %, Mar 100 %, den Satz „Monthly completion increased dramatically.“ und eine Teams-Tabelle. Die drei Zahlen wurden auch im Accessibility Tree als Text ausgegeben. |
| E02 | `Operations →` geöffnet: „Operations projects“ und `Project Linden` erscheinen. Anschließend `Project Linden` geöffnet: Überschrift, „3 overdue tasks“, `Close details`. Schließen entfernt die Detailansicht; Fokus laut Tree danach auf HTML-Inhalt statt Projekt-Auslöser. |
| E03 | Settings: Display name von Casey zu `Casey Updated` geändert; Notification email zu `invalid-email`. Tab aus dem E-Mail-Feld setzt den Fokus direkt auf `Delete workspace`. `Save changes` wird im Tree ausschließlich als Text aufgeführt. |
| E04 | Pointer-Aktivierung von `Save changes`: beide Felder werden auf Casey beziehungsweise casey@example.test zurückgesetzt; Meldung „Server unavailable. Try again.“ erscheint. Keine feldbezogene Validierung vor diesem Ausgang. Erneute Aktivierung mit den wiederhergestellten Standardwerten ergibt denselben Fehlerzustand. |
| E05 | `Delete workspace` öffnet Overlay; Fokus bleibt laut Tree auf dem Hintergrund-Auslöser. Escape schließt es nicht. Tab setzt Fokus auf `×`; Shift+Tab setzt ihn wieder auf den Hintergrund-Auslöser. Das Overlay wird als Container, nicht als benannter Dialog ausgegeben. |
| E06 | Dialog getrennt über `Cancel` und über `×` geschlossen; beide Ausgänge funktionieren visuell, Fokus liegt danach jeweils auf dem HTML-Inhalt. Separat erneut geöffnet und `Delete everything` ausgeführt: nativer Alert „Deletion simulated; no real data changed“. `OK` geschlossen. |
| E07 | Developers: readonly-Feld mit `demo_value_not_a_live_secret`; Scope-Menü mit `Full workspace access` und `Read only`. `Read only` gewählt, `Save` aktiviert: „Changes saved“. Neuladen setzt Scope zurück auf `Full workspace access` und entfernt Meldung. Auch Save im Standard-Scope wurde aufgerufen. |
| E08 | Webhooks zeigt „No deliveries yet.“. `View delivery details` öffnet „Delivery attempts / Loading…“. Die Loading-Anzeige bleibt beim späteren Screenshot bestehen und erscheint nach Navigation/Browser-Zurück weiter. Quelltext besitzt keine Abschluss-, Fehler- oder Retry-Transition. |
| E09 | Navigation Developers → Overview; Browser-Zurück führt zu Developers und erhält seinen lokalen Meldungs-/Drilldown-Zustand; Browser-Vorwärts führt wieder zu Overview. Direkt eingegebenes `#missing` blendet sämtlichen Hauptinhalt aus; Header und Navigation bleiben. |
| E10 | Übersicht, beide Projektstufen, Dialog und Developers mit geöffneten Lieferdetails visuell geprüft. Diagramm-Balken wirken extrem unterschiedlich lang; sekundäre graue Texte sind sehr schwach. Keine formale Pixelmessung aus diesen Screenshots. |
| E11 | Reproduzierbare Kontrastberechnung aus den CSS-Farbwerten, WCAG-sRGB-Linearisierung: `#b9bec7` auf `#f4f6fa` = **1,725:1**; auf Weiß = **1,866:1**. Kontrollwerte: Weiß/`#244bc5` = 7,272:1; `#242b39`/`#f4f6fa` = 13,118:1. Keine Bildkompression als Messgrundlage. |
| E12 | Quelltextprüfung: feste Shellbreite 1200 px ohne Media-/Container-Queries (Z. 7); Balkenbreiten 10/105/220 für Werte 98/99/100 (Z. 11); Save-div ohne Tastatur-/Button-Semantik (Z. 12); globale Dialog-divs ohne Fokuslogik (Z. 15); unbekannte Hashes ohne Fallback (Z. 17–18); Form-reset vor Fehler (Z. 19). |

## Priorisierte Befunde

Die Schweregrade sind die projektinterne Skala des Skills. Es gibt keine belastbare Grundlage für einen prozentualen Design-Score oder behauptete Umsatz-/Effizienzgewinne.

### UX-01 — Hoch: Einstellungen lassen sich per Tastatur nicht speichern

**Ort:** Settings, `Save changes`; Quelltext Z. 12. **Evidenz:** E03, E12; unmittelbar beobachtet.

Reproduktion: Display name bearbeiten, per Tab zum E-Mail-Feld und weiter navigieren. Der nächste Fokus ist `Delete workspace`; die Speicheraktion fehlt in der Fokusfolge und besitzt keine Button-Rolle. Der Text ist als `div` mit ausschließlich `onclick` implementiert.

**Folge:** Eine zentrale Handlung ist für reine Tastaturbedienung blockiert. Dies betrifft WCAG 2.2 [2.1.1 Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) und die fehlende programmatisch erkennbare Rolle unter [4.1.2 Name, Role, Value](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html).

**Empfehlung und Abnahme:** Eine native, korrekt benannte Speicher-Schaltfläche mit Formular-Submit verwenden. Nach Eingabe sind Speichern und Wiederholen per Tab/Enter/Space möglich; der tatsächliche Fehler bleibt zugänglich. Das erfordert keinen gestalterischen Umbau der gesamten Seite.

### UX-02 — Hoch: Speicherfehler vernichtet den bearbeiteten Entwurf

**Ort:** Settings, beide Felder und Fehlerrückmeldung; Z. 12, 19. **Evidenz:** E04; unmittelbar beobachtet und im Handler bestätigt.

Reproduktion: beide Werte ändern und Save aktivieren. Die Anwendung meldet einen Serverfehler, setzt die Eingaben aber vorher zurück. „Try again“ kann damit nicht dieselben Änderungen erneut senden. Auch ein offensichtlich ungültiger E-Mail-Wert erreicht diesen Ausgang; der direkte Klickpfad nutzt die native Formularvalidierung nicht.

**Folge:** Eingabearbeit geht verloren, Ursache und Korrekturmöglichkeit werden verwischt. Der konkrete Verlust ist belegt; ob ein leeres Feld erlaubt wäre, ist dagegen keine dokumentierte Produktregel.

**Basis:** Fehlererholung und wahrheitsgetreue Speicherzustände aus den Skill-Modulen Workflows/Business Administration; die Forderung nach Entwurfserhalt ist hier eine begründete UX-Empfehlung. Kein pauschaler WCAG-Verstoß allein wegen fehlender clientseitiger Validierung wird behauptet.

**Empfehlung und Abnahme:** Bei Fehlschlag Werte bewahren, Feldvalidierung vom Transportfehler trennen, Retry auf denselben Entwurf anwenden. Test: `Casey Updated` und eine gültige geänderte E-Mail bleiben nach simuliertem Serverfehler erhalten; ungültige E-Mail erhält eine verständliche Korrekturanweisung; Wiederholen leert das Formular nicht.

### UX-03 — Hoch: Der Löschdialog besitzt keinen verlässlichen Modalitäts- und Fokusvertrag

**Ort:** Settings → Delete workspace → Overlay; Z. 15. **Evidenz:** E05, E06.

Beim Öffnen bleibt der Fokus auf dem Hintergrund. Escape wirkt nicht; Shift+Tab aus dem Schließen-Control erreicht den Hintergrund. Der Accessibility Tree meldet einen allgemeinen Container. Nach Cancel beziehungsweise × kehrt Fokus nicht zum Auslöser zurück.

**Folge:** Tastatur- und assistive Nutzung können den Kontext und die Reichweite einer folgenreichen Handlung nicht verlässlich verfolgen. Der vorhandene Erklärungstext und die tatsächlich funktionierende Cancel-Aktion sind positiv, reichen aber nicht für das Interaktionsmodell.

**Basis:** [WAI-ARIA APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) ist informative Gestaltungsempfehlung. Fehlende Rollen-/Namensinformation betrifft zusätzlich SC 4.1.2. Nicht jede Abweichung von APG, etwa Escape isoliert betrachtet, ist automatisch ein eigenständiger WCAG-Verstoß.

**Empfehlung und Abnahme:** Passendes natives Dialogverhalten oder vollständig implementierte Modal-Komponente verwenden: Name, geeigneter Startfokus, Hintergrund inaktiv, begrenzte Fokusfolge, Escape/Cancel, Rückkehr zum Auslöser. Alle drei Ausgänge erneut mit Maus und Tastatur prüfen. Kein echtes Löschen ist hier erfolgt oder behauptet.

### UX-04 — Hoch, aus Quelltext stark belegt: Die feste Seitenbreite verhindert eine adaptive Shell

**Ort:** Shell aller drei Seiten, einschließlich lokaler Komponenten und Drilldowns; Z. 7. **Evidenz:** E12; **kein ausgeführter 320-px-Laufzeittest**.

Die Shell ist immer 1200 CSS px breit, mit fest 220 px breiter Navigation und ohne adaptive Regel. Bei einem 320-px-Viewport bleiben damit bereits strukturell 880 px außerhalb der sichtbaren Breite. Formular- und Navigationsinhalte benötigen keine unvermeidliche zweidimensionale Darstellung.

**Folge:** Auf schmalen Ansichten sind wichtige Inhalte voraussichtlich nur durch horizontales Verschieben erreichbar. Desktop-Screenshots allein belegen keine Tablet-/Smartphone-Tauglichkeit.

**Basis:** [WCAG 1.4.10 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), einschließlich seiner Ausnahmen. Eine mögliche Ausnahme für einzelne Tabellen würde nicht die gesamte feste Shell freistellen.

**Empfehlung und Abnahme:** Fluiden Hauptbereich und eine passende schmale Navigation spezifizieren. Alle drei Seiten, jede aufgeklappte Ebene und den Dialog bei 320 CSS px sowie sinnvollen mittleren/breiten Größen tatsächlich bedienen. Lokales Tabellen-Scrolling nur dort einsetzen, wo die Aufgabe es rechtfertigt. Der Dialog hat Flex-Shrink; aus `width:450px` allein wird ausdrücklich kein gesonderter 498-px-Mindestbreitenfehler abgeleitet.

### UX-05 — Mittel: Das Diagramm überzeichnet eine Veränderung von zwei Prozentpunkten

**Ort:** Overview → Completion rate; Z. 11. **Evidenz:** E01, E10, E12.

Die Beschriftungen lauten 98, 99, 100 %, die Balkenbreiten dagegen 10, 105, 220. Der letzte Balken ist 22-mal so lang wie der erste. Auch gleiche Wertabstände erzeugen ungleiche Längenzuwächse: 95 und 115 px. Eine lineare, gemeinsame Skala erklärt diese Darstellung deshalb nicht. „Increased dramatically“ verstärkt den Eindruck; eine fachliche Bedeutung dieser Wortwahl ist nicht dokumentiert. „Current month“ über der Darstellung passt außerdem nicht eindeutig zu drei Monatswerten ohne Jahresangabe.

**Folge:** Die Anzeige kann eine deutlich größere quantitative Veränderung suggerieren, als die Zahlen belegen.

**Basis:** Numerische Konsistenz; Skill Data Visualization; [ONS zu Achsen und Skalen](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines).

**Empfehlung und Abnahme:** Für Balken eine gemeinsame, nachvollziehbare Größenskala verwenden oder ein geeignetes Punkt-/Linienformat mit sichtbar erklärtem Wertebereich wählen. Veränderung als +2 Prozentpunkte ausdrücken, Zeitraum eindeutig benennen, behauptete Bewertung fachlich begründen. Die Textwerte sind im geprüften Accessibility Tree vorhanden; ein vollständig unsichtbares Diagramm für Screenreader wird nicht behauptet. Struktur und Verständlichkeit mit einem echten Screenreader bleiben zu testen.

### UX-06 — Mittel: Sekundärtext unterschreitet den Textkontrast deutlich

**Ort:** Header auf allen drei Seiten; Overview „Status for the current month“; Z. 7, 9, 11. **Evidenz:** E10, E11.

Die beiden normalen Text-/Hintergrundkombinationen erreichen nur 1,866:1 beziehungsweise 1,725:1. Diese Texte sind weder inaktive Controls noch Logos oder beiläufige Textbestandteile eines Bildes.

**Basis:** [WCAG 1.4.3 Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), Ziel 4,5:1 für normalen Text. Der Befund gilt für diese konkreten Textverwendungen, nicht pauschal für jede graue Linie.

**Empfehlung und Abnahme:** Sekundärtextfarbe an beiden tatsächlichen Hintergründen auf mindestens 4,5:1 bringen und sämtliche Header-Verwendungen prüfen. Primärtext und weißer Speichertext auf Blau bestanden die hier berechneten statischen Farbpaarprüfungen; das ist kein vollständiger Kontrast-Pass sämtlicher Zustände.

### UX-07 — Mittel: „Changes saved“ behauptet eine Speicherung, die nicht stattfindet

**Ort:** Developers → Scope/Save; Z. 13. **Evidenz:** E07.

`Read only` wählen, Save aktivieren, neu laden: Die Anzeige springt zu `Full workspace access` zurück. Der Handler ändert ausschließlich den Rückmeldetext. Das ist eine belegte Diskrepanz des Prototypverhaltens, **kein** Nachweis einer tatsächlichen Berechtigungsänderung oder Sicherheitslücke.

**Folge:** Eine Person kann glauben, den Zugriff eingeschränkt zu haben. Auch in einer Demo sollte ein simuliertes Ergebnis als solches erkennbar sein.

**Empfehlung und Abnahme:** Entweder die Simulation transparent benennen oder einen klar definierten speicherbaren Testzustand einführen. In einer späteren echten Anwendung erst nach bestätigter Speicherung Erfolg melden und gespeicherte von wirksamen Berechtigungen unterscheiden. Nach Reload muss der sichtbare Zustand zum versprochenen Vertrag passen; Backend-Enforcement erfordert eine getrennte autorisierte Prüfung.

### UX-08 — Mittel: Webhook-Drilldown endet dauerhaft in einem widersprüchlichen Ladezustand

**Ort:** Developers → Webhooks → View delivery details; Z. 13. **Evidenz:** E08 und vollständiger Handler-Quelltext.

Trotz „No deliveries yet“ öffnet die Detailaktion „Delivery attempts / Loading…“. Es gibt weder einen Request noch eine definierte Transition zu Ergebnis, Leerzustand oder Fehler. Eine bloß längere Wartezeit würde den Quelltext-bedingten Stillstand nicht lösen.

**Folge:** Die Person kann nicht unterscheiden, ob überhaupt Daten existieren, ob etwas bearbeitet wird oder welche Handlung hilft.

**Empfehlung und Abnahme:** Für diese leere Fixture einen ehrlichen abgeschlossenen Leerzustand zeigen. Falls ein echter Abruf vorgesehen ist, Lade-, Leer-, Ergebnis-, Fehler- und angemessenen Retry-Zustand definieren. Detailansicht nie ohne laufende Arbeit als dauerhaft ladend ausgeben. Keine echten Webhook-Zustellungen oder Provider-Retryregeln wurden getestet.

### UX-09 — Mittel: Speicher-Rückmeldungen haben keine programmatische Statussemantik

**Ort:** Settings `#save-status`, Developers `#key-status`; Z. 12–13, 19. **Evidenz:** E04, E07 plus Quelltext.

Beide Rückmeldungen werden in gewöhnliche leere Absätze geschrieben, ohne Live-Region-/Status-/Alert-Semantik. Der Fehler oder Erfolg erscheint visuell ohne gezielte Fokusführung. Die vorhandenen Textknoten sind im Tree lesbar; das beweist keine spontane Ankündigung.

**Basis:** [WCAG 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html). **Vertrauen:** fehlender programmatischer Mechanismus aus Quelltext belegt; tatsächlich gesprochene Ausgabe wurde nicht gehört.

**Empfehlung und Abnahme:** Geeignete, bereits im DOM vorhandene Rückmelderegion mit passender Dringlichkeit implementieren. Erfolg und Fehler einmal verständlich ankündigen; Wiederholen darf weder still bleiben noch unnötig mehrfach unterbrechen. Danach mit den vorgesehenen Browser-/Screenreader-Kombinationen prüfen.

### UX-10 — Niedrig: Unbekannte Direktlinks führen zu leerem Hauptinhalt

**Ort:** Hash-Navigation; Z. 17–18. **Evidenz:** E09.

Direktes Öffnen von `#missing` lässt den Hauptbereich leer. Navigation und Header bleiben vorhanden, sodass kein vollständiger Ausstieg blockiert ist. Für einen ungültigen, veralteten oder falsch eingegebenen Link fehlen jedoch Erklärung und definierter Fallback.

**Empfehlung und Abnahme:** Eindeutigen Nicht-gefunden-Zustand oder sinnvolle Standardroute vorsehen. Direktlinks auf alle bekannten Seiten, unbekannten Hash, Reload sowie Browser-Zurück/Vorwärts prüfen. Innerhalb der getesteten gültigen Seiten funktionierten Browser-Zurück/Vorwärts.

## Zusätzliche Vertragsfragen und zurückgehaltene Behauptungen

- Settings mischt personenbezogen wirkende Felder und Workspace-Löschung. Die Überschrift „Workspace actions“ trennt bereits einen Bereich. Ob Display name und Notification email global, workspacebezogen oder gemeinsam gelten, ist nicht dokumentiert. Vor einer Neuordnung den tatsächlichen Eigentümer und Wirkungsbereich klären; kein erfundenes Organisationsmodell einführen.
- Die Aussage „All members can manage workspace keys“ ist expliziter Fixture-Inhalt. Es gibt keine Grundlage, eine abweichende Owner-only-Regel als weltweiten Standard aufzuzwingen. Wer löschen oder Schlüssel verwalten darf, benötigt einen echten Produktvertrag und serverseitige Prüfung.
- `demo_value_not_a_live_secret` ist erkennbar synthetisch. Dies ist kein nachgewiesenes Secret-Leak. Maskierung allein wäre im echten Produkt außerdem keine Autorisierung.
- Der Close-Button ist laut CSS 14 × 14 px. Das ist ein Kandidat für bessere Bedienbarkeit, aber **kein automatisch nachgewiesener Verstoß gegen WCAG 2.5.8**: Abstands- und Gleichwertigkeitsausnahmen müssen mit tatsächlicher Geometrie geprüft werden. Cancel bietet hier zusätzlich einen anderen Schließweg. 44 × 44 CSS px ist keine pauschale AA-Vorgabe.
- Bei den Projekt-Drilldowns fehlen programmatisch sichtbare Aufklappzustände; nach Close details geht Fokus zum HTML-Inhalt. Für die Verfeinerung empfiehlt sich ein klarer Disclosure-/Fokusvertrag mit Rückkehr zu Project Linden. Es wird keine ungetestete Screenreader-Unbenutzbarkeit behauptet.
- Kein „moderneres“ Font, Farbschema, Glass-Effekt oder zusätzliche Animation ist allein wegen Geschmack erforderlich. Die vorhandenen nativen Labels, Tabellenüberschriften, Hauptüberschriften und klare Textbenennung der Löschfolge sind brauchbare Grundlagen.

## Inventar und Abdeckungsmatrix

`pass` bezieht sich ausschließlich auf den benannten ausgeführten Check; `fail` bedeutet geprüft mit Befund. Responsive-, AT- und weitere offene Querschnittschecks sind unten getrennt aufgeführt. Ein besuchtes Element ist nicht automatisch insgesamt bestanden.

| Einheit / konkrete Verwendung | Geprüfter Zustand oder Übergang | Ergebnis und Evidenz |
|---|---|---|
| Shell: Header, Main-Navigation mit drei Links, Hauptbereich; je auf Overview/Settings/Developers | Inhalte, Labels, Routenwechsel, visuelle Gruppierung | **fail** Kontrast/Adaptive-Quelle; Links funktionieren (E01, E09–E12) |
| Overview: h1 und sekundäre Periodenzeile | initial | **fail** Kontrast und unklare Periodenbeschreibung (E01, E11) |
| Completion-Widget: h2, SVG mit drei Labels/Balken, Fazit | sämtliche vorhandenen Werte | **fail** Skalierung (E01, E10, E12) |
| Teams-Widget: h2, Tabelle, beide Header, einzige Zeile, Owner, Operations-Button | initial, Öffnen | **pass** vorhandene Inhalte/erste Transition; weitere Accessibility-Dimensionen offen (E01–E02) |
| Operations-Drilldown: h3, Project-Linden-Button | öffnen, Projekt öffnen | **pass** definierte Öffnungen; Aufklappsemantik verbesserungsbedürftig (E02) |
| Project-Linden-Detail: h4, Aufgabenstatus, Close-details-Button | öffnen/schließen | **fail** Fokus nach Schließen; Inhalte erreichbar (E02) |
| Settings: h1, beide Label/Input-Verwendungen | Ausgangswerte, Textbearbeitung, ungültige E-Mail, Tab-Folge | **pass** Labels/Eingabe; Validierungsvertrag unvollständig (E03–E04) |
| Settings: Save-div und Rückmeldung | Klick, Fehler, Retry; Tastaturversuch | **fail** UX-01/02/09 (E03–E04) |
| Settings: Workspace-actions-h2, Delete-workspace-Button | öffnen | **pass** Auslöser und erklärter Zielbereich; Modalvertrag fail (E05) |
| Lösch-Overlay: Container, Titel, Erklärung | geöffnet, Escape, Fokusfolge | **fail** UX-03 (E05) |
| Dialog: × | schließen | **pass** Sichtbarkeit; **fail** Fokusrückkehr (E06) |
| Dialog: Cancel | abbrechen | **pass** Sichtbarkeit; **fail** Fokusrückkehr (E06) |
| Dialog: Delete everything | simuliert bestätigen | **pass** angekündigter Simulationsausgang (E06) |
| Browser-Alert: Erklärung, OK | quittieren | **pass** lokale Bestätigung (E06) |
| Developers: h1, API-credentials-h2, Richtlinientext, Key-Label, readonly-Keyfeld | Ausgangszustand | **pass** Inhalt/zugänglicher Feldname; keine echte Secret-/Backendprüfung (E07) |
| Developers: Scope-Label und natives Select | beide definierten Optionen | **pass** Auswahl erreichbar (E07) |
| Developers: Save und Rückmeldung | Save in beiden Scopes, Reload nach Read only | **fail** UX-07/09 (E07) |
| Webhooks: h2 und Leertext | leer | **fail** Widerspruch zur Folgeansicht (E08) |
| Webhooks: View-delivery-details-Button, h3, Loading-Text | öffnen, erneute Navigation/Rückkehr | **fail** UX-08 (E08–E09) |
| Router-Zusatzfall | unbekannter Hash | **fail** UX-10 (E09) |

**Besuchszahlen:** 3/3 implementierte Hauptseiten; 2/2 verschachtelte Projekt-Drilldowns; 1/1 Webhook-Drilldown; 1/1 anwendungsseitiges Overlay mit 3/3 definierten Ausgängen; 1/1 daraus erzeugter nativer Alert. Beide Scope-Optionen und beide Save-Handler wurden aktiviert. Alle expliziten App-Handler in `index.html` wurden ausgeführt; wiederholte Schleifen wurden nicht als neue Implementierungszweige gezählt. Der fehlerhafte Verlauf gilt als untersuchte Abdeckung, keinesfalls als bestandene Produktqualität.

## Was vor einer vollständigen Audit-Aussage noch fehlt

| Offene Dimension | Status, konkreter nächster Test |
|---|---|
| Responsive Integration sämtlicher obiger Verwendungen | **blocked** durch gesperrten Mac; 320 CSS px, Tabletbreite, breites/kurzes Fenster, aufgeklappte Zustände und Dialog prüfen. Feste Shell ist bereits aus Quelle beanstandet. |
| Zoom und Textanpassung | **not-tested** bei 200 %/Reflow-Zielgröße; echte Zoomwerte bestätigen, Text-Spacing-Overrides und lange Eingaben prüfen. 110 % ist kein Ersatz. |
| Vollständige Tastaturbedienung | **teilweise getestet**; Save-Barriere/Modalfokus belegt, aber noch nicht jede Aktion mit jeder zutreffenden Taste und jede lokale Navigation vollständig wiederholt. |
| Screenreader | **not-tested**; Accessibility Tree ist kein Hörtest. Dialogöffnung/-schluss, Diagrammbedeutung, Felder, Meldungen und Drilldowns mit realem Screenreader prüfen. |
| Pointer-Zielgrößen/Fokusdarstellung | **not-tested** als vollständige geometrische/visuelle Matrix; besonders × inklusive zulässiger Ausnahmen und alle fokussierten Nutzungen prüfen. |
| Touch und On-Screen-Keyboard | **not-tested**; keine reale Tablet-/Smartphonebedienung. |
| Vollständiges WCAG-2.2-A/AA-Kriterienregister | **not-tested** als Gesamtprüfung; sämtliche anwendbaren Kriterien mit Nachweis beziehungsweise begründetem N/A abgleichen. Die genannten Befunde sind kein Zertifikat. |
| Forced Colors, weitere Inhaltslängen | **not-tested**; vorhandene Steuerelemente unter diesen Nutzungsbedingungen prüfen. Keine implementierte zweite Theme-/Localevariante gefunden. |
| Rollen-, Tenant-, Auth-, echte API-/Webhook- und Offline-Serverfälle | **not-applicable für diese reine Fixture**; es gibt keine Implementierung oder reale Gegenstelle. Eine spätere Produktionsaussage würde diese Bereiche ausdrücklich neu in den Umfang aufnehmen. |
| Nutzerverständnis und Aufgabenverbesserung | **not-tested**; repräsentative Nutzer müssten Perioden, Scope und Fehlererholung verstehen. Kein belegter Verbesserungsfaktor. |
| Weitere Browser/Performance | **not-tested**; kein Cross-Browser-, Geräte-, Last- oder Feldperformance-Pass. Keine gemessenen Leistungsversprechen. |

**Nächste sinnvolle Reihenfolge:** Zuerst Speicherzugänglichkeit und Entwurfserhalt, anschließend den Modalvertrag und die adaptive Shell beheben; danach Diagramm, Kontrast, verlässliche Speicher-/Ladezustände und Statusankündigungen. Für eine tatsächliche Umsetzung wären die betroffenen Zustände im Konzept zu präzisieren und gegebenenfalls freizugeben. Der vorliegende Auftrag bleibt ein Audit ohne App-Änderung. Vor dem Abschluss eines vollständigen Audits müssen die offenen anwendbaren Prüfungen mit Belegen geschlossen werden; ein bloßes Umbenennen dieser Prüfung in „vollständig“ wäre nicht gerechtfertigt.
