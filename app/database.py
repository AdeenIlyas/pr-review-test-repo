import sqlite3


def connect():
    """
    Create sqlite connection.
    """

    return sqlite3.connect("app.db")