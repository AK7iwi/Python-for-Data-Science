import numpy as np
import math


def validate_data_content(values: list, name: str) -> None:
    """
    Validate that the data is a list of int or float
    and is finite and positive.

    Args:
        values (list): The data to validate
        name (str): The name of the parameter for error messages

    Returns:
        None

    Raises:
        TypeError: If the data is not a list of int or float
        ValueError: If the data is not finite or positive
    """
    for i, value in enumerate(values):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} at index {i} must be int or float")
        if not math.isfinite(value):
            raise ValueError(f"{name} at index {i} must be finite")
        if value <= 0:
            raise ValueError(f"{name} at index {i} must be positive")


def validate_data_structure(values: list, name: str) -> None:
    """
    Validate that the data is a list and not empty.

    Args:
        values (list): The data to validate
        name (str): The name of the parameter for error messages

    Returns:
        None

    Raises:
        TypeError: If the data is not a list
        ValueError: If the data is empty
    """
    if not isinstance(values, list):
        raise TypeError(f"{name} must be a list")
    if not values:
        raise ValueError(f"{name} cannot be empty")


def validate_data(values: list, name: str) -> None:
    """
    Validate that the data is a list of int or float and is finite
    and positive.

    Args:
        values (list): List of values to check
        name (str): Name of the parameter for error messages

    Returns:
        None

    Raises:
        None
    """

    validate_data_structure(values, name)
    validate_data_content(values, name)


def validate_limit(limit: int) -> None:
    """
    Validate that the limit is an integer and is positive.

    Args:
        limit (int): The limit to validate

    Returns:
        None

    Raises:
        TypeError: If limit is not an integer
        ValueError: If limit is negative
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    if limit < 0:
        raise ValueError("Limit must be positive")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values and return boolean list.

    Args:
        bmi (list[int | float]): List of BMI values
        limit (int): The limit to compare against

    Returns:
        list[bool]: List of booleans (True if BMI > limit)

    Raises:
        None
    """
    validate_limit(limit)
    validate_data(bmi, "BMI")

    bmi_array = np.array(bmi)

    # Vectorized comparison
    return (bmi_array > limit).tolist()


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
    validate_data(height, "Height")
    validate_data(weight, "Weight")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size")

    # Convert to numpy arrays
    h_array = np.array(height)
    w_array = np.array(weight)

    # Calculate BMI
    bmi_array = w_array / (h_array ** 2)

    return bmi_array.tolist()
