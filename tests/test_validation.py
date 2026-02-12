import pytest
from src.validation import validate_person


def test_validate_person_valid_data():
    # Arrange
    person_data = {
        "firstname": "Max",
        "lastname": "Mustermann",
        "birth_year": 1995,
        "city": "Bremen"
    }

    # Act
    result = validate_person(person_data)

    # Assert
    assert result is True


def test_validate_person_missing_firstname():
    # Arrange
    person_data = {
        "firstname": "",
        "lastname": "Mustermann",
        "birth_year": 1995,
        "city": "Bremen"
    }

    # Act / Assert
    with pytest.raises(ValueError):
        validate_person(person_data)


def test_validate_person_missing_lastname():
    # Arrange
    person_data = {
        "firstname": "Max",
        "lastname": "",
        "birth_year": 1995,
        "city": "Bremen"
    }

    # Act / Assert
    with pytest.raises(ValueError):
        validate_person(person_data)


def test_validate_person_birth_year_out_of_range():
    # Arrange
    person_data = {
        "firstname": "Anna",
        "lastname": "Beispiel",
        "birth_year": 1880,
        "city": "Bremen"
    }

    # Act / Assert
    with pytest.raises(ValueError):
        validate_person(person_data)


def test_validate_person_birth_year_wrong_type():
    # Arrange
    person_data = {
        "firstname": "Anna",
        "lastname": "Beispiel",
        "birth_year": "neunzehn",
        "city": "Bremen"
    }

    # Act / Assert
    with pytest.raises(TypeError):
        validate_person(person_data)