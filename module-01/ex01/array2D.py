import sys
import numpy as np
from validate_args import validate_args


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
            raise TypeError(f"Row {i} must be a list")
        if len(row) == 0:
            raise ValueError(f"Row {i} cannot be empty")
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


def validate_data(family: list, start: int, end: int) -> None:
    """
    Validate that the data of slice_me is valid.

    Args:
        family (list): 2D list to validate
        start (int): Start index for slicing
        end (int): End index for slicing

    Returns:
        None

    Raises:
        None
    """
    validate_2d_array(family)
    validate_slice_indices(start, end, len(family))


def print_info(family_array: np.ndarray, sliced_array: np.ndarray) -> None:

    """
    Print information about the arrays.

    Args:
        family_array (np.ndarray): The original array
        sliced_array (np.ndarray): The sliced array

    Returns:
        None

    Raises:
        None
    """
    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {sliced_array.shape}")


def slice_array(family: list, start: int, end: int) -> tuple[np.ndarray,
                                                             np.ndarray]:
    """
    Slice a 2D array and return the truncated version.

    Args:
        family (list): 2D list to slice
        start (int): Start index for slicing
        end (int): End index for slicing

    Returns:
        tuple[np.ndarray, np.ndarray]: The original and sliced arrays

    Raises:
        None
    """
    family_array = np.asarray(family)
    sliced_array = family_array[start:end]

    return family_array, sliced_array


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
    validate_data(family, start, end)

    family_array, sliced_array = slice_array(family, start, end)
    print_info(family_array, sliced_array)

    return sliced_array.tolist()


def main() -> int:
    """
    Main function to test the slice_me function.
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    try:
        validate_args()

        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
