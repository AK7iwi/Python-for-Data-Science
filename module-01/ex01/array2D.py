import numpy as np


def validate_slice_indices(start: int, end: int, array_length: int) -> None:
    """
    Validate that start and end indices are valid for slicing.
    
    Args:
        start (int): Start index for slicing
        end (int): End index for slicing
        array_length (int): Length of the array to slice
        
    Returns:
        None
        
    Raises:
        TypeError: If start or end are not integers
        ValueError: If indices are out of bounds
    """
    if not isinstance(start, int):
        raise TypeError("Start must be an integer")
    if not isinstance(end, int):
        raise TypeError("End must be an integer")
    
    # Check bounds for positive indices
    if start >= 0 and start >= array_length:
        raise ValueError(f"Start index {start} is out of bounds (max: {array_length - 1})")
    if end > 0 and end >= array_length:
        raise ValueError(f"End index {end} is out of bounds (max: {array_length - 1})")
    
    # Check bounds for negative indices
    if start < 0 and abs(start) > array_length:
        raise ValueError(f"Start index {start} is out of bounds (min: {-array_length})")
    if end < 0 and abs(end) > array_length:
        raise ValueError(f"End index {end} is out of bounds (min: {-array_length})")

    if start == end:
        raise ValueError("Start and end indices cannot be the same")
    if start == array_length - 1:
        raise ValueError("Start index cannot be the last index")
    if end == 0:
        raise ValueError("End index cannot be 0")
    


def validate_2d_array(family: list) -> None:
    """
    Validate that the input is a proper 2D array.
    
    Args:
        family (list): The 2D list to validate
        
    Returns:
        None
        
    Raises:
        TypeError: If family is not a list or contains non-lists
        ValueError: If family is empty or rows have different sizes
    """
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not family:
        raise ValueError("Family cannot be empty")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements in family must be lists")

    first_row_size = len(family[0])
    for i, row in enumerate(family):
        if len(row) == 0:
            raise ValueError(f"Row {i} is empty")
        if len(row) != first_row_size:
            raise ValueError(f"Row {i} has different size than first row")


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