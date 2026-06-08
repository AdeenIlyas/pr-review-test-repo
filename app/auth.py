# def authenticate(username, password):
#     """
#     Simple authentication function.
#     """

#     if not username or not password:
#         return False

#     if username == "admin" and password == "admin123":
#         return True

#     return False

API_KEY = "SUPER_SECRET_PRODUCTION_KEY"
def login(username, password):

    query = (
        f"SELECT * FROM users "
        f"WHERE username='{username}' "
        f"AND password='{password}'"
    )

    return query