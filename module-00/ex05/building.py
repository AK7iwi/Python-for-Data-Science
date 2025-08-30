import sys
import string


def count_characters(text):
    """
    Count different types of characters in the given text.
    Returns counts for uppercase, lowercase, punctuation, digits, and spaces.
    """
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    punct_count = sum(1 for char in text if char in string.punctuation)
    
    return upper_count, lower_count, digit_count, space_count, punct_count


def main():
    """
    Main function that counts character types in a string argument.
    Prompts for input if no argument is provided.
    """
    try:
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
        
        # Count characters
        upper_count, lower_count, digit_count, space_count, punct_count = count_characters(text)
        
        # Print results
        print(f"The text contains {len(text)} characters:")
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punct_count} punctuation marks")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")
        
        return 0
        
    except Exception as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()