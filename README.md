# Essensbestellung
Hier gibt's alle Informationen zum Setup und Arbeiten mit dem Projekt.

README work in progress...

## Voraussetzungen
- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Git](https://git-scm.com/downloads)
- [Docker / Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Basic Setup
Wie man das Projekt grundlegend zum Laufen bringt.

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

Server stoppen:
```shell
make dev-down oder make clean
```
Weitere make Befehle findet ihr in der [Makefile](Makefile) im root.