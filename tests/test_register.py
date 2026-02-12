import unittest
from src.buergerregister.models import Person
from src.buergerregister.register import Buergerregister

class TestBuergerregister(unittest.TestCase):
    
    def setUp(self):
        """Wird vor jedem Test ausgeführt."""
        self.reg = Buergerregister()
        self.p1 = Person("Anna", "Muster", 1990, "Berlin")

    def test_add_valid_person(self):
        """Testet das erfolgreiche Hinzufügen."""
        success, msg = self.reg.add(self.p1)
        self.assertTrue(success)
        self.assertEqual(len(self.reg.list()), 1)

    def test_add_duplicate(self):
        """Testet die Duplikat-Erkennung."""
        self.reg.add(self.p1)
        success, msg = self.reg.add(self.p1) # Gleiche Person nochmal
        self.assertFalse(success)
        self.assertIn("Duplikat", msg)
        self.assertEqual(len(self.reg.list()), 1)

    def test_validation_failure(self):
        """Testet, ob ungültige Personen abgelehnt werden."""
        p_invalid = Person("", "Muster", 1800, "Berlin") # Kein Vorname, Jahr zu alt
        success, msg = self.reg.add(p_invalid)
        self.assertFalse(success)
        self.assertIn("Validierungsfehler", msg)

if __name__ == '__main__':
    unittest.main()