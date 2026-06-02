def login(username, password):

    query = (
        f"SELECT * FROM users "
        f"WHERE username='{username}' "
        f"AND password='{password}'"
    )

    return query