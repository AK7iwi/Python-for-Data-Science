import sys
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from validate_args import validate_args


def display_image_with_scale(image: np.ndarray, title: str) -> None:
    """
    Display image with scale on x and y axis.

    Args:
        image (np.ndarray): The image to display
        title (str): Title for the plot

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.xlabel('X axis (pixels)')
    plt.ylabel('Y axis (pixels)')
    plt.colorbar(label='Pixel intensity')
    plt.show()


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
    print(image)


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
    print(f"New shape after slicing: {image.shape}")
    print_image_info(image)


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert RGB image to grayscale using numpy.

    Args:
        image (np.ndarray): RGB image array

    Returns:
        np.ndarray: Grayscale image array

    Raises:
        None
    """
    # Check if image is already grayscale
    if len(image.shape) == 2:
        return image

    # Convert RGB to grayscale using standard formula
    grayscale = np.dot(image[..., :3], [0.299, 0.587, 0.114])
    grayscale = grayscale.astype(np.uint8)

    return grayscale


def define_zoom_area(image: np.ndarray) -> tuple:
    """
    Define the zoom area for the center portion of the image.

    Args:
        image (np.ndarray): The image to define zoom area for

    Returns:
        tuple: (start_x, start_y, end_x, end_y) coordinates

    Raises:
        None
    """
    height, width = image.shape[:2]
    center_x, center_y = width // 2, height // 2
    zoom_size = min(width, height) // 2

    start_x = center_x - zoom_size // 2
    start_y = center_y - zoom_size // 2
    end_x = center_x + zoom_size // 2
    end_y = center_y + zoom_size // 2

    return start_x, start_y, end_x, end_y


def zoom_center_square(image: np.ndarray) -> np.ndarray:
    """
    Zoom (crop) a portion of the image.

    Args:
        image (np.ndarray): The image to zoom

    Returns:
        np.ndarray: The zoomed image

    Raises:
        None
    """

    start_x, start_y, end_x, end_y = define_zoom_area(image)
    zoomed_image = image[start_y:end_y, start_x:end_x]

    print(f"\nZooming to area: ({start_x}, {start_y}) to "
          f"({end_x}, {end_y})")

    return zoomed_image


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


def zoom_center_square_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Zoom (crop) a portion of the image and convert to grayscale.

    Args:
        image (np.ndarray): The image to zoom

    Returns:
        np.ndarray: The zoomed grayscale image

    Raises:
        None
    """
    validate_image_array(image)

    zoomed_image = zoom_center_square(image)
    zoomed_grayscale_image = convert_to_grayscale(zoomed_image)
    print_info(zoomed_grayscale_image)

    display_image_with_scale(zoomed_grayscale_image, "Zoomed Image")

    return zoomed_grayscale_image


def main() -> int:
    """
    Main function to load, analyze, zoom and display an image.

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
        print_image_info(image)
        zoom_center_square_to_grayscale(image)

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
