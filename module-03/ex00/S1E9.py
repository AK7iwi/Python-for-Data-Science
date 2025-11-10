"""
Module S1E9: Character and Stark classes implementation.
"""
import sys
from abc import ABC, abstractmethod
from validate_args import validate_args_for_prog


class Character(ABC):
    """
    Abstract base class representing a character.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): Whether the character is alive.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Character instance.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.

        Returns:
            None

        Raises:
            TypeError: If first_name is not a string or is_alive is not a boolean.
            ValueError: If first_name is empty.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @property
    def first_name(self) -> str:
        """
        Get the first name of the character.

        Returns:
            str: The first name of the character.
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """
        Set the first name of the character with validation.

        Args:
            value (str): The first name to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("first_name must be a string")
        if not value.strip():
            raise ValueError("first_name cannot be empty")
        self._first_name = value

    @property
    def is_alive(self) -> bool:
        """
        Get the alive status of the character.

        Returns:
            bool: Whether the character is alive.
        """
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value: bool) -> None:
        """
        Set the alive status of the character with validation.

        Args:
            value (bool): The alive status to set.

        Raises:
            TypeError: If value is not a boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("is_alive must be a boolean")
        self._is_alive = value

    @abstractmethod
    def die(self) -> None:
        """
        Abstract method to change the health state of the character.

        This method should set is_alive from True to False.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        pass


class Stark(Character):
    """
    Class representing a Stark character, inheriting from Character.

    Attributes:
        first_name (str): The first name of the Stark character.
        is_alive (bool): Whether the Stark character is alive.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Stark instance.

        Args:
            first_name (str): The first name of the Stark character.
            is_alive (bool, optional): Whether the Stark character is alive.
                Defaults to True.

        Returns:
            None

        Raises:
            TypeError: If first_name is not a string or is_alive is not a boolean.
            ValueError: If first_name is empty.
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Set the Stark character's is_alive attribute to False.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.is_alive = False


def main() -> int:
    """
    Main function to demonstrate Character and Stark classes.

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

    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    return 0


if __name__ == "__main__":
    sys.exit(main())
