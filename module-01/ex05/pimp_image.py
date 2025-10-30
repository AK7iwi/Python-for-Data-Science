import sys
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from validate_args import validate_args_for_test, MissingArgumentsError


def validate_image_array(image: np.ndarray) -> None:
    """
    Validate that the input is a valid image array.

    Args:
        image (np.ndarray): The image to validate

    Returns:
        None

    Raises:
        TypeError: If image is not a numpy array
        ValueError: If image is invalid
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a numpy array")
    if len(image.shape) < 2:
        raise ValueError("Image must be at least 2D")


def display_image(image: np.ndarray, title: str) -> None:
    """
    Display the image with scale on x and y axis.

    Args:
        image (np.ndarray): The image to display
        title (str): Title for the plot

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.

    Args:
        array (np.ndarray): The image array to invert

    Returns:
        np.ndarray: The inverted image array
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_image_array(array)
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

    inverted = 255 - array

    display_image(inverted, "Inverted Image")

    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image.

    Args:
        array (np.ndarray): The image array to filter

    Returns:
        np.ndarray: The red-filtered image array
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_image_array(array)
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

    # Keep only red channel, set green and blue to 0
    red_filtered = array.copy()
    red_filtered[:, :, 1] = 0  # Green channel = 0
    red_filtered[:, :, 2] = 0  # Blue channel = 0

    display_image(red_filtered, "Red Filter")

    return red_filtered


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image.

    Args:
        array (np.ndarray): The image array to filter

    Returns:
        np.ndarray: The green-filtered image array
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_image_array(array)
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

    # Keep only green channel, set red and blue to 0
    green_filtered = array.copy()
    green_filtered[:, :, 0] = 0  # Red channel = 0
    green_filtered[:, :, 2] = 0  # Blue channel = 0

    display_image(green_filtered, "Green Filter")

    return green_filtered


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image.

    Args:
        array (np.ndarray): The image array to filter

    Returns:
        np.ndarray: The blue-filtered image array
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_image_array(array)
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

    # Keep only blue channel, set red and green to 0
    blue_filtered = array.copy()
    blue_filtered[:, :, 0] = 0  # Red channel = 0
    blue_filtered[:, :, 1] = 0  # Green channel = 0

    display_image(blue_filtered, "Blue Filter")

    return blue_filtered


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applies a grey filter to the image.

    Args:
        array (np.ndarray): The image array to convert

    Returns:
        np.ndarray: The grey-filtered image array
        None: If there is an error

    Raises:
        None
    """
    try:
        validate_image_array(array)
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

    # Grayscale conversion using per-pixel mean across channels
    grayscale = array.mean(axis=2)
    grayscale = grayscale.astype(np.uint8)
    grayscale_3d = np.stack([grayscale, grayscale, grayscale], axis=2)

    display_image(grayscale_3d, "Grey filter")

    return grayscale_3d


def main():
    """
    Main function to test all filter functions.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    array = ft_load("../images/valid_images/landscape.jpg")
    if array is None:
        return 1
    print(array)

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)

    return 0


if __name__ == "__main__":
    sys.exit(main())
