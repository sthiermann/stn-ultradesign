# Synthetische Evaluationen

Diese Dateien wurden für die Entwicklung von STN Ultradesign selbst erstellt. Sie enthalten keine echte Kundenanwendung, keine gültigen Zugangsdaten und keine produktiven Integrationen.

| Aufgabe | Eingabe | Archiviertes Ergebnis |
| --- | --- | --- |
| Vollständigen Audit durchführen, Grenzen offenlegen | [Auftrag](audit-fixture/task.md), [absichtlich fehlerhafte Mini-Anwendung](audit-fixture/index.html) | [Auditbericht](audit-result.md) |
| Konzept vor Produktionsfreigabe entwickeln | [Brief](concept-fixture/brief.md) | [Konzept](concept-output/index.html), [Review](concept-output/review.md), [Vertrag](concept-output/design-contract.md), [Prüfprotokoll](concept-output/verification.md) |

Für einen unabhängigen Wiederholungslauf nur den jeweiligen Auftrag, den Skill und die dort genannten Eingaben geben. Das archivierte Ergebnis darf dem evaluierenden Agenten nicht vorab als Musterantwort dienen. Neue Ergebnisse unter `work/evaluation/` ablegen, damit die hier dokumentierte Ausgangsevaluation erhalten bleibt.

Die Audit-Fixture enthält bewusst Defekte. Sie ist weder ein Produktionsstarter noch eine empfohlene Komponentenimplementierung. Bei Bedarf ausschließlich lokal aus dem Repository-Stamm bereitstellen:

```sh
python3 -m http.server 8767 --bind 127.0.0.1 --directory evals/audit-fixture
```

Die HTML-Dateien benötigen keine externen Ressourcen. Aktuelle Browser-/Werkzeugverfügbarkeit und tatsächlich durchgeführte Tests beim Wiederholen neu protokollieren. Die [Qualitätsübersicht](../docs/quality/evaluation.md) erklärt die Grenzen der bisherigen Ergebnisse.
