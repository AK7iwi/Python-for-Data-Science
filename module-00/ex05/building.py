import sys
import string


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
        None: This function only prints to stdout

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


def validate_argument() -> str:
    """
    Validate command line arguments and return the text to process.

    Args:
        None

    Returns:
        str: The text to count characters from

    Raises:
        AssertionError: If more than one argument is provided
    """
    # Check number of arguments
    if len(sys.argv) == 1:
        # No argument provided, prompt user
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        # One argument provided
        text = sys.argv[1]
    else:
        # More than one argument
        raise AssertionError("more than one argument is provided")

    return text


def main():
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
        # Validate argument
        text = validate_argument()

        # Count characters
        upper_count, lower_count, digit_count, space_count, punct_count = (
            count_characters(text)
        )

        # Print results
        print_results(text, upper_count, lower_count, digit_count, space_count,
                      punct_count)

        return 0

    except Exception as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()
