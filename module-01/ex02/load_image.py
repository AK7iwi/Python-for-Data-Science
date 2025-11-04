import sys
from PIL import Image
import numpy as np
from validate_args import validate_args_for_test, MissingArgumentsError


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
    print("Image dimensions:")
    print(f"-Width (X axis): {width} pixels")
    print(f"-Height (Y axis): {height} pixels")
    print(f"-Number of channels: {channels}")
    print(f"-Total pixels: {height * width}")
    print("="*50)


def print_info(image: np.ndarray) -> None:
    """
    Print information about the image.

    Args:
        image (np.ndarray): The image to print information about

    Returns:
        None

    Raises:
        None
    """
    print(f"The shape of image is: {image.shape}")
    print_image_info(image)


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
    with Image.open(path) as image:
        if image.mode != 'RGB':
            image = image.convert('RGB')

        return np.asarray(image)


def ft_load(path: str) -> np.ndarray:
    """
    Load an image file and return its RGB pixel content as a numpy array.

    Args:
        path (str): Path to the image file

    Returns:
        np.ndarray: RGB pixel array of the image
        None: If there is an error

    Raises:
        None
    """
    try:
        image = load_image(path)
    except Image.UnidentifiedImageError as e:
        print(f"UnidentifiedImageError: {e}. Probably not a valid image file.")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except AttributeError:
        print(f"AttributeError: Not a valid image file: '{path}'")
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

    print_info(image)

    return image


def main() -> int:
    """
    Main function to test the ft_load function.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    print(ft_load("../images/valid_images/landscape.jpg"))

    return 0


if __name__ == "__main__":
    sys.exit(main())
