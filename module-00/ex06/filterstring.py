import sys
from ft_filter import ft_filter


def validate_arguments() -> tuple[str, int]:
    """
    Validate command line arguments and return the string and integer.

    Args:
        None

    Returns:
        tuple: A tuple containing (string_arg, integer_arg)
            - string_arg (str): The input string to filter
            - integer_arg (int): The length threshold for filtering

    Raises:
        AssertionError: If the arguments are bad (wrong number or type)
    """
    # Check number of arguments
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    # Get arguments
    string_arg = sys.argv[1]
    integer_arg = sys.argv[2]

    try:
        integer_arg = int(integer_arg)
    except ValueError:
        raise AssertionError("the arguments are bad")

    return string_arg, integer_arg


def main():
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
        string_arg, integer_arg = validate_arguments()
        result = ft_filter(lambda x: len(x) > integer_arg, string_arg.split())
        print(result)

        return 0

    except Exception as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()
