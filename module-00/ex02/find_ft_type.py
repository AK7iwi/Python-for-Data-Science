def all_thing_is_obj(object: any) -> int:
    """
    Print the type of the given object and return 42.

    Args:
        object (any): The object whose type will be printed

    Returns:
        int: Always returns 42

    Raises:
        None
    """
    try:
        if isinstance(object, list):
            print(f"List : {type(object)}")
        elif isinstance(object, tuple):
            print(f"Tuple : {type(object)}")
        elif isinstance(object, set):
            print(f"Set : {type(object)}")
        elif isinstance(object, dict):
            print(f"Dict : {type(object)}")
        elif isinstance(object, str):
            print(f"{object} is in the kitchen : {type(object)}")
        elif isinstance(object, int):
            print("Type not found") ## Raise error
        else:
            print("Type not found") ## Raise error + merge with top condition

        return 42

    except Exception as e:
        print(f"Error: {e}")
        return 1
