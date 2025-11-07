"""
Module ft_calculator: Calculator class for vector-scalar operations.
"""
import sys
from validate_args import validate_args_for_prog


class calculator:
    """
    Calculator class for performing operations between a vector and a scalar.

    Attributes:
        vector (list[float]): The vector to perform operations on.
    """

    def __init__(self, vector: list[float]) -> None:
        """
        Initialize a calculator instance with a vector.

        Args:
            vector (list[float]): The vector to perform operations on.

        Returns:
            None

        Raises:
            None
        """
        self.vector = vector

    def __add__(self, object: int | float) -> None:
        """
        Add a scalar to each element of the vector.

        Args:
            object (float): The scalar value to add.

        Returns:
            None

        Raises:
            None
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

        return None

    def __mul__(self, object: int | float) -> None:
        """
        Multiply each element of the vector by a scalar.

        Args:
            object (float): The scalar value to multiply by.

        Returns:
            None

        Raises:
            None
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

        return None

    def __sub__(self, object: int | float) -> None:
        """
        Subtract a scalar from each element of the vector.

        Args:
            object (float): The scalar value to subtract.

        Returns:
            None

        Raises:
            None
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

        return None

    def __truediv__(self, object: int | float) -> None:
        """
        Divide each element of the vector by a scalar.

        Args:
            object (float): The scalar value to divide by.

        Returns:
            None

        Raises:
            ZeroDivisionError: If object is 0.
        """
        try:
            self.vector = [x / object for x in self.vector]
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            return None

        print(self.vector)

        return None


def main() -> int:
    """
    Main function to demonstrate calculator class.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        validate_args_for_prog()
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5

    return 0


if __name__ == "__main__":
    sys.exit(main())
