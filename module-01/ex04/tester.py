import numpy as np
from load_image import ft_load
from zoom import zoom_center_square_to_grayscale
from rotate import rotate_image, display_image

# Test rotate_image
print("--------------------------------")
print("Test rotate_image")
print("--------------------------------")

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("animal.jpeg")
    zoomed_image = zoom_center_square_to_grayscale(image)
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    zoomed_image = "invalid"
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    zoomed_image = np.asarray([1, 2, 3])
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    zoomed_image = np.asarray([])
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test display_image
print("--------------------------------")
print("Test display_image")
print("--------------------------------")

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("animal.jpeg")
    zoomed_image = zoom_center_square_to_grayscale(image)
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    rotated_image = "invalid"
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    rotated_image = np.asarray([1, 2, 3])
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    rotated_image = np.asarray([])
    display_image(rotated_image, "Rotated Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4 - Invalid title: non-string value
print("Test 4 - Invalid title: non-string value")

try:
    image = ft_load("animal.jpeg")
    zoomed_image = zoom_center_square_to_grayscale(image)
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, 123)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5 - Invalid title: empty string
print("Test 5 - Invalid title: empty string")

try:
    image = ft_load("animal.jpeg")
    zoomed_image = zoom_center_square_to_grayscale(image)
    rotated_image = rotate_image(zoomed_image)
    display_image(rotated_image, "")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
