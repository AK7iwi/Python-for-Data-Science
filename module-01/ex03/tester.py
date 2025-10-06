from load_image import ft_load
from zoom import zoom_center_square_to_grayscale, print_image_info

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    image = ft_load("animal.jpeg")
    print_image_info(image)

    zoom_center_square_to_grayscale(image)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# All errors that can occur are handled by the load_image.py file
