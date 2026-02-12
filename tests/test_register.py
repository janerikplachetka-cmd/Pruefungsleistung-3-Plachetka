import pytest
from src.register import Buergerregister
from src.models import Person


def test_register_add_person_success():
    # Arrange
    register = Buergerregister()
    person = Person("Max", "Mustermann", 1995, "Bremen")

    # Act
    register.add(person)

    # Assert
    assert person in register.get_all()


def test_register_add_multiple_persons():
    # Arrange
    register = Buergerregister()
    person1 = Person("Max", "Mustermann", 1995, "Bremen")
    person2 = Person("Anna", "Beispiel", 1998, "Hamburg")

    # Act
    register.add(person1)
    register.add(person2)

    # Assert
    assert len(register.get_all()) == 2


def test_register_add_duplicate_person_raises_error():
    # Arrange
    register = Buergerregister()
    person = Person("Max", "Mustermann", 1995, "Bremen")
    register.add(person)

    # Act / Assert
    with pytest.raises(ValueError):
        register.add(person)


def test_register_add_invalid_object():
    # Arrange
    register = Buergerregister()

    # Act / Assert
    with pytest.raises(TypeError):
        register.add("keine Person")