import sys
from typing import Iterator
from validate_args import validate_args_for_test


def ft_filter(function, iterable) -> Iterator:
    """
    Custom filter function that behaves like the built-in filter.

    Args:
        function (callable or None): Function to apply to each element, or None
        to filter out falsy values
        iterable (iterable): The iterable to filter

    Returns:
        filter object: An iterator yielding those items of iterable for which
        function(item) is true.
        If function is None, return the items that are true.

    Raises:
        None
    """
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))


def main() -> int:
    """
    Main function to test the ft_filter function.
    """
    list_test = [1, 2, 3, 4, 5]

    try:
        if not validate_args_for_test():
            return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    result = ft_filter(lambda x: x % 2 == 0, list_test)
    print("ft_filter: ", result)
    print("list(result): ", list(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
