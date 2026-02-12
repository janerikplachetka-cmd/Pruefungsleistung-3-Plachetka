import pytest
from src.models import Person


def test_person_creation_valid():
    # Arrange
    firstname = "Max"
    lastname = "Mustermann"
    birth_year = 1995
    city = "Bremen"

    # Act
    person = Person(firstname, lastname, birth_year, city)

    # Assert
    assert person.firstname == firstname
    assert person.lastname == lastname
    assert person.birth_year == birth_year
    assert person.city == city


def test_person_equality_same_data():
    # Arrange
    person1 = Person("Max", "Mustermann", 1995, "Bremen")
    person2 = Person("Max", "Mustermann", 1995, "Bremen")

    # Act / Assert
    assert person1 == person2


def test_person_inequality_different_data():
    # Arrange
    person1 = Person("Max", "Mustermann", 1995, "Bremen")
    person2 = Person("Anna", "Mustermann", 1995, "Bremen")

    # Act / Assert
    assert person1 != person2