import numpy as np


def validate_indices_bounds(start: int, end: int, array_length: int) -> None:
    """
    Validate that indices are within the bounds of the array.

    Args:
        start (int): Start index for slicing
        end (int): End index for slicing
        array_length (int): Length of the array to slice

    Returns:
        None

    Raises:
        ValueError: If indices are out of bounds
    """
    # Normalize negative indices to positive
    start_normalized = start if start >= 0 else array_length + start
    end_normalized = end if end >= 0 else array_length + end

    # not `>=` for end to allow the last index value
    if start_normalized < 0 or start_normalized >= array_length:
        raise ValueError(f"Start index {start} is out of bounds "
                         f"(min: {-array_length}, max: {array_length - 1})")
    if end_normalized < 0 or end_normalized > array_length:
        raise ValueError(f"End index {end} is out of bounds "
                         f"(min: {-array_length}, max: {array_length})")
    if end_normalized < start_normalized:
        raise ValueError("End index must be greater than start index")


def validate_indice_type(indice: int, name: str) -> None:
    """
    Validate that the indice is an integer.

    Args:
        indice (int): The indice to validate
        name (str): The name of the indice

    Returns:
        None

    Raises:
        TypeError: If the indice is not an integer
    """
    if not isinstance(indice, int):
        raise TypeError(f"{name} must be an integer")


def validate_slice_indices(start: int, end: int, array_length: int) -> None:
    """
    Validate that indices are valid for slicing.

    Args:
        start (int): Start index for slicing
        end (int): End index for slicing
        array_length (int): Length of the array to slice

    Returns:
        None

    Raises:
        None
    """
    validate_indice_type(start, "Start")
    validate_indice_type(end, "End")
    validate_indices_bounds(start, end, array_length)


def validate_2d_array_content(family: list) -> None:
    """
    Validate that the 2D array contains only lists, no empty rows and has the
    same size for all rows.

    Args:
        family (list): The 2D list to validate

    Returns:
        None

    Raises:
        TypeError: If input contains non-lists
        ValueError: If input contains empty rows or rows have different sizes
    """
    first_row_size = len(family[0])
    for i, row in enumerate(family):
        if not isinstance(row, list):
            raise TypeError("All elements in family must be lists")
        if len(row) == 0:
            raise ValueError(f"Row {i} is empty")
        if len(row) != first_row_size:
            raise ValueError(f"Row {i} has different size than first row")


def validate_2d_array_structure(family: list) -> None:
    """
    Validate that the 2D array is a valid list of lists.

    Args:
        family (list): The 2D list to validate

    Returns:
        None

    Raises:
        TypeError: If input is not a list
        ValueError: If input is empty
    """
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not family:
        raise ValueError("Family cannot be empty")


def validate_2d_array(family: list) -> None:
    """
    Validate that the input is a proper 2D array.

    Args:
        family (list): The 2D list to validate

    Returns:
        None

    Raises:
        None
    """
    validate_2d_array_structure(family)
    validate_2d_array_content(family)


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and return the truncated version.

    Args:
        family (list): 2D list to slice
        start (int): Start index for slicing
        end (int): End index for slicing

    Returns:
        list: Sliced 2D array as a list

    Raises:
        None
    """
    validate_2d_array(family)
    validate_slice_indices(start, end, len(family))

    family_array = np.array(family)
    print(f"My shape is : {family_array.shape}")

    sliced_array = family_array[start:end]
    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
