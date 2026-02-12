from dataclasses import dataclass

@dataclass
class Person:
    """
    Repräsentiert eine Bürgerin bzw. einen Bürger als einfaches Datenobjekt.
    """
    vorname: str
    nachname: str
    geburtsjahr: int
    wohnort: str

    def normalize_name(self, name: str) -> str:
        """
        Normalizes a name string by stripping whitespace and converting to title case.

        Args:
        name (str): The name string to normalize.

        Returns:
            str: The normalized name string.
        """
        return name.strip().title()
