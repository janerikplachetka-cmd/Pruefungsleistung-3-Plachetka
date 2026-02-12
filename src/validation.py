from typing import Any, Dict, List, Tuple

def validiere_person(daten: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Prüft ein Personen-Dictionary auf Pflichtfelder und Plausibilität.

    Args:
        daten (dict): Ein Dictionary mit den Schlüsseln 'vorname', 'nachname',
                      'geburtsjahr' und 'wohnort'.

    Returns:
        tuple: (ist_valide (bool), fehlerliste (list[str]))
    """
    errors: List[str] = []

    # Prüfung auf leere Strings (Pflichtfelder)
    if not daten.get("vorname"):
        errors.append("Der Vorname darf nicht leer sein.")
    
    if not daten.get("nachname"):
        errors.append("Der Nachname darf nicht leer sein.")
    
    if not daten.get("wohnort"):
        errors.append("Der Wohnort darf nicht leer sein.")

    # Plausibilitätsprüfung Geburtsjahr
    jahr = daten.get("geburtsjahr")
    if not isinstance(jahr, int):
        errors.append("Das Geburtsjahr muss eine Zahl sein.")
    elif not (1900 <= jahr <= 2025):
        errors.append(f"Das Geburtsjahr {jahr} ist unplausibel (muss zwischen 1900 und 2025 liegen).")

    # Ergebnis zurückgeben: True wenn keine Fehler da sind
    return (len(errors) == 0, errors)
