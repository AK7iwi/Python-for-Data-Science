import sys


def get_dict():
    """
    Returns the nested morse code dictionary.
    """
    # Dictionary representing the morse code chart
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


def encrypt(message):
    """
    Encrypts a message using the morse code chart.
    Converts alphanumeric characters and spaces to morse code.
    """

    NESTED_MORSE = get_dict()
    encrypted_message = ""
    for char in message.upper():
        if char in NESTED_MORSE:
            encrypted_message += NESTED_MORSE[char]
        else:
            raise AssertionError("the arguments are bad")

    return encrypted_message.rstrip()


def main():
    """
    Main function that converts a string to morse code.
    Takes one string argument containing alphanumeric characters and spaces.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        arg = sys.argv[1]

        encrypted_message = encrypt(arg)
        print(encrypted_message)

        return 0

    except Exception as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()
