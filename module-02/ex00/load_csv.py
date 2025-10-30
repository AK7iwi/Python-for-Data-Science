import sys
import pandas as pd
from validate_args import validate_args_for_test, MissingArgumentsError


def validate_csv_format(path: str) -> None:
    """
    Validate that the file has a CSV format.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        ValueError: If file format is not CSV
    """
    with open(path, 'r'):
        pass
    if not path.lower().endswith('.csv'):
        raise ValueError(f"Not a CSV file: '{path}'")


def validate_path_string(path: str) -> None:
    """
    Validate that the path is a non-empty string.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        TypeError: If path is not a string
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string")


def validate_path(path: str) -> None:
    """
    Validate that the path is a valid CSV file path.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        None
    """
    validate_path_string(path)
    validate_csv_format(path)


def print_dataset_info(dataset: pd.DataFrame) -> None:
    """
    Print detailed information about the dataset.

    Args:
        dataset (pd.DataFrame): The dataset to print information about

    Returns:
        None

    Raises:
        None
    """
    print(f"Loading dataset of dimensions {dataset.shape}")


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV dataset and return it with dimensions information.

    Args:
        path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded dataset
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_path(path)
        dataset = pd.read_csv(path)
    except pd.errors.EmptyDataError as e:
        print(f"EmptyDataError: {e}")
        return None
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except IsADirectoryError:
        print(f"IsADirectoryError: Is a directory: '{path}'")
        return None
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: '{path}'")
        return None
    except PermissionError:
        print(f"PermissionError: Permission denied: '{path}'")
        return None

    print_dataset_info(dataset)

    return dataset


def main() -> int:
    """
    Main function to test the load function.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    print(load("../csv_files/valid_csv/life_expectancy_years.csv"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
