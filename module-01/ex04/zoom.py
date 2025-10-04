import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


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


def zoom_image(image: np.ndarray) -> tuple:
    """
    Zoom (crop) a portion of the image.

    Args:
        image (np.ndarray): The image to zoom
        start_x (int): Start x coordinate
        start_y (int): Start y coordinate
        end_x (int): End x coordinate
        end_y (int): End y coordinate

    Returns:
        np.ndarray: The zoomed image

    Raises:
        None
    """

    start_x, start_y, end_x, end_y = define_zoom_area(image)
    zoomed = image[start_y:end_y, start_x:end_x]

    return zoomed, start_x, start_y, end_x, end_y


def print_image_info(image: np.ndarray) -> None:
    """
    Print detailed information about the original image.

    Args:
        image (np.ndarray): The original image array

    Returns:
        None

    Raises:
        None
    """
    height, width, channels = image.shape

    print("\n" + "="*50)
    print("Image dimensions:")
    print(f"-Width (X axis): {width} pixels")
    print(f"-Height (Y axis): {height} pixels")
    print(f"-Number of channels: {channels}")
    print(f"-Total pixels: {height * width}")
    print("="*50)


def load_image(path: str) -> np.ndarray:
    """
    Load an image.

    Args:
        path (str): Path to the image

    Returns:
        np.ndarray: The image

    Raises:
        None
    """
    return ft_load(path)


def main():
    """
    Main function to load, analyze, and zoom an image.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        image = load_image("animal.jpeg")
        print_image_info(image)

        zoomed_image, start_x, start_y, end_x, end_y = zoom_image(image)
        print(f"\nZooming to area: ({start_x}, {start_y}) to "
              f"({end_x}, {end_y})")

        grayscale_image = convert_to_grayscale(zoomed_image)
        print(f"New shape after zooming: {grayscale_image.shape}")

        display_image_with_scale(grayscale_image, "Zoomed Image")

        print(grayscale_image)

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
