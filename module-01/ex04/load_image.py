import numpy as np
import os
from PIL import Image


def validate_path_exists(path: str) -> None:
    """
    Validate that the file path exists.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        FileNotFoundError: If file does not exist
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' not found")


def validate_image_format(path: str) -> None:
    """
    Validate that the file has a supported image format.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        ValueError: If file format is not supported
    """
    supported_formats = {'.jpg', '.jpeg', '.JPG', '.JPEG'}
    file_extension = os.path.splitext(path)[1]

    if file_extension not in supported_formats:
        raise ValueError(f"Unsupported image format: {file_extension}. "
                         f"Supported formats: JPG, JPEG")


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


def print_info(image_array: np.ndarray) -> None:
    """
    Print information about the image array.
    """
    print(f"The shape of image is: {image_array.shape}")


def load_image(path: str) -> np.ndarray:
    """
    Load an image file and return its RGB pixel content as a numpy array.
    """
    # Load image using PIL
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')

    return np.array(image)


def validate_path(path: str) -> None:
    """
    Validate that the path is a valid image file path.

    Args:
        path (str): The file path to validate

    Returns:
        None

    Raises:
        None
    """
    validate_path_string(path)
    validate_image_format(path)
    validate_path_exists(path)


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file and return its RGB pixel content as a numpy array.

    Args:
        path (str): Path to the image file

    Returns:
        np.ndarray: RGB pixel array of the image

    Raises:
        None
    """
    validate_path(path)
    image = load_image(path)
    print_info(image)

    return image


def main():
    """
    Main function to test the ft_load function.
    """
    try:
        print(ft_load("landscape.jpg"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
