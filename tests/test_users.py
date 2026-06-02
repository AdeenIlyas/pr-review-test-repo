from app.users import get_user


def test_get_user():

    user = get_user(1)

    assert user["name"] == "John"