# Entwicklerbereiche: API-Zugänge, Webhooks und API-Dokumentation

Recherche und Abruf: **16.09.2026**. Grundlage sind öffentlich zugängliche Originaldokumentationen von Stripe, Google, Atlassian, Apple, GitHub, OpenAPI Initiative, SmartBear, Redocly und OWASP. Alle unten aufgeführten Seiten wurden direkt geöffnet; relevante Inhalte wurden gelesen. Es wurde kein angemeldetes Kundensystem bedient und kein echter Schlüssel erstellt, offengelegt, rotiert oder widerrufen.

Die daraus entwickelte Referenz `references/developer-platforms.md` ist eigenständig formuliert. Tabellen, Entscheidungsschritte und Abnahmeszenarien sind eine eigene Synthese. Fremde Skills, Vorlagen, Codes und Assets wurden nicht übernommen. Veröffentlichte Produktregeln werden als Beispiele gekennzeichnet; Sicherheitsleitlinien und OpenAPI-Spezifikation werden davon getrennt.

## Quellenregister

Alle Quellen: direkt gelesen, Abruf 16.09.2026. „Produkt“ beschreibt einen bestimmten Herstellervertrag; „Spezifikation“ bezeichnet die maßgebliche technische Beschreibung; „Leitlinie“ ist keine automatische Zertifizierung.

