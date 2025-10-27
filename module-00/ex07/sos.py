import sys


def validate_args() -> str:
    """
    Validate command line arguments and return the string to encrypt.

    Args:
        None

    Returns:
        str: The string argument to convert to morse code

    Raises:
        AssertionError: If the number of arguments is not 2
    """
    args = sys.argv
    if len(args) != 2:
        raise AssertionError("the arguments are bad")

    arg = args[1]

    return arg


def get_dict() -> dict[str, str]:
    """
    Returns the nested morse code dictionary.

    Args:
        None

    Returns:
        dict: The morse code dictionary mapping characters to their morse
              representations

    Raises:
        None
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    return NESTED_MORSE


def encrypt(message: str) -> str:
    """
    Encrypts a message using the morse code chart.
    Converts alphanumeric characters and spaces to morse code.

    Args:
        message (str): The message to encrypt to morse code

    Returns:
        str: The encrypted message in morse code

    Raises:
        AssertionError: If the message contains invalid characters (KeyError exception)
    """
    NESTED_MORSE = get_dict()
    encrypted_message = ""
    for char in message.upper():
        try:
            encrypted_message += NESTED_MORSE[char]
        except KeyError:
            raise AssertionError("the arguments are bad")

    return encrypted_message.rstrip()


def main() -> int:
    """
    Main function that converts a string to morse code.
    Takes one string argument containing alphanumeric characters and spaces.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        arg = validate_args()
        encrypted_message = encrypt(arg)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1

    print(encrypted_message)

    return 0


if __name__ == "__main__":
    sys.exit(main())
