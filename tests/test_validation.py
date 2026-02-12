import unittest
from src.buergerregister.validation import validiere_person

class TestValidation(unittest.TestCase):
    
    def test_valid_person(self):
        """Testet eine vollständig gültige Person."""
        data = {
            "vorname": "Max",
            "nachname": "Mustermann",
            "geburtsjahr": 1990,
            "wohnort": "Berlin"
        }
        valid, errors = validiere_person(data)
        self.assertTrue(valid)
        self.assertEqual(len(errors), 0)

    def test_missing_fields(self):
        """Testet Fehler bei fehlenden Pflichtfeldern."""
        data = {
            "vorname": "",
            "nachname": "Mustermann",
            "geburtsjahr": 1990,
            "wohnort": "" # Fehlt
        }
        valid, errors = validiere_person(data)
        self.assertFalse(valid)
        self.assertIn("Der Vorname darf nicht leer sein.", errors)
        self.assertIn("Der Wohnort darf nicht leer sein.", errors)

    def test_invalid_birth_year_type(self):
        """Testet Fehler bei falschem Datentyp für Jahr."""
        data = {
            "vorname": "Max",
            "nachname": "Mustermann",
            "geburtsjahr": "1990", # String statt int
            "wohnort": "Berlin"
        }
        valid, errors = validiere_person(data)
        self.assertFalse(valid)
        self.assertIn("Das Geburtsjahr muss eine Zahl sein.", errors)

    def test_invalid_birth_year_range(self):
        """Testet Fehler bei Jahren außerhalb des Bereichs."""
        # Fall: Zu alt
        data_old = {"vorname": "A", "nachname": "B", "geburtsjahr": 1899, "wohnort": "C"}
        valid, errors = validiere_person(data_old)
        self.assertFalse(valid)
        self.assertTrue(any("unplausibel" in e for e in errors))

        # Zukunft (2026
        data_future = {"vorname": "A", "nachname": "B", "geburtsjahr": 2026, "wohnort": "C"}
        valid, errors = validiere_person(data_future)
        self.assertFalse(valid)
        self.assertTrue(any("unplausibel" in e for e in errors))

    def test_edge_case_years(self):
        """Testet die Grenzjahre 1900 und 2025."""
        # 1900 -> OK
        data_1900 = {"vorname": "A", "nachname": "B", "geburtsjahr": 1900, "wohnort": "C"}
        valid, _ = validiere_person(data_1900)
        self.assertTrue(valid)

        # 2025 -> OK
        data_2025 = {"vorname": "A", "nachname": "B", "geburtsjahr": 2025, "wohnort": "C"}
        valid, _ = validiere_person(data_2025)
        self.assertTrue(valid)

if __name__ == '__main__':
    unittest.main()
