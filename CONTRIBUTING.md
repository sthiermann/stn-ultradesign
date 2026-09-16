# Mitwirken

Verbesserungen sollen eine konkrete Designentscheidung oder Prüfung verlässlicher machen. Beschreibe im Issue oder Pull Request den Anwendungsfall, das beobachtete Problem und das gewünschte Ergebnis. Bei einer falschen Empfehlung reichen ein minimales Beispiel und ein nachvollziehbarer Gegenbeleg.

## Anforderungen an Beiträge

- **Eigene Inhalte:** Texte, Regeln, Code, Vorlagen und Testdaten selbst erstellen. Keine fremden Skills, Komponentenbibliotheken, Screenshots, Schriftdateien oder Markenassets übernehmen. Öffentliche Prinzipien knapp in eigenen Worten erläutern und die Primärquelle verlinken.
- **Prüfbare Empfehlungen:** Auslöser, Entscheidung, relevante Ausnahme und überprüfbares Ergebnis beschreiben. Standards, Herstellerempfehlungen, Forschung und eigene Annahmen unterscheiden.
- **Passender Umfang:** Den Einstieg in `SKILL.md` knapp halten. Spezialwissen in die passende Referenz aufnehmen. Keine neuen Werkzeuge oder Abhängigkeiten ohne belegten Bedarf.
- **Produktkontext:** Bestehende Marke, Zielgruppe, Aufgaben, Barrierefreiheit und Plattform berücksichtigen. Persönliche Stilvorlieben nicht zu universellen Verboten machen.
- **Nachvollziehbare Ergebnisse:** Keine erfundenen Tests, Nutzerstudien, Screenshots, Freigaben oder Leistungsversprechen. Ein Mockup belegt keine funktionierende Interaktion.
- **Vollständigkeit:** Ein Vollaudit darf keine Seite, Komponentenverwendung, kein Widget, keine Drilldown-Ebene und keinen definierten relevanten Ablauf durch eine Stichprobe ersetzen. Fortsetzbare Etappen und offene Zugriffslücken explizit erfassen.

## Vor dem Pull Request

1. Interne Verweise, Skill-Namen und Metadaten kontrollieren.
2. Für veränderliche Regeln die aktuelle Primärquelle prüfen; Datum, Version und relevante Grenzen nennen.
3. Bei Verhaltensänderungen mindestens einen repräsentativen Auftrag und einen passenden Gegenfall ausführen. Ausgangslage, verwendeten Client, Modell, Werkzeuge und Ergebnis dokumentieren. Für reine Textkorrekturen genügt eine gezielte Prüfung.
4. Änderungen am Audit-Prüfer mit gültigen sowie absichtlich inkonsistenten Datensätzen prüfen. Der Prüfer darf dokumentierte Abdeckung nicht als Nachweis tatsächlicher UI-Qualität ausgeben.
5. Datenschutzgerechte Beispiele verwenden. Keine Kundendaten, Zugangsdaten oder internen Produktbilder veröffentlichen.

Die [Evaluationsreferenz](skills/stn-ultradesign/references/skill-evaluation.md) beschreibt Vergleiche unter kontrollierten Bedingungen. Ein fairer Vergleich verwendet dieselben Aufgaben und Bedingungen, macht Streuung sichtbar und trennt visuelle Präferenz von Aufgabenerfolg.

## Änderungen am Paket

Versionen in den Plugin-Manifesten synchron halten. Installationsanweisungen gegen offizielle Dokumentation und verfügbare Client-Hilfe prüfen. Eine Formatprüfung und ein tatsächlich ausgeführter Installationstest getrennt berichten. Neue Hooks, externe Dienste oder Netzwerkkomponenten sind eine eigene Produktentscheidung.

Mit einem Beitrag bestätigst du, dass du ihn unter der [MIT-Lizenz](LICENSE) dieses Projekts bereitstellen darfst. Erforderliche Quellen- und Rechtehinweise gehören in den Beitrag und gegebenenfalls in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
