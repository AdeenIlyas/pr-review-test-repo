from app.auth import authenticate


def test_valid_login():
    assert authenticate(
        "admin",
        "admin123"
    ) is True


def test_invalid_login():
    assert authenticate(
        "john",
        "wrong"
    ) is False