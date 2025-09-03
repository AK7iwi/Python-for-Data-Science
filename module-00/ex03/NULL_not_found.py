def NULL_not_found(object: any) -> int:
    """
    Check the type of null-like objects and print their information.

    Args:
        object (any): The object to check for null-like properties

    Returns:
        int: 0 for recognized null types, 1 for unrecognized types

    Raises:
        None
    """
    try:
        if object is None:
            print(f"Nothing: None {type(object)}")
            return 0
        elif isinstance(object, float) and str(object) == "nan":
            print(f"Cheese: nan {type(object)}")
            return 0
        elif isinstance(object, bool) and object is False:
            print(f"Fake: False {type(object)}")
            return 0
        elif isinstance(object, int) and object == 0:
            print(f"Zero: 0 {type(object)}")
            return 0
        elif isinstance(object, str) and object == "":
            print(f"Empty: {type(object)}")
            return 0
        else:
            print("Type not Found")
            return 1

    except Exception as e:
        print(f"Error: {e}")
        return 1
