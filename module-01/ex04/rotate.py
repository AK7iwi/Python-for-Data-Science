import sys
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load, print_image_info
from zoom import zoom_center_square_to_grayscale
from validate_args import validate_args_for_prog


def display_image(image: np.ndarray) -> None:
    """
    Display the image with scale on x and y axis.

    Args:
        image (np.ndarray): The image to display

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title("Rotated Image")
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
    print(f"\nNew shape after Transpose: {image.shape}")
    print_image_info(image)


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
    # 1 for the channel because grayscale image
    transposed = np.zeros((cols, rows, 1), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = image[i, j]

    return transposed


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
    transposed_image = manual_transpose(image)
    print_info(transposed_image)

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
        validate_args_for_prog()
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    image = ft_load("../images/valid_images/animal.jpeg")
    if image is None:
        return 1

    zoomed_image = zoom_center_square_to_grayscale(image)
    print(zoomed_image)

    rotated_image = rotate_image(zoomed_image)
    print(rotated_image)

    display_image(rotated_image)

    return 0


if __name__ == "__main__":
    sys.exit(main())
