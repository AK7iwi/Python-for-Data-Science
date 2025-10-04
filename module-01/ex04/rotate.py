import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

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
    
    # Check if grayscale or color
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(image)
    
    plt.title(title)
    plt.axis('off')
    plt.show()


def cut_square(image: np.ndarray) -> np.ndarray:
    """
    Cut a square part from the center of the image.

    Args:
        image (np.ndarray): The image to cut

    Returns:
        np.ndarray: Square portion of the image

    Raises:
        None
    """
    height, width = image.shape[:2]
    
    size = min(height, width)
    
    center_y, center_x = height // 2, width // 2
    
    start_y = center_y - size // 2
    end_y = center_y + size // 2
    start_x = center_x - size // 2
    end_x = center_x + size // 2
    
    square = image[start_y:end_y, start_x:end_x]
    
    return square


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
        transposed = np.zeros((cols, rows), dtype=image.dtype)
        for i in range(rows):
            for j in range(cols):
                transposed[j, i] = image[i, j]
    else:
        transposed = np.zeros((cols, rows, image.shape[2]), dtype=image.dtype)
        for i in range(rows):
            for j in range(cols):
                transposed[j, i] = image[i, j]
    
    return transposed


def main():
    """
    Main function to load, cut, and transpose an image.

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        image = ft_load("animal.jpeg")
        
        square_image = cut_square(image)
        print(f"Square image shape: {square_image.shape}")
        
        transposed_image = manual_transpose(square_image)
        
        print(f"New shape after Transpose: {transposed_image.shape}")
        print(transposed_image)
        
        display_image(transposed_image, "Transposed Image")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()
