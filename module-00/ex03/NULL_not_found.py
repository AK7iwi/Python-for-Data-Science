import sys
import math
from validate_args import validate_args


def print_null_type(object: any) -> None:
    """
    Print the type of the null-like object.

    Args:
        object (any): The null-like object to print the type of

    Returns:
        None

    Raises:
        TypeError: if the type is not found
    """
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: False {type(object)}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: 0 {type(object)}")
    elif isinstance(object, str) and len(object) == 0:
        print(f"Empty: {type(object)}")
    else:
        raise TypeError("Type not Found")


def NULL_not_found(object: any) -> int:
    """
    Check the type of null-like objects and print their information.

    Args:
        object (any): The object to check for null-like properties

    Returns:
        int: 0 for recognized null types, 1 for unrecognized types

    Raises:
        None
    """
    try:
        print_null_type(object)

    except TypeError as e:
        print(e)
        return 1

    return 0


def main() -> int:
    """
    Main function to test the NULL_not_found function.
    """
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False

    try:
        validate_args()

        NULL_not_found(Nothing)
        NULL_not_found(Garlic)
        NULL_not_found(Zero)
        NULL_not_found(Empty)
        NULL_not_found(Fake)
        print(NULL_not_found("Brian"))

        return 0

    except ValueError as e:
        print(f"ValueError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
