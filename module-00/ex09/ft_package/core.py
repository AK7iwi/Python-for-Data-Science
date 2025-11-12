from typing import Any


def count_in_list(lst: list, item: Any) -> int:
    """
    Return the number of occurrences of item in lst.

    Args:
        lst (list): The list to search in
        item (Any): The item to count occurrences of

    Returns:
        int: The number of times the item appears in the list

    Raises:
        None
    """
    return lst.count(item)
