import numpy as np
from load_image import ft_load
from zoom import zoom_center_square_to_grayscale
from rotate import rotate_image

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("animal.jpeg")
    zoomed_image = zoom_center_square_to_grayscale(image)
    rotate_image(zoomed_image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    image = "invalid"
    rotate_image(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    image = np.array([1, 2, 3])
    rotate_image(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    image = np.array([])
    rotate_image(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
