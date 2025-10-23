import sys
import string


def validate_args() -> str:
    """
    Validate command line arguments and return the text to process.

    Args:
        None

    Returns:
        str: The text to count characters from

    Raises:
        AssertionError: If more than one argument is provided
        or if the input is interrupted (EOFError, KeyboardInterrupt exceptions)
    """
    args = sys.argv
    if len(args) == 1 or (len(args) == 2 and args[1] == ""):
        while True:
            try:
                text = input("What is the text to count?\n")
                if text:
                    break
                print("Please provide a non-empty text.")
            except (EOFError, KeyboardInterrupt):
                raise AssertionError("input was interrupted")
    elif len(args) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        text = args[1]

    return text


def print_results(text: str, upper_count: int, lower_count: int,
                  digit_count: int, space_count: int,
                  punct_count: int) -> None:
    """
    Print the character count results in the specified format.

    Args:
        text (str): The input text
        upper_count (int): Count of uppercase letters
        lower_count (int): Count of lowercase letters
        digit_count (int): Count of digits
        space_count (int): Count of spaces
        punct_count (int): Count of punctuation marks

    Returns:
        None

    Raises:
        None
    """
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def count_characters(text: str) -> tuple[int, int, int, int, int]:
    """
    Count different types of characters in the given text.

    Args:
        text (str): The text to count characters from

    Returns:
        tuple: A tuple containing (upper_count, lower_count, digit_count,
               space_count, punct_count)
            - upper_count (int): Count of uppercase letters
            - lower_count (int): Count of lowercase letters
            - digit_count (int): Count of digits
            - space_count (int): Count of spaces
            - punct_count (int): Count of punctuation marks

    Raises:
        None
    """
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    punct_count = sum(1 for char in text if char in string.punctuation)

    return upper_count, lower_count, digit_count, space_count, punct_count


def main() -> int:
    """
    Main function that counts character types in a string argument.
    Takes zero or one command line argument: an optional string to analyze.
    If no argument is provided, prompts user for input.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        text = validate_args()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1

    upper_count, lower_count, digit_count, space_count, punct_count = (
        count_characters(text))
    print_results(text, upper_count, lower_count, digit_count, space_count,
                  punct_count)

    return 0


if __name__ == "__main__":
    sys.exit(main())
