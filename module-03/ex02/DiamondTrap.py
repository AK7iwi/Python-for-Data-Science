"""
Module DiamondTrap: King class with multiple inheritance.
"""
import sys
from S1E7 import Baratheon, Lannister
from validate_args import validate_args_for_prog


class King(Baratheon, Lannister):
    """
    Class representing a King, inheriting from both Baratheon and Lannister.

    This demonstrates the diamond problem in multiple inheritance,
    resolved by Python's C3 linearization (Method Resolution Order).

    Attributes:
        first_name (str): The first name of the King.
        is_alive (bool): Whether the King is alive.
        family_name (str): The family name.
        eyes (str): Eye color.
        hairs (str): Hair color.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a King instance.

        Args:
            first_name (str): The first name of the King.
            is_alive (bool, optional): Whether the King is alive.
                Defaults to True.

        Returns:
            None

        Raises:
            None
        """
        super().__init__(first_name, is_alive)

    # ==================== Methods ==================== #
    def get_eyes(self) -> str:
        """
        Get the eye color of the King (uses the eyes property).

        Args:
            None

        Returns:
            str: The eye color.

        Raises:
            None
        """
        return self.eyes

    def set_eyes(self, color: str) -> None:
        """
        Set the eye color of the King (uses the eyes property).

        Args:
            color (str): The new eye color.

        Returns:
            None

        Raises:
            None
        """
        self.eyes = color

    def get_hairs(self) -> str:
        """
        Get the hair color of the King (uses the hairs property).

        Args:
            None

        Returns:
            str: The hair color.

        Raises:
            None
        """
        return self.hairs

    def set_hairs(self, color: str) -> None:
        """
        Set the hair color of the King (uses the hairs property).

        Args:
            color (str): The new hair color.

        Returns:
            None

        Raises:
            None
        """
        self.hairs = color


def main() -> int:
    """
    Main function to demonstrate King class with multiple inheritance.

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

    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    return 0


if __name__ == "__main__":
    sys.exit(main())
