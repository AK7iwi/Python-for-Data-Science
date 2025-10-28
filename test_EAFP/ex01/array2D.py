import sys
import numpy as np
from validate_args import validate_args_for_test, MissingArgumentsError


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
    try:    
        family_array, sliced_array = slice_array(family, start, end)
    except IndexError as e:
        print(f"IndexError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

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
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
