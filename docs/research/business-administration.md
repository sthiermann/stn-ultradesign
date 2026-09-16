# Recherche: Administration echter Business-Anwendungen

**Zugriff und Prüfung: 16. September 2026.** Untersucht wurden offizielle Produktdokumentationen von Atlassian, Google, Apple und Stripe. Das zugehörige Modul `skills/stn-ultradesign/references/business-administration.md` wurde eigenständig entwickelt; fremde Skills, Codes, Assets und Vorlagen wurden nicht übernommen. Produktfakten sind von unseren eigenen Gestaltungsempfehlungen getrennt.

## Zentrales Ergebnis

Gute Administration organisiert Einstellungen nach ihrer Wirkung: auf eine Person, eine Mitgliedschaft, eine Organisation, ein Projekt, ein Objekt, ein Abrechnungskonto oder eine technische Integration. Ein einziges unspezifisches Einstellungsmenü verbirgt diese Unterschiede. Ebenso unzuverlässig ist eine pauschale Rollenleiter „Nutzer < Admin < Owner“: Die untersuchten Produkte verteilen konkrete Fähigkeiten auf unterschiedliche Rollen, Geltungsbereiche und Bedingungen.

Unsere Ableitung: Vor einer visuellen Überarbeitung muss der Skill die tatsächlichen Ressourcen, Rollen und Zuständigkeiten der Anwendung verstehen. Für jede Einstellung werden Ort, Wirkung, Lese- und Schreibrecht, verbindliche Datenquelle, Vererbung, Speicherung und Zeitpunkt der Wirksamkeit dokumentiert. Die Rechteverwaltung bleibt serverseitig zu prüfen; sichtbare oder ausgeblendete Bedienelemente beweisen deren Durchsetzung nicht.

## Was die Produkte konkret zeigen

