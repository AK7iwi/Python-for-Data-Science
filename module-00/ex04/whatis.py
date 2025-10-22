import sys


def validate_args() -> int | None:
    """
    Validate command line arguments and return the number.

    Args:
        None

    Returns:
        int: The validated integer argument
        None: If no argument is provided

    Raises:
        AssertionError: If more than one argument or argument is not an integer
    """
    args = sys.argv
    if len(args) == 1:
        return None
    elif len(args) > 2:
        raise AssertionError("more than one argument is provided")

    arg = args[1]
    try:
        number = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")

    return number


def check_odd_even(number: int) -> None:
    """
    Check if a number is odd or even and print the result.

    Args:
        number (int): The number to check

    Returns:
        None

    Raises:
        None
    """
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> int:
    """
    Main function that checks if a number is odd or even.
    Takes exactly one command line argument: an integer to check.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        number = validate_args()
        if number is not None:
            check_odd_even(number)

        return 0

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
