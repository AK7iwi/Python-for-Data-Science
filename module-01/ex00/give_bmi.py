import numpy as np


def check_type(values: list) -> None:
    """
    Check if all values in the list are numeric (int or float).

    Args:
        values (list): List of values to check
        name (str): Name of the parameter for error messages

    Returns:
        None

    Raises:
        TypeError: If any value is not int or float
    """
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError("All values must be int or float")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        list[int | float]: List of BMI values

    Raises:
        TypeError: If lists contain non-numeric values
        ValueError: If lists are not the same size or contain invalid values
    """
    # Check if all elements are numeric before converting to numpy
    check_type(height)
    check_type(weight)

    # Convert to numpy arrays
    h_array = np.array(height)
    w_array = np.array(weight)

    # Check if lists have the same length
    if len(h_array) != len(w_array):
        raise ValueError("Height and weight lists must have the same size")

    # Check for valid values (numpy handles type checking automatically)
    if not np.all(np.isfinite(h_array)) or not np.all(np.isfinite(w_array)):
        raise ValueError("All values must be finite numbers")

    if np.any(h_array <= 0) or np.any(w_array <= 0):
        raise ValueError("All values must be positive")

    # Calculate BMI using vectorized operation
    bmi_array = w_array / (h_array ** 2)

    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values and return boolean list.

    Args:
        bmi (list[int | float]): List of BMI values
        limit (int): The limit to compare against

    Returns:
        list[bool]: List of booleans (True if BMI > limit)

    Raises:
        TypeError: If bmi contains non-numeric values or limit is not int
        ValueError: If limit is negative
    """
    bmi_array = np.array(bmi)

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit must be non-negative")

    # Vectorized comparison
    return (bmi_array > limit).tolist()
