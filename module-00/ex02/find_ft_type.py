import sys
from validate_args import validate_args


def print_type_object(object: any) -> None:
    """
    Print the type of the given object.

    Args:
        object (any): The object to print the type of

    Returns:
        None

    Raises:
        TypeError: if the type is not found
    """
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        if len(object) == 0:
            raise TypeError("Empty string")
        else:
            print(f"{object} is in the kitchen : {type(object)}")
    else:
        raise TypeError("Type not found")


def all_thing_is_obj(object: any) -> int:
    """
    Check the type of the given object and return 42.

    Args:
        object (any): The object whose type will be printed

    Returns:
        int: Always returns 42

    Raises:
        None
    """
    try:
        print_type_object(object)

    except TypeError as e:
        print(e)

    return 42


def main() -> int:
    """
    Main function to test the all_thing_is_obj function.
    """
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    try:
        validate_args()

        all_thing_is_obj(ft_list)
        all_thing_is_obj(ft_tuple)
        all_thing_is_obj(ft_set)
        all_thing_is_obj(ft_dict)
        all_thing_is_obj("Brian")
        all_thing_is_obj("Toto")
        print(all_thing_is_obj(10))

        return 0

    except ValueError as e:
        print(f"ValueError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
