def all_thing_is_obj(object: any) -> int:
    """
    Print the type of the given object and return 42.
    Handles different data types with specific formatting.
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
            print("Type not found")
        else:
            print("Type not found")

        return 42

    except Exception as e:
        print(f"Error: {e}")
        return 1
