"""
Module new_student: Student dataclass implementation.
"""
import sys
import random
import string
from dataclasses import dataclass, field
from validate_args import validate_args_for_test, MissingArgumentsError


def generate_id() -> str:
    """
    Generate a random ID string.

    Returns:
        str: A random 15-character lowercase string.

    Raises:
        None
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Dataclass representing a student.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Whether the student is active. Defaults to True.
        login (str): The student's login (generated from surname).
        id (str): The student's unique ID (randomly generated).
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """
        Post-initialization processing.

        Generates the login from the first letter of name plus surname.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.login = self.name[0].capitalize() + self.surname.lower()


def main() -> int:
    """
    Main function to test the Student dataclass.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    student = Student(name="Edward", surname="agle")
    print(student)

    return 0


if __name__ == "__main__":
    sys.exit(main())