**Atlassian:** Die Dokumentation beschreibt parallel Centralized und Original User Management. Unter demselben Namen kann ein Site Admin je nach Erfahrung andere Möglichkeiten besitzen. In der zentralisierten Variante sind Site Administration und User Access Administration getrennte Zuständigkeiten. Der Organization-Admin-Titel allein bedeutet außerdem nicht automatisch Produktzugang; zusätzliche automatisch vergebene App-Rollen sind separat entziehbar. Der Skill muss deshalb Variante und effektive Rechte erfassen, statt aus einem Rollennamen Fähigkeiten zu erraten. [Admin-Rollen](https://support.atlassian.com/user-management/docs/what-are-the-different-types-of-admin-roles/), [Unterschiede beim Site Admin](https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-the-centralized-user-management-and-original-user-management-experiences/)

Die aktuelle Jira-Dokumentation verwendet „Space Roles“; ein früherer Link zur Projektrollenverwaltung leitet auf die entsprechenden Space-Permission-Schemes weiter. Rollen und geteilte Berechtigungsschemata können unterschiedliche Wirkungsbereiche haben. Für ein bestehendes Projekt dürfen seine eigenen Fachbegriffe dadurch nicht ohne Anlass ersetzt werden. [Space Roles](https://support.atlassian.com/jira-cloud-administration/docs/how-to-use-space-roles/), [Permission Schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-space-permissions-using-permission-schemes/)

**Google:** Persönliche Informationen und Sichtbarkeit werden im Google Account verwaltet. Cloud-Ressourcen besitzen dagegen eine Hierarchie aus Organisation, optionalen Ordnern, Projekten und Ressourcen. Eine Person ist nicht mit dem von ihr angelegten Organisationsprojekt gleichzusetzen. [Google Account](https://support.google.com/accounts/answer/15781205?hl=en), [Cloud-Ressourcenhierarchie](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)

Google Cloud kombiniert geerbte Allow Policies; Deny Policies und Principal Access Boundaries bilden zusätzliche Mechanismen. „Die restriktivste Rolle gewinnt“ wäre daher eine falsche allgemeine Erklärung. Cloud Billing und Google-Payments-Profile besitzen außerdem unterschiedliche, teilweise überlappende Berechtigungen. Unsere Oberfläche muss wirksame Rechte und deren Herkunft verständlich zeigen, nicht eine fiktiv einfache Auswertungsregel erfinden. [IAM-Überblick](https://docs.cloud.google.com/iam/docs/overview), [Billing-Zugriff](https://docs.cloud.google.com/billing/docs/how-to/billing-access)

**Apple:** Persönliche Apple-Account-Daten und die Teamverwaltung in App Store Connect sind getrennte Bereiche. Es gibt mehrere Teamrollen, aber nur einen Account Holder. Individuelle und organisatorische Programmitgliedschaft unterscheiden sich. Apple dokumentiert zudem Rollen und zusätzliche Ressourcenrechte, deren App-Zugriff nicht auf einzelne Apps beschränkt werden kann. [Apple Account](https://support.apple.com/en-gb/105023), [Konten und Rollen](https://developer.apple.com/help/app-store-connect/manage-your-team/overview-of-accounts-and-roles), [Nutzerverwaltung](https://developer.apple.com/help/app-store-connect/manage-your-team/add-and-edit-users/)

Eine Eigentumsübertragung ist nicht einfach ein weiterer Rollenwechsel: Apple verlangt für organisatorische Mitgliedschaften einen geeigneten Mitarbeitenden mit rechtlicher Bindungsbefugnis. Daraus leiten wir keine allgemeine Apple-Pflicht für andere Anwendungen ab; wir erkennen die Notwendigkeit, fachliche Verpflichtungen eines Owners ausdrücklich zu modellieren. [Account-Holder-Übertragung](https://developer.apple.com/help/account/access/transfer-the-account-holder-role)

**Stripe:** Ein Organisationsrecht wird in die darunterliegenden Accounts vererbt. Es lässt sich nicht durch eine schwächere Account-Rolle neutralisieren. Rollen können gleichzeitig gelten. Die Informationsarchitektur braucht deshalb einen sichtbaren Account-/Organisationskontext und eine Erklärung effektiver Rechte. [Organisationszugriff](https://docs.stripe.com/get-started/account/orgs/team), [Rollen](https://docs.stripe.com/get-started/account/teams/roles)

## Lebenszyklus und Autorität sind Teil des Designs

Atlassian unterscheidet in der zentralisierten Verwaltung temporäre Suspendierung mit wiederherstellbaren Rollen und Gruppen von Entfernung mit erneuter Einladung und Zuweisung. Das globale Atlassian-Konto wird dadurch nicht automatisch gelöscht. Diese Unterscheidung verhindert irreführende Bestätigungsdialoge. [Suspendieren oder entfernen](https://support.atlassian.com/user-management/docs/remove-or-suspend-a-user)

Bei Atlassians SCIM-Provisionierung werden synchronisierte Gruppen und verknüpfte Eigenschaften vom Identitätsanbieter verwaltet. Die Behandlung externer Nutzer unterscheidet sich von verwalteten Konten. Ein lokales Bearbeitungsformular darf nicht unbemerkt Änderungen zulassen, die beim nächsten Abgleich verschwinden. [Provisionierung](https://support.atlassian.com/provisioning-users/docs/understand-user-provisioning)

Google dokumentiert eine verzögerte Verteilung von IAM-Änderungen. Das Speichern eines Entzugs und dessen vollständige Wirksamkeit sind daher unterscheidbare Zustände. Entsprechende Produktzusagen müssen überprüft werden, bevor die Oberfläche sofortige Wirksamkeit behauptet. [Verteilung von Zugriffsänderungen](https://docs.cloud.google.com/iam/docs/access-change-propagation)

Atlassian und Google stellen Auditprotokolle bereit, deren Umfang, Zugriff und Verfügbarkeit vom jeweiligen System abhängen. Unser Skill erfindet deshalb weder unbegrenzte Aufbewahrung noch vollständige rückwirkende Ereignisse. [Atlassian Audit Log](https://support.atlassian.com/security-and-access-policies/docs/view-audit-log-activities/), [Google Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit)

## Eigenes Zielmodell für den Skill

Die folgenden Festlegungen sind unsere eigene Synthese:

| Bereich | Vorgesehener Ausgangspunkt | Zentrale Prüffrage |
|---|---|---|
| Persönliches Konto | Profil, persönliche Sicherheit, Präferenzen | Betrifft die Änderung nur diese Person? |
| Mitgliedschaft | Workspace-bezogene Rolle und Benachrichtigungen | Ist die Einstellung pro Organisation unterschiedlich? |
| Organisation | Unternehmensdaten, Mitglieder, Gruppen, Richtlinien | Wer ist betroffen und wer besitzt Verwaltungsbefugnis? |
| Projekt/Workspace | Lokale Workflows, Felder, Team und Standardwerte | Ist die Wirkung lokal oder über ein Schema geteilt? |
| Abrechnung | Zuständiges Billing-Konto | Sind Zahlungsverwaltung und Produktadministration getrennt? |
| Entwicklerbereich | Zugehörige Organisation, Projekt und Umgebung | Gehört die Integration einer Person oder einer Anwendung? |

Für jeden Bereich entsteht eine konkrete Rechteentscheidung aus Akteur, Aktion, Ressource, Geltungsbereich, Bedingungen und verbindlicher Quelle. „Sichtbar“, „deaktiviert mit Erklärung“, „Zugriff anfordern“ und „verborgen“ werden anhand des jeweiligen Nutzungsfalls gewählt. Eine fehlende Berechtigung darf nicht mit einem fehlenden Tarif, einer technischen Störung oder einem unvollständigen Setup verwechselt werden.

Der Mitgliederprozess wird vollständig beschrieben: Einladung vorbereiten, versenden, annehmen, ablaufen lassen oder widerrufen; Rollen und Gruppen ändern; Zugriff suspendieren und wiederherstellen; Mitgliedschaft entfernen; Eigentum übertragen. Für jeden Übergang müssen Seiteneffekt, Wirksamkeit, Zurück/Abbrechen und Fehlerbehandlung feststehen.

## Verbindliche Prüffälle

Im vollständigen Audit werden **jede Einstellungsseite, jede Komponentenverwendung, jedes Widget, jeder Drilldown und jeder definierte Zustandsübergang** erfasst. Dazu kommen relevante Rollen-, Scope-, Vererbungs- und Provisionierungsvarianten. Risikopriorisierung bestimmt die Reihenfolge; sie legitimiert keine unbenannten Auslassungen. Nicht geprüfte Einträge bleiben sichtbar und verhindern eine Behauptung vollständiger Abdeckung.

Zu den konkreten Tests gehören: persönliche Änderung ohne Wirkung auf Kollegen; Projektänderung ohne unbeabsichtigte Organisationswirkung; Rechnungseinsicht ohne allgemeine Administration; Erklärung geerbter Rechte; Einladung unter falscher Identität; Widerruf einer Einladung; parallele Rollenänderung; letzter Owner; lokal gesperrte SCIM-Eigenschaft; verzögerte Wirksamkeit; Organisationswechsel bei laufender Aktion; und nachvollziehbarer Audit-Eintrag ohne Geheimnisse.

Vor Implementierung werden Scope-Struktur, Rollenmatrix, Zustände, Screens und tatsächliche Texte als Konzept verfeinert und freigegeben. Danach wird dieselbe Version geprüft umgesetzt. Der Nutzen ist an weniger Fehlkonfigurationen, verständlicher Rechtevergabe, erfolgreicher Wiederherstellung und schnellerem Auffinden der richtigen Einstellung zu messen. Die Recherche liefert dafür begründete Regeln; der Wirksamkeitsnachweis an einer realen Anwendung bleibt Aufgabe eines Pilot-Audits.
