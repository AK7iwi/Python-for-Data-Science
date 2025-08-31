import sys


# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
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
    "9": "----. "
}


def encrypt(message):
    """
    Encrypts a message using the morse code chart.
    Converts alphanumeric characters and spaces to morse code.
    """
    encrypted_message = ""
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            encrypted_message += MORSE_CODE_DICT[char]
        else:
            raise AssertionError("the arguments are bad")

    return encrypted_message


def main():

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
