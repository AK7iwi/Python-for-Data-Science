import numpy as np

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
        TypeError: If family is not a list or contains non-lists
        ValueError: If family is empty or rows have different sizes
    """
    # Check if family is a list
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    
    if not family:
        raise ValueError("Family cannot be empty")
    
    # Check if all elements are lists and have the same size
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements in family must be lists")
    
    # Check if all rows have the same size
    first_row_size = len(family[0])
    for i, row in enumerate(family):
        if len(row) != first_row_size:
            raise ValueError(f"Row {i} has different size than first row")
    
    # Convert to numpy array
    family_array = np.array(family)
    
    # Print original shape
    print(f"My shape is : {family_array.shape}")
    
    # Slice the array
    sliced_array = family_array[start:end]
    
    # Print new shape
    print(f"My new shape is : {sliced_array.shape}")
    
    # Return as list
    return sliced_array.tolist()