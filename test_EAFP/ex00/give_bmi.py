import sys
import numpy as np
import math
from validate_args import validate_args_for_test, MissingArgumentsError


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values and return boolean list (True if BMI > limit).

    Args:
        bmi (list[int | float]): List of BMI values
        limit (int): The limit to compare against

    Returns:
        list[bool]: List of booleans (True if BMI > limit)
        None: If the data is invalid

    Raises:
        None
    """
    try:
        limit = (np.asarray(bmi) > limit).tolist()
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

    return limit


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
        None: If the data is invalid

    Raises:
        None
    """
    try:
        bmi = calculate_bmi(height, weight)
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

    return bmi


def main() -> int:
    """
    Main function to test give_bmi and apply_limit functions.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    limit = 26

    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

    return 0


if __name__ == "__main__":
    sys.exit(main())
