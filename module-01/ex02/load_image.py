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
    
    # Load image using PIL
    image = Image.open(path)
        
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
        
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    print(image_array)
        
    return image_array
