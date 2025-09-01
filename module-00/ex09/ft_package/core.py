def add(a, b):
    """Return a + b."""
    return a + b


def sub(a, b):
    """Return a - b."""
    return a - b


def mul(a, b):
    """Return a * b."""
    return a * b


def div(a, b):
    """Return a / b. Raises ZeroDivisionError if b == 0."""
    return a / b


def count_in_list(lst, value):
    """Return the number of occurrences of value in lst."""
    return sum(1 for x in lst if x == value)