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
    plt.imshow(image)
    plt.title(title)
    plt.xlabel('X axis (pixels)')
    plt.ylabel('Y axis (pixels)')
    plt.colorbar(label='Pixel intensity')
    plt.show()


def validate_zoom_parameters(start_x: int, start_y: int, 
                           end_x: int, end_y: int, 
                           image_shape: tuple) -> None:
    """
    Validate that zoom parameters are within image bounds.

    Args:
        start_x (int): Start x coordinate
        start_y (int): Start y coordinate
        end_x (int): End x coordinate
        end_y (int): End y coordinate
        image_shape (tuple): Shape of the image (height, width, channels)

    Returns:
        None

    Raises:
        ValueError: If parameters are out of bounds
    """
    height, width = image_shape[:2]
    
    if start_x < 0 or start_x >= width:
        raise ValueError(f"Start x ({start_x}) out of bounds [0, {width-1}]")
    if start_y < 0 or start_y >= height:
        raise ValueError(f"Start y ({start_y}) out of bounds [0, {height-1}]")
    if end_x <= start_x or end_x > width:
        raise ValueError(f"End x ({end_x}) must be > start_x and <= {width}")
    if end_y <= start_y or end_y > height:
        raise ValueError(f"End y ({end_y}) must be > start_y and <= {height}")


def zoom_image(image: np.ndarray, start_x: int, start_y: int, 
               end_x: int, end_y: int) -> np.ndarray:
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
    validate_zoom_parameters(start_x, start_y, end_x, end_y, image.shape)
    
    # Crop the image
    zoomed = image[start_y:end_y, start_x:end_x]

    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    
    return zoomed


def print_image_info(image: np.ndarray) -> None:
    """
    Print detailed information about the image.

    Args:
        image (np.ndarray): The image array

    Returns:
        None

    Raises:
        None
    """
    height, width, channels = image.shape
    
    print(f"Image dimensions:")
    print(f"-Width (X axis): {width} pixels")
    print(f"-Height (Y axis): {height} pixels")
    print(f"-Number of channels: {channels}")
    print(f"-Total pixels: {height * width}")


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
        image = ft_load("animal.jpeg")
        
        print("\n" + "="*50)
        print_image_info(image)
        print("="*50)
        
        # Define zoom area (center portion)
        height, width = image.shape[:2]
        center_x, center_y = width // 2, height // 2
        zoom_size = min(width, height) // 2
        
        start_x = center_x - zoom_size // 2
        start_y = center_y - zoom_size // 2
        end_x = center_x + zoom_size // 2
        end_y = center_y + zoom_size // 2
        
        print(f"\nZooming to area: ({start_x}, {start_y}) to ({end_x}, {end_y})")
        zoomed_image = zoom_image(image, start_x, start_y, end_x, end_y)

        display_image_with_scale(image, "Original Image")
        display_image_with_scale(zoomed_image, "Zoomed Image")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
