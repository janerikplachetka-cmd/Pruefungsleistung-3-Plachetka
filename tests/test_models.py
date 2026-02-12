import unittest
from src.buergerregister.models import Person

class TestModels(unittest.TestCase):
    
    def test_normalize_name(self):
        """Testet die Normalisierung von Namen."""
        p = Person("Max", "Mustermann", 1990, "Berlin")
        
        # Test cases
        self.assertEqual(p.normalize_name("  max  "), "Max")
        self.assertEqual(p.normalize_name("MUSTERMANN"), "Mustermann")
        self.assertEqual(p.normalize_name("anne-marie"), "Anne-Marie") # Note: title() might handle hyphens simply
        
        # Check title() behavior on mixed input
        self.assertEqual(p.normalize_name("jOhN dOe"), "John Doe")

if __name__ == '__main__':
    unittest.main()
