import numpy as np
from load_image import ft_load
from zoom import zoom_center_square_to_grayscale, display_image_with_scale, print_image_info

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("animal.jpeg")
    print_image_info(image)
    zoom_center_square_to_grayscale(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    image = "invalid"
    zoom_center_square_to_grayscale(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    image = np.array([1, 2, 3])
    zoom_center_square_to_grayscale(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    image = np.array([])
    zoom_center_square_to_grayscale(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# 
