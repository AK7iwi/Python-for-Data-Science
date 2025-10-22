import sys


def validate_args_for_test() -> bool:
    """
    Validate the number of arguments for the test of function.

    Args:
        None

    Returns:
        bool: True if the arguments are valid, False otherwise

    Raises:
        ValueError: If the number of arguments is not 2
        or the second argument is not "test"
    """
    args = sys.argv
    if len(args) == 1:
        return False
    elif len(args) > 2 or args[1] != "test":
        raise ValueError("Invalid arguments")

    return True


def validate_args_for_prog() -> None:
    """
    Validate the number of arguments.

    Args:
        None

    Returns:
        None

    Raises:
        ValueError: If the number of arguments is not 1
    """
    args = sys.argv
    if len(args) != 1:
        raise ValueError("Invalid number of arguments")


def main() -> int:
    """
    Main function to test the validate_args function.
    """
    try:
        validate_args_for_prog()
        # validate_args_for_test()

    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
