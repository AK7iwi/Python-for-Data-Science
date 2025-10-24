import sys
import numpy as np
import math
from validate_args import validate_args


def validate_measurement_content(values: list[int | float], name: str) -> None:
    """
    Validate that the data is a list of ints or floats that are finite and
    positive.

    Args:
        values (list[int | float]): The data to validate
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


def validate_measurement_structure(values: list[int | float],
                                   name: str) -> None:
    """
    Validate that the data is a list and not empty.

    Args:
        values (list[int | float]): The data to validate
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


def validate_measurement(values: list[int | float], name: str) -> None:
    """
    Validate measurement data.

    Args:
        values (list[int | float]): The data to validate
        name (str): The name of the parameter for error messages

    Returns:
        None

    Raises:
        None
    """
    validate_measurement_structure(values, name)
    validate_measurement_content(values, name)


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


def validate_data_limit(bmi: list[int | float], limit: int) -> None:
    """
    Validate that the data of apply_limit is valid.

    Args:
        bmi (list[int | float]): List of BMI values
        limit (int): The limit to validate

    Returns:
        None

    Raises:
        None
    """
    validate_limit(limit)
    validate_measurement(bmi, "BMI")


def validate_measurement_length(height: list[int | float],
                                weight: list[int | float]) -> None:
    """
    Validate that the height and weight lists have the same length.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        None

    Raises:
        ValueError: If the height and weight lists have different lengths
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size")


def validate_data_bmi(height: list[int | float],
                      weight: list[int | float]) -> None:
    """
    Validate that the data of give_bmi is valid.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        None

    Raises:
        None
    """
    validate_measurement(height, "Height")
    validate_measurement(weight, "Weight")
    validate_measurement_length(height, weight)


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
    validate_data_limit(bmi, limit)

    return (np.asarray(bmi) > limit).tolist()


def calculate_bmi(height: list[int | float],
                  weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.

    Args:
        height (list[int | float]): List of heights in meters
        weight (list[int | float]): List of weights in kilograms

    Returns:
        list[int | float]: List of BMI values

    Raises:
        None
    """
    return (np.asarray(weight) / (np.asarray(height) ** 2)).tolist()


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
        None
    """
    validate_data_bmi(height, weight)

    bmi = calculate_bmi(height, weight)

    return bmi


def main() -> int:
    """
    Main function to test give_bmi and apply_limit functions.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    limit = 26

    try:
        validate_args()

        bmi = give_bmi(height, weight)
        print(bmi)
        print(apply_limit(bmi, limit))

        return 0

    except ValueError as e:
        print(f"Value Error: {e}")
        return 1
    except TypeError as e:
        print(f"Type Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
