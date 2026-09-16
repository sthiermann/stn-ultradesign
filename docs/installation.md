# Installation

Stand: 16. September 2026. Installiere entweder den einzelnen Skill oder das Plugin im jeweiligen Client. Eine doppelte Installation desselben Skills ist nicht erforderlich.

## Codex: einzelner Skill

Codex lädt projektbezogene Skills aus `.agents/skills/` und persönliche Skills aus `~/.agents/skills/`. Der ganze Skill-Ordner muss erhalten bleiben, damit Referenzen, Vorlagen und Skripte erreichbar sind. Siehe [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills).

Repository herunterladen, beispielsweise im Terminal:

```sh
git clone https://github.com/sthiermann/stn-ultradesign.git
cd stn-ultradesign
```

Für eine persönliche Installation unter macOS oder Linux, aus dem heruntergeladenen Repository:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/skills/stn-ultradesign" "$HOME/.agents/skills/stn-ultradesign"
```

Der Link setzt voraus, dass am Ziel noch kein gleichnamiger Eintrag liegt und das Repository an diesem Ort bleibt. Alternativ den Ordner `skills/stn-ultradesign` vollständig nach `~/.agents/skills/stn-ultradesign` kopieren. Für eine Projektinstallation entsprechend nach `<projekt>/.agents/skills/stn-ultradesign` kopieren. Unter Windows die entsprechenden Verzeichnisse im Benutzerprofil verwenden; der Kopierweg benötigt keine symbolischen Links.

Codex neu öffnen, falls der Skill noch nicht erscheint. In Codex CLI oder IDE über `/skills` auswählen oder `$stn-ultradesign` im Auftrag erwähnen. Oberflächen mit einer Skill-Auswahl über `@` können den Skill dort anbieten.

```text
$stn-ultradesign Prüfe den Einstellungsbereich auf Verständlichkeit,
Konsistenz, Fehlerbehandlung und Tastaturbedienung.
```

## Codex: Plugin-Paket

Das Repository enthält das unterstützte Kompatibilitätsmanifest `.codex-plugin/plugin.json`. Die offizielle [Plugin-Anleitung](https://learn.chatgpt.com/docs/build-plugins) beschreibt den lokalen Marketplace-Weg mit `$plugin-creator`: den vorhandenen Repository-Ordner einem lokalen Marketplace hinzufügen, den Client aktualisieren und das Plugin aus dieser Quelle installieren. Dabei soll der Creator das bestehende Paket registrieren und keine Skill-Inhalte neu erzeugen.

Eine Veröffentlichung auf GitHub ist keine Aufnahme in das offizielle Plugin-Verzeichnis. Dieses Repository konfiguriert selbst keinen persönlichen Codex-Marketplace. Für die unmittelbare Nutzung reicht die oben dokumentierte Einzelinstallation.

## Claude Code: Plugin aus GitHub

Die folgenden Befehle innerhalb von Claude Code eingeben:

```text
/plugin marketplace add sthiermann/stn-ultradesign
/plugin install stn-ultradesign@stn-ultradesign
```

Den gewünschten Installationsumfang in der angezeigten Auswahl festlegen. Falls Claude Code dazu auffordert, anschließend `/reload-plugins` ausführen. Der Aufruf lautet:

```text
/stn-ultradesign:stn-ultradesign Entwickle zunächst ein überprüfbares
Designkonzept für diesen Workflow. Setze es nach meiner Freigabe um.
```

Der Marketplace verweist auf das Plugin im Repository-Stamm. Daher den GitHub-Repositorynamen als Quelle verwenden, keine direkte URL zur einzelnen `marketplace.json`. Siehe [Claude Code: Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) und [Plugins entdecken und installieren](https://code.claude.com/docs/en/discover-plugins).

Zum lokalen Ausprobieren ohne Marketplace-Installation:

```sh
claude --plugin-dir /absoluter/pfad/stn-ultradesign
```

`/absoluter/pfad/stn-ultradesign` durch den tatsächlichen Repository-Pfad ersetzen. Die [Plugin-Referenz](https://code.claude.com/docs/en/plugins-reference) dokumentiert diesen Entwicklungsmodus.

## Claude Code: einzelner Skill als Alternative

`skills/stn-ultradesign` vollständig nach `~/.claude/skills/stn-ultradesign` oder `<projekt>/.claude/skills/stn-ultradesign` kopieren. Danach `/stn-ultradesign` verwenden. Die persönliche Installation gilt für lokale Claude-Code-Sitzungen; andere Claude-Produkte haben eigene Ladewege. Siehe [Claude Code: Skills](https://code.claude.com/docs/en/skills).

## Installation prüfen und aktualisieren

Einen neuen Auftrag öffnen und den Skill explizit aufrufen. Zunächst einen begrenzten Audit anfordern. Prüfen, ob der Agent den Skill und passende Referenzen liest, den Umfang einhält und tatsächlich beobachtete Ergebnisse von Annahmen trennt.

Bei einer Link-Installation folgen die Skill-Dateien dem ausgecheckten Repository-Stand; bei einer Kopie muss der Skill-Ordner nach einer Aktualisierung erneut übertragen werden. Änderungen vor dem Übernehmen prüfen. Claude-Plugin-Updates über den Plugin-Manager des Clients ausführen.

Manifestvalidierung prüft das Paketformat. Sie belegt weder eine erfolgreiche Installation in allen Client-Versionen noch die fachliche Qualität eines konkreten Audits. Client-Version, Installationsweg und tatsächlich durchgeführte Prüfungen bei Problemen angeben.
