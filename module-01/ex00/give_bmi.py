import numpy as np
import math


def validate_params(values: list, name: str) -> None:
    """
    Check if all values in the list are numeric (int or float).

    Args:
        values (list): List of values to check
        name (str): Name of the parameter for error messages

    Returns:
        None

    Raises:
        TypeError: If any value is not int or float or the "list" is not a list
        ValueError: If the list is empty or any value is not finite or positive
    """
    # Check if the list is a list and not empty
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    if not values:
        raise ValueError(f"{name} cannot be empty")

    # Check if all values are int or float and are finite and positive
    for i, value in enumerate(values):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} at index {i} must be int or float")
        if not math.isfinite(value):
            raise ValueError(f"{name} at index {i} must be finite")
        if value <= 0:
            raise ValueError(f"{name} at index {i} must be positive")


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
        ValueError: If lists are not the same size
    """
    validate_params(height, "Height")
    validate_params(weight, "Weight")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size")

    # Convert to numpy arrays and calculate BMI
    h_array = np.array(height)
    w_array = np.array(weight)
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
        TypeError: If limit is not an integer
        ValueError: If limit is negative
    """
    validate_params(bmi, "BMI")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit must be positive")

    bmi_array = np.array(bmi)

    # Vectorized comparison
    return (bmi_array > limit).tolist()
