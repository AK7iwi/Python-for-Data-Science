import numpy as np
import matplotlib.pyplot as plt
from zoom import zoom_center_square_to_grayscale


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


def rotate_image(zoomed_image: np.ndarray) -> np.ndarray:
    """
    Rotate a 2D array (no library allowed).

    Args:
        image (np.ndarray): The image to rotate

    Returns:
        np.ndarray: Rotated image

    Raises:
        None
    """
    transposed_image = manual_transpose(zoomed_image)

    return transposed_image


def main():
    """
    Main function to load, cut, and transpose an image.

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        _, zoomed_image, *_ = zoom_center_square_to_grayscale("animal.jpeg")
        transposed_image = rotate_image(zoomed_image)

        print(f"Square image shape: {transposed_image.shape}")
        print(zoomed_image)
        print(f"New shape after Transpose: {transposed_image.shape}")
        print(transposed_image)

        display_image(transposed_image, "Transposed Image")

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
