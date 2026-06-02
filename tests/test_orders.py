from app.orders import calculate_total


def test_total():

    items = [
        {"price": 10},
        {"price": 20}
    ]

    assert calculate_total(items) == 30