| ID | Quelle | Art | Relevanter Befund |
|---|---|---|---|
| D01 | [Stripe API keys](https://docs.stripe.com/keys) | Produkt | Einmalige Anzeige gilt nicht pauschal für alle Schlüssel. Manuell erstellte Live-Secrets unterscheiden sich von bestimmten Stripe-erstellten Schlüsseln. |
| D02 | [Stripe key practices](https://docs.stripe.com/keys-best-practices) | Produkt/Leitlinie | Eingeschränkte Zugriffe, klar vergebene Verwaltungsrechte und Überprüfung der Nutzung gehören zur Schlüsselverwaltung. |
| D03 | [Stripe Workbench](https://docs.stripe.com/workbench/overview) | Produkt | Anfragen, Fehler, Objekte und Ereignisse sind miteinander untersuchbar. Das liefert ein Vorbild für eine zusammenhängende Diagnoseoberfläche. |
| D04 | [Stripe webhooks](https://docs.stripe.com/webhooks) | Produkt | Automatische Wiederholung, manuelles erneutes Senden und fehlende Reihenfolgegarantie müssen auseinandergehalten werden. Manuelles Resend beendet nicht automatisch weitere Wiederholungen. |
| D05 | [Stripe signature errors](https://docs.stripe.com/webhooks/signature) | Produkt | Signaturprüfung hängt vom unveränderten Body und passenden Endpoint-Secret ab. Lokale CLI-Weiterleitung und Dashboard-Endpunkt verwenden unterschiedliche Secrets. |
| D06 | [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) | Produkt | Idempotenz bei API-Anfragen ist ein eigener Mechanismus. Daraus folgt keine automatische Deduplizierung eigener Webhook-Verarbeitung. |
| D07 | [Google API keys](https://docs.cloud.google.com/docs/authentication/api-keys) | Produkt | Standard-API-Schlüssel authentifizieren keinen Principal; gebundene Authorization Keys arbeiten als Service Account. Einschränkungen und Produkthinweise sind wesentlich. |
| D08 | [Google authentication](https://docs.cloud.google.com/docs/authentication) | Produkt/Leitlinie | Menschliche und technische Identitäten sowie mehrere Formen kurzlebiger oder föderierter Authentifizierung sind getrennt beschrieben. |
| D09 | [Google service account key practices](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) | Produkt/Leitlinie | Langfristige Schlüssel benötigen bewusstes Lifecycle-Management; sicherere Alternativen sollen geprüft werden. |
| D10 | [Atlassian token management](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) | Produkt | Persönliche Tokens und Service-Account-Tokens haben eigene Verwaltungswege. Ablauf und Scopes sind sichtbar; Wiederherstellung des Werts ist nicht vorgesehen. |
| D11 | [Atlassian API Access reference](https://developer.atlassian.com/cloud/admin/api-access/rest/api-group-api-token/) | Produkt/API-Vertrag | Verwaltungsoperationen besitzen eigene Rechte. Token-Metadaten umfassen unter anderem Ablauf und letzte Aktivität; dies ist kein Abruf des geheimen Werts. |
| D12 | [Apple App Store Connect API](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api) | Produkt | Persönliche und Team-Keys haben unterschiedliche Wege und Zugriffsmodelle. Private Schlüssel können einmal heruntergeladen werden; Widerruf ist nicht rückgängig zu machen. |
| D13 | [GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | Produkt | Tokenarten und Berechtigungen unterscheiden sich; für geeignete Automatisierungen sind GitHub Apps eine Alternative zum persönlichen Token. |
| D14 | [GitHub webhook practices](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks) | Produkt/Leitlinie | Geheimnisbasierte Prüfung und Delivery-Identifier helfen bei sicherer Verarbeitung und Wiederholung. |
| D15 | [GitHub failed deliveries](https://docs.github.com/en/webhooks/using-webhooks/handling-failed-webhook-deliveries) | Produkt | GitHub wiederholt fehlgeschlagene Webhook-Zustellungen nicht automatisch. Dieser Unterschied zu Stripe muss im Produkt erklärt werden. |
| D16 | [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) | Spezifikation | Publiziert am 10.09.2026; beim Abruf auch Inhalt des offiziellen Latest-Dokuments. Formatversion und dokumentierte API-Version sind unterschiedliche Angaben. |
| D17 | [OpenAPI security](https://learn.openapis.org/specification/security.html) | Offizielle Erläuterung | Sicherheitsdefinitionen und ihre Verwendung pro Operation müssen zusammen gelesen werden. Kombinationen und Alternativen dürfen im UI nicht falsch vereinfacht werden. |
| D18 | [OpenAPI parameters](https://learn.openapis.org/specification/parameters.html) | Offizielle Erläuterung | Parameterort, Serialisierung und Request-Body sind unterschiedliche Vertragsbestandteile. Ein generisches Eingabefeld bildet sie nicht automatisch korrekt ab. |
| D19 | [Swagger UI configuration](https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/) | Werkzeug | Interaktive Ausführung, gespeicherte Autorisierung und externe Validierung besitzen eigene Einstellungen. UI-Voreinstellungen müssen geprüft werden. |
| D20 | [Redocly CORS proxy](https://redocly.com/docs/realm/config/cors-proxy) | Werkzeug/Produkt | Proxy-Funktion und Zielbeschränkung verändern Datenwege. Hinweise gelten für die dokumentierte Edition und Konfiguration. |
| D21 | [OWASP object-level authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/) | Sicherheitsleitlinie | Ressourcenbezogene Autorisierung muss am Backend erfolgen; unsichtbare Schaltflächen verhindern keine unzulässigen direkten Aufrufe. |
| D22 | [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html) | Sicherheitsleitlinie | Serveranfragen an eingetragene URLs benötigen Kontrollen. Dies betrifft Webhook-Tests, Zieladressen und Dokumentations-Proxies. |

## Was wir daraus für das Skill lernen

**Die Informationsarchitektur muss Eigentum und Wirkung zeigen.** Persönliche Tokens gehören zur Person; technische Integrationen benötigen einen dauerhaften Besitzer und einen klaren Organisations-, Projekt- und Umgebungskontext. Die endgültige Navigation hängt vom tatsächlichen Produktmodell ab. Eine globale Seite „API“ ist häufig zu unpräzise. Ebenso gefährlich wäre ein Projektfilter, der lediglich die Liste filtert, während der Schlüssel weiterhin umfassend berechtigt bleibt.

**Ein Administrator ist keine universelle Geheimnisleserolle.** Auflisten, Erstellen, Berechtigungen ändern, Rotieren, Widerrufen und Einsehen sind unterschiedliche Fähigkeiten. Ein Governance-Bereich kann Nutzungsmetadaten und Widerruf anbieten, ohne jemals den geheimen Wert auszuliefern. Das Skill verlangt deshalb eine Aktionsmatrix und passende serverseitige Prüfungen statt eines einzigen Schalters „Admin“.

**Gute Lifecycle-UX berücksichtigt Ausfälle.** Einmalige Anzeige verlangt eine verständliche Übergabe, einschließlich fehlgeschlagenem Kopieren und abgebrochener Erstellung. Geplante Rotation benötigt andere Hinweise als eine bestätigte Kompromittierung. Ablaufzeiten brauchen verständliche Zeitzonen; unbekannte letzte Verwendung darf nicht als unbenutzt ausgegeben werden. Diese Abnahmepunkte sind eigene Gestaltungsvorschläge, die mit realen Backend-Verträgen abgeglichen werden müssen.

**Webhooks brauchen eine Betriebsoberfläche.** Endpunkt, Ereignis, Zustellversuch und fachliche Verarbeitung sind verschiedene Dinge. Ein HTTP-Erfolg beweist keine abgeschlossene Bestellung. Historische Ereignisse erneut zu senden kann Nebenwirkungen auslösen. Deshalb zeigt der Entwurf Ziel, Umgebung, Ereignis und Bedeutung der Wiederholung sowie Diagnose und Wiederherstellung. Deduplizierung ist eine Eigenschaft der Verarbeitung, keine dekorative Checkbox.

**API-Dokumentation ist zugleich Erklärung und mögliche Aktionsoberfläche.** Eine Referenz muss Navigation, Version, Authentifizierung, Eingaben, Schemas, Antworten, Fehler und Beispiele verständlich verbinden. Ein interaktiver Explorer benötigt zusätzlich eindeutige Zielumgebung, sichere Credential-Behandlung und Kenntnis des tatsächlichen Netzwerkpfads. Ein hübscher Swagger- oder Redoc-Bildschirm erfüllt diese Anforderungen nicht automatisch.

**Aktuelle Versionsprüfung ist unverzichtbar.** OpenAPI 3.2.1 war erst sechs Tage vor diesem Abruf veröffentlicht. Das ist kein Grund, bestehende Verträge ungeprüft zu migrieren: Validator, Renderer und Codegenerierung müssen den verwendeten Funktionsumfang unterstützen. Herstellerdokumentation verändert sich ebenfalls; Navigationsnamen, Ablaufregeln, Editionen und API-Verhalten werden bei konkreter Umsetzung neu geprüft.

## Abnahme und Grenzen

Das Referenzmodul enthält konkrete Fälle für Read-only-Integrationen, Kontextwechsel zwischen Staging und Produktion, eingeschränkte Adminsicht, fehlgeschlagene Geheimnisübergabe, Rotation, Ablauf, doppelte und verspätete Webhooks sowie redigierte Diagnoseexporte. Konzept, Zustände und erlaubte Aktionen werden vor Umsetzung besprochen und explizit freigegeben. Anschließend prüft die Umsetzung dieselben Verträge.

Der verpflichtende Vollaudit inventarisiert jede implementierte Seite, Komponentenverwendung, jedes Widget, jeden Drilldown und jeden definierten Workflow-Übergang. Dazu zählen Credential-Untertypen, Berechtigungszustände, Webhook-Verwaltungsoberflächen und sämtliche veröffentlichten Operationen samt Explorer. Gemeinsame Komponenten oder repräsentative Beispiele ersetzen keine Prüfung ihrer einzelnen Verwendung. Nicht erreichbare Zustände bleiben ausdrücklich offene Abdeckungslücken.

Die Recherche enthält keine Live-Verifikation eines Kundensystems und keine Sicherheitszertifizierung. Öffentlich beschriebene Eigenschaften belegen keine Ende-zu-Ende-Sicherheit einer späteren Implementierung. Anbieterbeispiele geben keine universelle Ablaufdauer, keinen einheitlichen Wiederholungszeitraum und keine weltweite Standardschnittstelle für Tokenverwaltung vor. Genau diese Unterschiede soll das Skill sichtbar und überprüfbar machen.
