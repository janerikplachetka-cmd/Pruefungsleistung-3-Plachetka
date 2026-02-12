# Bürgerregister Light - Portfolio 3

Dieses Repository bildet die Grundlage für die Teilprüfung 3 (Qualitätssicherung mit Tests, Metriken und CI)

## Ziele
• eine bestehende Software strukturiert zu analysieren
• eine sinnvolle Teststrategie abzuleiten und umzusetzen
• Qualität mithilfe geeigneter Metriken messbar zu machen
• Automatisierung durch Continuous Integration einzusetzen
• Ergebnisse praxisnah, nachvollziehbar und reflektiert schriftlich darzustellen.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -U pip
pip install -e .[dev]
```

## Tests ausführen
```bash
pytest -q
```

## Beispiel
```python
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

reg = Buergerregister()
reg.add(Person("Anna", "Schmidt", 1990, "Essen"))
print(reg.list())
```

