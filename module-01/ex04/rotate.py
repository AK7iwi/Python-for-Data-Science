import sys
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from zoom import zoom_center_square_to_grayscale
from validate_args import validate_args


def display_image(image: np.ndarray, title: str) -> None:
    """
    Display the image with matplotlib.

    Args:
        image (np.ndarray): The image to display
        title (str): Title for the plot

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.xlabel('X axis (pixels)')
    plt.ylabel('Y axis (pixels)')
    plt.show()


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
    print(f"New shape after Transpose: {image.shape}")
    print(image)


def manual_transpose(image: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D array (no library allowed).

    Args:
        image (np.ndarray): The image to transpose

    Returns:
        np.ndarray: Transposed image

    Raises:
        None
    """
    rows, cols = image.shape[:2]

    if len(image.shape) == 2:
        channels = 1
    else:
        channels = image.shape[2]

    transposed = np.zeros((cols, rows, channels), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = image[i, j]

    return transposed


def validate_image_array(image: np.ndarray) -> None:
    """
    Validate that the input is a valid image array.
    
    Args:
        image (np.ndarray): The image to validate
        
    Raises:
        TypeError: If image is not a numpy array
        ValueError: If image is invalid
    
    Returns:
        None
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a numpy array")
    if len(image.shape) < 2:
        raise ValueError("Image must be at least 2D")
    if image.size == 0:
        raise ValueError("Image cannot be empty")


def rotate_image(image: np.ndarray) -> np.ndarray:
    """
    Rotate a 2D array (no library allowed).

    Args:
        image (np.ndarray): The image to rotate

    Returns:
        np.ndarray: Rotated image

    Raises:
        None
    """
    validate_image_array(image)

    transposed_image = manual_transpose(image)
    print_info(transposed_image)

    display_image(transposed_image, "Transposed Image")

    return transposed_image


def main() -> int:
    """
    Main function to load, cut, and transpose an image.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        validate_args()

        image = ft_load("animal.jpeg")
        zoomed_image = zoom_center_square_to_grayscale(image)
        rotate_image(zoomed_image)

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
