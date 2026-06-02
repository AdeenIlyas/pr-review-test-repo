def calculate_total(items):
    """
    Calculate order total.
    """

    total = 0

    for item in items:
        total += item["price"]

    return total