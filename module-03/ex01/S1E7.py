"""
Module S1E7: Baratheon and Lannister classes implementation.
"""
import sys
from S1E9 import Character
from validate_args import validate_args_for_prog


class Baratheon(Character):
    """
    Class representing a Baratheon character, inheriting from Character.

    Attributes:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): Whether the Baratheon character is alive.
        family_name (str): The family name, always 'Baratheon'.
        eyes (str): Eye color, always 'brown'.
        hairs (str): Hair color, always 'dark'.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Baratheon instance.

        Args:
            first_name (str): The first name of the Baratheon character.
            is_alive (bool, optional): Whether the Baratheon character
                is alive. Defaults to True.

        Returns:
            None

        Raises:
            TypeError: If first_name is not a string, is_alive is not
                a boolean, family_name is not a string, eyes is not a string,
                or hairs is not a string.
            ValueError: If first_name, family_name, eyes, or hairs is empty.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # ==================== Properties ==================== #
    @property
    def family_name(self) -> str:
        """
        Get the family name of the Baratheon character.

        Returns:
            str: The family name.
        """
        return self._family_name

    @family_name.setter
    def family_name(self, value: str) -> None:
        """
        Set the family name of the Baratheon character with validation.

        Args:
            value (str): The family name to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("family_name must be a string")
        if not value.strip():
            raise ValueError("family_name cannot be empty")

        self._family_name = value

    @property
    def eyes(self) -> str:
        """
        Get the eye color of the Baratheon character.

        Returns:
            str: The eye color.
        """
        return self._eyes

    @eyes.setter
    def eyes(self, value: str) -> None:
        """
        Set the eye color of the Baratheon character with validation.

        Args:
            value (str): The eye color to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("eyes must be a string")
        if not value.strip():
            raise ValueError("eyes cannot be empty")

        self._eyes = value

    @property
    def hairs(self) -> str:
        """
        Get the hair color of the Baratheon character.

        Returns:
            str: The hair color.
        """
        return self._hairs

    @hairs.setter
    def hairs(self, value: str) -> None:
        """
        Set the hair color of the Baratheon character with validation.

        Args:
            value (str): The hair color to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("hairs must be a string")
        if not value.strip():
            raise ValueError("hairs cannot be empty")

        self._hairs = value

    # ==================== Methods ==================== #
    def die(self) -> None:
        """
        Set the Baratheon character's is_alive attribute to False.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Return a string representation of the Baratheon character.

        Args:
            None

        Returns:
            str: String representation in the format
                 "Vector: ('family_name', 'eyes', 'hairs')"

        Raises:
            None
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Return a string representation of the Baratheon character.

        Args:
            None

        Returns:
            str: String representation in the format
                 "Vector: ('family_name', 'eyes', 'hairs')"

        Raises:
            None
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Class representing a Lannister character, inheriting from Character.

    Attributes:
        first_name (str): The first name of the Lannister character.
        is_alive (bool): Whether the Lannister character is alive.
        family_name (str): The family name, always 'Lannister'.
        eyes (str): Eye color, always 'blue'.
        hairs (str): Hair color, always 'light'.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initialize a Lannister instance.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): Whether the Lannister character
                is alive. Defaults to True.

        Returns:
            None

        Raises:
            TypeError: If first_name is not a string, is_alive is not
                a boolean, family_name is not a string, eyes is not a string,
                or hairs is not a string.
            ValueError: If first_name, family_name, eyes, or hairs is empty.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    # ==================== Properties ==================== #
    @property
    def family_name(self) -> str:
        """
        Get the family name of the Lannister character.

        Returns:
            str: The family name.
        """
        return self._family_name

    @family_name.setter
    def family_name(self, value: str) -> None:
        """
        Set the family name of the Lannister character with validation.

        Args:
            value (str): The family name to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("family_name must be a string")
        if not value.strip():
            raise ValueError("family_name cannot be empty")

        self._family_name = value

    @property
    def eyes(self) -> str:
        """
        Get the eye color of the Lannister character.

        Returns:
            str: The eye color.
        """
        return self._eyes

    @eyes.setter
    def eyes(self, value: str) -> None:
        """
        Set the eye color of the Lannister character with validation.

        Args:
            value (str): The eye color to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("eyes must be a string")
        if not value.strip():
            raise ValueError("eyes cannot be empty")

        self._eyes = value

    @property
    def hairs(self) -> str:
        """
        Get the hair color of the Lannister character.

        Returns:
            str: The hair color.
        """
        return self._hairs

    @hairs.setter
    def hairs(self, value: str) -> None:
        """
        Set the hair color of the Lannister character with validation.

        Args:
            value (str): The hair color to set.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is empty.
        """
        if not isinstance(value, str):
            raise TypeError("hairs must be a string")
        if not value.strip():
            raise ValueError("hairs cannot be empty")

        self._hairs = value

    # ==================== Methods ==================== #
    def die(self) -> None:
        """
        Set the Lannister character's is_alive attribute to False.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Return a string representation of the Lannister character.

        Args:
            None

        Returns:
            str: String representation in the format
                 "Vector: ('family_name', 'eyes', 'hairs')"

        Raises:
            None
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Return a string representation of the Lannister character.

        Args:
            None

        Returns:
            str: String representation in the format
                 "Vector: ('family_name', 'eyes', 'hairs')"

        Raises:
            None
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> "Lannister":
        """
        Class method to create a Lannister character.

        Args:
            first_name (str): The first name of the Lannister character.
            is_alive (bool, optional): Whether the Lannister character
                is alive. Defaults to True.

        Returns:
            Lannister: A new Lannister instance.

        Raises:
            None
        """
        return cls(first_name, is_alive)


def main() -> int:
    """
    Main function to demonstrate Baratheon and Lannister classes.

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

    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    name_info = (Jaine.first_name, type(Jaine).__name__)
    print(f"Name : {name_info}, Alive : {Jaine.is_alive}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
