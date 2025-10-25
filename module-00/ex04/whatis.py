import sys


def validate_args() -> int:
    """
    Validate command line arguments and return the number.

    Args:
        None

    Returns:
        int: The validated integer argument

    Raises:
        AssertionError: If the number of arguments is not 2
        or if the argument is not an integer (ValueError exception)
    """
    args = sys.argv
    if len(args) == 1:
        raise ValueError()
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
    except ValueError:
        return 1
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1

    check_odd_even(number)

    return 0


if __name__ == "__main__":
    sys.exit(main())
