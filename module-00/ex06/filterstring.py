import sys
from ft_filter import ft_filter


def main():
    """
    Main function that filters words from a string based on length.
    Takes two arguments: string and integer.
    """
    try:
        # Check number of arguments
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        # Get arguments
        string_arg = sys.argv[1]
        integer_arg = sys.argv[2]

        try:
            integer_arg = int(integer_arg)
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Filter the string
        result = ft_filter(lambda x: len(x) > integer_arg, string_arg.split())

        # Print result
        print(result)

        return 0

    except Exception as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()
