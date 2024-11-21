![Tests](https://github.com/Zitronenjoghurt/essensbestellung/actions/workflows/app-test.yml/badge.svg)

# Essensbestellung
Hier gibt's alle Informationen zum Setup und Arbeiten mit dem Projekt.\
**Vor dem Pushen die Informationen zur [Versionierung](#versionierung) durchlesen!**

Work in progress...

## Code Konventionen
- Python conventions (z.B. snake_case)
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
- [Datenbankmigrationen lokal anwenden](#migrationen-anwenden)

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

# Versionierung
Der ganze Development Prozess läuft auf dem `develop` Branch ab, der dann bei erreichten Meilensteinen zu `main` gemergt wird. Auf `main` hat man somit immer eine stabile Version des Projekts.

Bevor man seinen eigenen Code auf `develop` pusht, zweigt man sich einen Branch von `develop` ab (das können eigentlich alle IDEs). Vergesst nicht vor dem Abzweigen zu pullen/fetchen und zweigt immer vom remote `develop` ab und nicht vom lokalen. Branch-Namen starten meistens mit `feature/` für Feature branches oder `bugfix/` für Bugfixes.

Man wird also für jede neue Aufgabe einen neuen Branch erstellen. Auf dem neuen Branch kann man dann coden und pushen wie man will, es sollte aber immer zum Sinn des Branches passen. Außerdem sollten die Commmit-Nachrichten kurz und aussagekräftig sein. Wenn das Feature / die Aufgabe abgeschlossen ist, erstellt man eine Pull Request von seinem Branch zu `develop`: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Dort laufen dann automatisch alle tests nochmal durch und ggfs. schaut jemand anderes auch nochmal mit drüber (Code Review). Wenn der Reviewer die Pull Request bestätigt kann sie gemergt werden, was die Changes dann auf den develop branch bringt. *fertig*.

Während eines Pull-Requests kann es jedoch zu Merge-Konflikten kommen (wenn zwei Leute z.B. die gleiche Datei verändert haben). Um das zu lösen mergt man bei sich in der IDE den `develop` branch (von remote, fetchen/pull vorher nicht vergessen xD) in seinen eigenen Branch. Dann resolved man die Merge-Konflikte (sollte in jeder IDE möglich sein) und pusht die Änderungen wieder auf seinen Branch. In der Pull-Request sollte sich dann wenn alles richtig abgelaufen ist der Status ändern, die Konflikte sind gelöst und es kann gemergt werden. Wenn man sich beim resolven der Merge-Konflikte nicht sicher ist, lieber zweimal fragen.

Wenn man das noch nie vorher gemacht hat, klingt es komplizierter als es eigentlich ist. Zur Not kann man es dann individuell nochmal zusammen durchgehen.

## Zusammenfassung zur Versionierung
Hier nochmal das wichtigste auf einem Blick.

### Ablauf Feature-Entwicklung
- Von `develop` abzweigen (immer vom remote)
  - Branch namen starten mit `feature/` oder `bugfix/`
  - Bsp.: `feature/qr_code_support`, `bugfix/fix_missing_user_roles`
- Feature entwickeln
- Regelmäßig pushen
- Wenn fertig, Pull Request erstellen
- Tests und Code Review abwarten
- evtl. Merge-Konflikte lösen
- Nach Bestätigung mergen

### Merge-Konflikte lösen
- Remote `develop` in eigenen Branch mergen
- Konflikte in IDE lösen
- Gelöste Änderungen pushen
- Pull Request sollte sich automatisch aktualisieren

### Hinweise
- Vor dem Abzweigen fetchen/pullen
- Immer vom **remote** `develop` abzweigen
- Bei Unsicherheiten beim Konflikt-Lösen nachfragen
- Branches thematisch/Aufgaben-fokussiert halten
- Kurze und aussagekräftige Commit-Nachrichten