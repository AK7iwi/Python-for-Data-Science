import sys
import os
import numpy as np
from PIL import Image
from validate_args import validate_args


def print_image_info(image: np.ndarray) -> None:
    """
    Print detailed information about the image.

    Args:
        image (np.ndarray): The image to print information about

    Returns:
        None

    Raises:
        None
    """
    height, width = image.shape[:2]
    if len(image.shape) == 2:
        channels = 1
    else:
        channels = image.shape[2]

    print("="*50)
    print(f"The shape of image is: {image.shape}")
    print("\nImage dimensions:")
    print(f"-Width (X axis): {width} pixels")
    print(f"-Height (Y axis): {height} pixels")
    print(f"-Number of channels: {channels}")
    print(f"-Total pixels: {height * width}")
    print("="*50)


def load_image(path: str) -> np.ndarray:
    """
    Load an image file and return its RGB pixel content as a numpy array.

    Args:
        path (str): Path to the image file

    Returns:
        np.ndarray: RGB pixel array of the image

    Raises:
        None
    """
    image = Image.open(path)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    return np.asarray(image)


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

    print_image_info(image)

    return image


def main() -> int:
    """
    Main function to test the ft_load function.
    """
    try:
        validate_args()

        print(ft_load("landscape.jpg"))

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
