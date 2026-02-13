# Bürgerregister (Prüfungsleistung 3 Plachetka)

Eine Anwendung zur einfachen Verwaltung von Bürgerdaten mit grafischer Oberfläche.

## Funktionen

Das Projekt bietet folgende Möglichkeiten:
*   **Personen erfassen**: Hinzufügen von Vorname, Nachname, Geburtsjahr und Wohnort.
*   **Validierung**: Überprüfung der Eingabedaten auf Plausibilität.
*   **Anzeige**: Auflistung aller erfassten Personen in einer Liste.
*   **Suche**: Filtern und Finden von Personen.
*   **Persistenz**: Daten werden zur Laufzeit im Speicher gehalten (In-Memory).

## Voraussetzungen

*   Python 3.10 oder höher
*   Standard-Bibliotheken (Tkinter, Dataclasses, Unittest/Pytest)

## Installation

1.  Repository klonen oder herunterladen.
2.  In das Projektverzeichnis wechseln.

## Nutzung

Starten der grafischen Oberfläche über die Kommandozeile:

```bash
python start_gui.py
```

## Tests

Ausführen der Unit-Tests mit `pytest`:

```bash
pytest
```
Alternativ können Tests auch direkt über Python ausgeführt werden (sofern konfiguriert).
