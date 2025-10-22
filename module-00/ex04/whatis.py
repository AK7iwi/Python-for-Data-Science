import sys


def validate_argument() -> int | None:
    """
    Validate command line arguments and return the number.

    Args:
        None

    Returns:
        int: The validated integer argument

    Raises:
        AssertionError: If more than one argument or argument is not an integer
    """
    # Check number of arguments
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        return None

    # Get the argument
    arg = sys.argv[1]

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
        None: This function only prints to stdout

    Raises:
        None
    """
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
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
        number = validate_argument()
        if number is not None:
            check_odd_even(number)

        return 0

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
