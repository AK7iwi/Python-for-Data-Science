import pandas as pd
import os
import sys


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV dataset and return it with dimensions information.
    
    Args:
        path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame | None: Loaded dataset or None if error occurs

    Raises:
        FileNotFoundError: If file does not exist
        PermissionError: If permission is denied to access the file
        pd.errors.ParserError: If the file cannot be parsed
        pd.errors.EmptyDataError: If the file is empty
        Exception: If an unexpected error occurs
    """
    try:
        # Validate path exists and is a file
        if not os.path.exists(path):
            print(f"Error: File '{path}' not found")
            return None
            
        if not os.path.isfile(path):
            print(f"Error: '{path}' is not a file")
            return None
            
        # Check file extension
        if not path.lower().endswith('.csv'):
            print(f"Error: File '{path}' is not a CSV file")
            return None
            
        # Load the CSV file
        dataset = pd.read_csv(path)
        
        # Print dimensions
        print(f"Loading dataset of dimensions {dataset.shape}")
        
        return dataset
        
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
        print(f"Error: Unexpected error loading '{path}': {e}")
        return None


def main():
    """Main function to test the load function."""
    if len(sys.argv) != 2:
        print("Usage: python load_csv.py <csv_file_path>")
        return
        
    file_path = sys.argv[1]
    result = load(file_path)
    
    if result is not None:
        print(result)


if __name__ == "__main__":
    sys.exit(main())
