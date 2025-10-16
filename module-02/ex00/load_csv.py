import sys
import os
import pandas as pd
from validate_args import validate_args


def validate_path_exists(path: str) -> None:
    """
    Validate that the file path exists and is a file.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        FileNotFoundError: If file does not exist or is not a file
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' not found")
    
    if not os.path.isfile(path):
        raise FileNotFoundError(f"'{path}' is not a file")


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
    if not path.lower().endswith('.csv'):
        raise ValueError(f"File '{path}' is not a CSV file")


def validate_path_string(path: str) -> None:
    """
    Validate that the path is a non-empty string.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        TypeError: If path is not a string
        ValueError: If path is empty
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    if not path.strip():
        raise ValueError("Path cannot be empty")


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
    validate_path_exists(path)


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


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return it as a pandas DataFrame.

    Args:
        path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded dataset

    Raises:
        None
    """
    dataset = pd.read_csv(path)

    return dataset


def load(path: str) -> pd.DataFrame | None:
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
        # validate_path(path)
        dataset = load_csv(path)
        print_dataset_info(dataset)

        return dataset

    # except (FileNotFoundError, ValueError, TypeError) as e:
    #     print(f"Error: {e}")
    #     return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: Cannot parse CSV file '{path}': {e}")
        return None
    except PermissionError:
        print(f"Error: Permission denied accessing '{path}'")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main() -> int:
    """
    Main function to test the load function.
    """
    try:
        validate_args()
        
        print(load("../csv_files/life_expectancy_years.csv"))

        return 0
        
    except Exception:
        return 1


if __name__ == "__main__":
    sys.exit(main())
