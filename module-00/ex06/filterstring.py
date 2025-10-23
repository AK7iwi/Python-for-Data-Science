import sys
from ft_filter import ft_filter


def validate_args() -> tuple[str, int]:
    """
    Validate command line arguments and return the string and integer.

    Args:
        None

    Returns:
        tuple: A tuple containing (string_arg, integer_arg)
            - string_arg (str): The input string to filter
            - integer_arg (int): The length threshold for filtering

    Raises:
        AssertionError: If wrong number of arguments
        or if the integer argument is not an integer (ValueError exception)
    """
    args = sys.argv
    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    string_arg = args[1]
    integer_arg = args[2]

    try:
        integer_arg = int(integer_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")

    return string_arg, integer_arg


def main() -> int:
    """
    Main function that filters words from a string based on length.
    Takes two command line arguments: string and integer.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        string_arg, integer_arg = validate_args()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1

    result = ft_filter(lambda x: len(x) > integer_arg, string_arg.split())
    print(list(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
