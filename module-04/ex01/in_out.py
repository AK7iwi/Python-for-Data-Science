"""
Module in_out: MathOperations class and closure functions.
"""
import sys
from validate_args import validate_args_for_test, MissingArgumentsError


class MathOperations:
    """
    Class containing mathematical operations.

    This class provides static methods for mathematical calculations.

    Attributes:
        None
    """

    # ==================== Methods ==================== #
    @staticmethod
    def square(x: int | float) -> int | float:
        """
        Calculate the square of a number.

        Args:
            x (int | float): The number to square.

        Returns:
            int | float: The square of x.

        Raises:
            None
        """
        return x * x

    @staticmethod
    def pow(x: int | float) -> int | float:
        """
        Calculate the exponentiation of a number by itself.

        Args:
            x (int | float): The number to exponentiate.

        Returns:
            int | float: x raised to the power of x.

        Raises:
            None
        """
        return x ** x


def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.

    Args:
        x (int | float): The number to square.

    Returns:
        int | float: The square of x.

    Raises:
        None
    """
    return MathOperations.square(x)


def pow(x: int | float) -> int | float:
    """
    Calculate the exponentiation of a number by itself.

    Args:
        x (int | float): The number to exponentiate.

    Returns:
        int | float: x raised to the power of x.

    Raises:
        None
    """
    return MathOperations.pow(x)


def outer(x: int | float, function) -> object:
    """
    Create a closure that applies a function repeatedly to a value.

    Args:
        x (int | float): The initial value.
        function: The function to apply to the value.

    Returns:
        object: An inner function that applies the function to the current
            value and returns the result.

    Raises:
        None
    """
    count = 0

    def inner() -> float:
        """
        Apply the function to the current value and return the result.

        Args:
            None

        Returns:
            float: The result of applying the function.

        Raises:
            None
        """
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner


def main() -> int:
    """
    Main function to test closure functions.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())

    return 0


if __name__ == "__main__":
    sys.exit(main())
