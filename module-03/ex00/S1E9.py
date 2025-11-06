"""
Module S1E9: Character and Stark classes implementation.
"""
from abc import ABC, abstractmethod


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
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """
        Abstract method to change the health state of the character.

        This method should set is_alive from True to False.

        Args:
            None

        Returns:
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
        """
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """
        Set the Stark character's is_alive attribute to False.

        Args:
            None

        Returns:
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
        ned = Stark("Ned")
        print(ned.__dict__)
        print(ned.is_alive)
        ned.die()
        print(ned.is_alive)
        print(ned.__doc__)
        print(ned.__init__.__doc__)
        print(ned.die.__doc__)
        print("---")
        lyanna = Stark("Lyanna", False)
        print(lyanna.__dict__)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
