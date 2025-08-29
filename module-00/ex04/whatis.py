import sys


def main():
    """
    Main function that checks if a number is odd or even.
    Takes one command line argument and validates it.
    """
    try:
        # Check number of arguments
        if len(sys.argv) != 2:
            if len(sys.argv) > 2:
                raise AssertionError("more than one argument is provided")
            return

        # Get the argument
        arg = sys.argv[1]

        # Check if argument is an integer
        try:
            number = int(arg)
        except ValueError:
            raise AssertionError("argument is not an integer")

        # Check if odd or even
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except Exception as e:
        print(f"AssertionError: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
