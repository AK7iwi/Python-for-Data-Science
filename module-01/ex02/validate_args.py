import sys


def validate_args() -> None:
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
        validate_args()
        return 0

    except ValueError as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
