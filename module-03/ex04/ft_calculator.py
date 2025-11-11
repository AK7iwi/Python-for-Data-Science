"""
Module ft_calculator: Calculator class for vector operations.
"""
import sys
from validate_args import validate_args_for_prog


class calculator:
    """
    Calculator class for performing operations on two vectors.

    All methods are static and can be called without instantiating the class.
    """

    # ==================== Methods ==================== #
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None

        Raises:
            None
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None

        Raises:
            None
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors element-wise (V1 - V2).

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None

        Raises:
            None
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


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

    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)

    return 0


if __name__ == "__main__":
    sys.exit(main())
