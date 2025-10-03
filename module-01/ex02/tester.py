from load_image import ft_load

# Test 1a: Basic valid input
print("Test 1a: Basic valid input")

try:
    print(ft_load("landscape.jpg"))
    
except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1b: 