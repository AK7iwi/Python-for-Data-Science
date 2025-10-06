from zoom import zoom_center_square_to_grayscale, display_image_with_scale

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    display_image_with_scale(zoom_center_square_to_grayscale("animal.jpeg"), "Zoomed Image")

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")