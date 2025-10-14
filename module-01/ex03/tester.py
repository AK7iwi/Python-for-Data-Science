import numpy as np
from load_image import ft_load
from zoom import zoom_center_square_to_grayscale, display_image

# Test zoom_center_square_to_grayscale
print("--------------------------------")
print("Test zoom_center_square_to_grayscale")
print("--------------------------------")

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("../images/animal.jpeg")
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    image = "invalid"
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    image = np.asarray([1, 2, 3])
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    image = np.asarray([])
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "Zoomed Image")

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
    image = ft_load("../images/animal.jpeg")
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    zoomed_grayscale_image = "invalid"
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    zoomed_grayscale_image = np.asarray([1, 2, 3])
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    zoomed_grayscale_image = np.asarray([])
    display_image(zoomed_grayscale_image, "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4 - Invalid title: non-string value
print("Test 4 - Invalid title: non-string value")

try:
    image = ft_load("../images/animal.jpeg")
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, 123)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5 - Invalid title: empty string
print("Test 5 - Invalid title: empty string")

try:
    image = ft_load("../images/animal.jpeg")
    zoomed_grayscale_image = zoom_center_square_to_grayscale(image)
    display_image(zoomed_grayscale_image, "")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
