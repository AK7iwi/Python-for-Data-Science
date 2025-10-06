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

# All errors that can occur are handled by the load_image.py file
