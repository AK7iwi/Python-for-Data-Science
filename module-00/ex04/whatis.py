import sys

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        return
    
    arg = sys.argv[1]
    
    try:
        number = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
