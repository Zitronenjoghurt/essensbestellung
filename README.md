# Essensbestellung
Hier gibt's alle Informationen zum Setup und Arbeiten mit dem Projekt.

Work in progress...

## Konventionen
- Python conventions (z.B. camel_case)
- keine Magic-Values, verschiedene Werte gleicher Art am besten in Enums
- separation of concerns
- (bei Bedarf erweitern)

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
! `make clean` resettet auch die Datenbank.\
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

# Service-Repository-Entity pattern
Wichtig für modulares Design und klareres separation of concerns:
https://medium.com/@ankitpal181/service-repository-pattern-802540254019

Im Prinzip hat man Entities, welche ihre Informationen beschreiben (und eventuell simple Operationen), Repositories die sich allein um das fetchen von Daten kümmern und Services, welche die komplexere Business Logic enthalten.
Die Entities sollten so wenig Logik wie möglich enthalten, damit man mithilfe der hierarchischen Struktur circular dependencies und Vermischung von Responsibilities so gut es geht vermeidet.

# Library Übersicht
Das sind die Libraries auf die Reflex aufbaut, die aber selbst Funktionen beitragen, die man Unabhängig oder in Kombination mit Reflex verwenden kann.

| Library    | Beschreibung                                                                                         |
|------------|------------------------------------------------------------------------------------------------------|
| alembic    | Datenbank-Migrations-Tool für SQLAlchemy. Ermöglicht automatische Schema-Updates und Versionierung.  |
| Pydantic   | Datenvalidierung durch Python Type Annotations. Wandelt JSON in Python-Objekte um und umgekehrt.     |
| SQLAlchemy | ORM (Object Relational Mapper) für Datenbank-Interaktionen. Abstrahiert SQL in Python-Code.          |
| SQLModel   | Kombiniert Pydantic und SQLAlchemy für typsichere Datenbankmodelle. Vereinfacht das API-Design       |
| FastAPI    | Modernes Python-Web-Framework für schnelle APIs. Nutzt Type-Hints für automatische Validierung/Docs. |
| Uvicorn    | ASGI-Server, der Python-Web-Apps ausführt. Ermöglicht async/await für hohe Performance.              |
| httpx      | Moderner HTTP-Client für Python. Unterstützt sync/async und moderne Protokolle wie HTTP/2.           |

