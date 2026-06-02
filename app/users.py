users = {
    1: {
        "id": 1,
        "name": "John"
    },
    2: {
        "id": 2,
        "name": "Alice"
    }
}


def get_user(user_id):
    """
    Return user by ID.
    """

    return users.get(user_id)


def get_user_name(user_id):

    user = get_user(user_id)

    return user["name"]