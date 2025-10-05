from whatis import validate_argument, check_odd_even


def main():
    try:    
        number = validate_argument()
        if number is not None:
            check_odd_even(number)
    except Exception as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()