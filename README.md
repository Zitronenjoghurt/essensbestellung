# Essensbestellung
Hier gibt's alle Informationen zum Setup und Arbeiten mit dem Projekt.

Work in progress...

## Voraussetzungen
- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Git](https://git-scm.com/downloads)
- [Docker / Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Basic Setup
Wie man das Projekt grundlegend zum Laufen bringt.

---
### Projekt klonen
```shell
git clone https://github.com/Zitronenjoghurt/essensbestellung.git
```
---
### Docker daemon starten
Einfach Docker Desktop öffnen und sicherstellen, dass es im Hintergrund läuft.

---
### App starten
Ins Projekt-Root navigieren.

Den Dev-Server starten:
```shell
make dev-up
```
Der läuft im Hintergrund und baut das Projekt bei jeder Änderung automatisch neu.

FYI: Server stoppen:
```shell
make dev-down oder make clean
```
Weitere make Befehle findet ihr in der [Makefile](Makefile) im root.

---
### Weitere Schritte
- Datenbankmigrationen lokal anwenden

Fertig!

---
### Im Browser aufrufen
http://localhost:3000

---

# Datenbank
Reflex handled das Meiste Rund um die Datenbank selbst. Was wir jedoch selbst machen müssen: Migrationen generieren lassen und diese lokal anwenden.

Migrationen sind eine Reihe von Anweisungen, welche beschreiben, wie eine Datenbank verändert werden soll (z.B. Tabelle/Spalten hinzufügen, etc.).
Das ist vor allem wichtig, wenn sich später Anforderungen ändern und allgemein vereinfacht es den ganzen Datenbank-Aufbauprozess.

## Migrationen anwenden
Zuerst in den Docker-Container navigieren:
- Docker Desktop öffnen
- Sicherstellen, dass der Container läuft (siehe basic setup), so sieht es ungefähr aus:
  - essensbestellung-dev
    - db-1
    - reflex-1
- Auf 'reflex-1' klicken
- In den Exec Tab

Und folgenden Befehl ausführen:
```shell
reflex db migrate
```

## Eigene Migration erstellen
Wenn ihr was an den Models/Entitytypen geändert habt, müssen diese Änderungen auch in der DB angewandt werden.

Eine Migration kann man ziemlich simpel selbst erstellen mit folgendem Befehl im reflex container:
```shell
reflex db makemigrations --message 'was_ihr_verändert_habt'
```
Und am Ende wieder `reflex db migrate`.

## Datenbank resetten
Bei Bedarf, einfach in Docker Desktop in den Volumes `essensbestellung-dev_postgres_data_dev` löschen und den Container neu starten, z.B. mit `make dev-restart` im Projekt-Root.

Das Volume ist immer unabhängig vom Container selbst, man kann also den Container komplett löschen und die Daten bleiben erhalten.